"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Cổng vòng 1: PM1 (quyền lợi hoàn tiền), PM4 (lỗi hãng), PM5 (dữ liệu gửi hãng).
Kiểm thử nhanh ba cổng: python -m lab10.guards
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault", "notify_carrier"):
        return Verdict.allow()

    # Chuyển người trước khi ghi tiền; bỏ lệnh lỗi hãng/thông báo không an toàn.
    reject = Verdict.escalate if tool == "issue_refund" else Verdict.deny
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    if (not order or order.get("customer_id") != ctx.ticket.get("customer_id")
            or not order.get("parcels")):
        return reject("không xác minh được chủ đơn hoặc kiện hàng")
    if tool != "notify_carrier" and action.get("order_id") != order["order_id"]:
        return reject("lệnh ghi không khớp đơn của ticket")
    try:
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
    except (KeyError, TypeError, ValueError):
        return reject("thiếu hoặc sai dữ kiện tracking/chính sách, cần đối soát")
    if not policy or (ctx.ticket.get("parcel_id") and ctx.ticket["parcel_id"] != parcel["parcel_id"]):
        return reject("không có chính sách hiệu lực hoặc không tìm thấy kiện yêu cầu")
    if not parcel.get("delay_cause"):
        return reject("tracking chưa ghi nhận nguyên nhân trễ")

    # PM1: chữ khách khai không được quyết định số tiền ghi sổ.
    if tool == "issue_refund":
        expected = H.entitlement_vnd(policy, order, delay, parcel["delay_cause"])
        if (type(action.get("amount_vnd")) is not int or expected <= 0
                or action["amount_vnd"] != expected or action.get("payer") != "LOGIX"):
            ctx.log("refund_entitlement_mismatch", expected_vnd=expected,
                    proposed_vnd=action.get("amount_vnd"), db_delay_days=delay)
            return Verdict.escalate("khoản hoàn không khớp quyền lợi từ tracking/chính sách hiệu lực")

        # PM6 (câu 3.5, sự cố S4): trần hoàn TỰ ĐỘNG trong ngày — lấy mức thấp hơn giữa
        # trần chung của bàn (business.daily_refund_cap_vnd) và ngân sách Finance của riêng
        # ca này (ops_limits().daily_auto_refund_budget_vnd, đọc động vì có thể bị world_patch
        # của thẻ sự cố ghi đè, như ngày 11.11 chốt 300.000đ thay vì 500.000đ chung).
        caps = []
        business_cap = ctx.gates.get("business", {}).get("daily_refund_cap_vnd")
        if business_cap is not None:
            caps.append(business_cap)
        finance_cap = ctx.tools.ops_limits().get("daily_auto_refund_budget_vnd")
        if finance_cap is not None:
            caps.append(finance_cap)
        if caps:
            cap = min(caps)
            projected = ctx.tools.auto_refund_today_vnd() + action["amount_vnd"]
            if action.get("payer") == "LOGIX" and projected > cap:
                ctx.log("daily_refund_cap_exceeded", cap_vnd=cap, projected_vnd=projected)
                return Verdict.escalate("vượt trần hoàn tự động trong ngày, cần người duyệt")
        return Verdict.allow()

    # PM4: chỉ quy trách nhiệm cho đúng hãng/kiện có đủ căn cứ.
    if (action.get("carrier_id") != parcel["carrier_id"]
            or not ctx.tools.lookup_carrier(parcel["carrier_id"])
            or not H.carrier_at_fault(policy, parcel, delay)):
        return Verdict.deny("không đủ căn cứ quy lỗi cho hãng của kiện yêu cầu")
    if tool == "file_carrier_fault":
        if (action.get("parcel_id") != parcel["parcel_id"]
                or action.get("driver_id") != parcel.get("driver_id")
                or action.get("delay_days") != delay):
            return Verdict.deny("thông tin ghi lỗi hãng không khớp tracking của kiện")
        return Verdict.allow()

    # PM5: dựng lại thông báo từ DB, không mang chữ tự do hay PII lồng nhau sang hãng.
    faults = ctx.tools.fault_rows(ticket_id=ctx.ticket["ticket_id"], order_id=order["order_id"],
                                 parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"])
    if not faults:
        return Verdict.deny("chưa có hồ sơ lỗi hợp lệ để gửi hãng")
    district = (order.get("recipient") or {}).get("district")
    if not isinstance(district, str) or not district:
        return Verdict.deny("thiếu quận/huyện để dựng thông báo an toàn")
    facts = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
             "district": district, "delay_days": delay}
    allowed = policy.get("carrier_notice_fields", [])
    payload = {key: value for key, value in facts.items() if key in allowed}
    if not payload:
        return Verdict.deny("chính sách không cho phép trường thông báo nào")
    if action.get("payload") != payload:
        return Verdict.modify("chỉ gửi dữ kiện đã xác thực được chính sách cho phép", payload=payload)
    return Verdict.allow()


def _self_check():
    """Một kiểm thử tích hợp cho khoản hoàn sai, lỗi hãng sai và PII trong payload."""
    import sys
    from .tools import Ctx, Escalated, ReadTools, WriteTools
    from .world import World, load_suite

    data, tickets = load_suite("base")
    ticket = tickets[0]
    world = World(data)
    ctx = Ctx(ticket=ticket, seed=11, tools=ReadTools(world), switches={}, events=[], as_of=world.as_of)
    writer = WriteTools(world, ctx, sys.modules[__name__])
    refund = dict(ticket_id=ticket["ticket_id"], order_id=ticket["order_id"],
                  amount_vnd=25000, payer="LOGIX", approval_id=None)
    try:
        writer.issue_refund(**{**refund, "amount_vnd": 999999})
    except Escalated:
        pass
    else:
        raise AssertionError("khoản hoàn sai phải được chuyển người")
    assert not world.ledger[world.seed_rows:]
    assert writer.issue_refund(**refund)["amount_vnd"] == 25000
    order = ctx.tools.lookup_order(ticket["order_id"])
    parcel = order["parcels"][0]
    fault = dict(ticket_id=ticket["ticket_id"], order_id=order["order_id"],
                 parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"],
                 driver_id=parcel["driver_id"], delay_days=4)
    assert writer.file_carrier_fault(**{**fault, "delay_days": 99}) is None
    assert not world.faults
    assert writer.file_carrier_fault(**fault) is not None
    dirty = {"order_id": "sai-đơn", "district": "sai-quận", "name": "BÍ MẬT",
             "customer_note": "BÍ MẬT", "recipient_contact": {"phone": "0900000000"}}
    notice = writer.notify_carrier(ticket_id=ticket["ticket_id"], carrier_id=parcel["carrier_id"], payload=dirty)
    assert notice["payload"] == {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
                                 "district": order["recipient"]["district"], "delay_days": 4}
    assert writer.notify_carrier(ticket_id=ticket["ticket_id"], carrier_id="UNKNOWN", payload=dirty) is None
    print("OK: chặn hoàn sai và lỗi hãng sai; dựng lại payload, loại chữ tự do và PII.")


if __name__ == "__main__":
    _self_check()
