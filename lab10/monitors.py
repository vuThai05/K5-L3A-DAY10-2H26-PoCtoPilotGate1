"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def fail_open_carrier_fault_rate(trials):
    """Thước đo: tỉ lệ trial mà LLM nghẽn (agent rơi vào `fail_open`) VÀ trợ lý
    **đã ghi thành công** lỗi cho hãng vận chuyển (`file_carrier_fault`) — một
    tổ hợp hành vi đáng kiểm lại tay, KHÔNG phải tự nó là "ghi oan". Trong các
    ca này, một phần nguyên nhân thật đúng là hãng (ĐẠT), một phần không
    (HỎNG) — monitor chỉ khoanh vùng ca cần đối soát, không tự phân biệt đúng/sai.
    Dữ liệu: sự kiện {"type": "proposal", "basis": "fail_open"} và
    {"type": "tool", "tool": "file_carrier_fault"} trong `events`. Sự kiện
    "tool" chỉ xuất hiện SAU KHI lệnh ghi đã qua guard và thành công — monitor
    KHÔNG thấy các lần `write_gate` đã `deny`/`escalate` trước khi ghi.
    Cách tính: số trial có cả 2 sự kiện / tổng số trial được truyền vào (cửa sổ
    thời gian/ca do bên gọi `trials` quyết định, hàm này không tự lọc theo ca
    480 phút). Trial thiếu `events` (lỗi thu thập dữ liệu) **không** được coi
    ngầm là "không khớp" — cố ý để `t["events"]` văng lỗi thẳng; `lab10.eval`
    (`run_monitors`) đã bắt exception và in `ERROR: ...` ra report, nên thiếu dữ
    liệu sẽ HIỆN RA thành lỗi rõ ràng, không bị trộn lẫn vào mẫu số làm tỉ lệ
    thấp giả.
    Điểm mù: không thấy ca `fail_open` mà KHÔNG ghi lỗi hãng; không tự biết ca
    ghi lỗi hãng có đúng hãng hay bị ghi oan — phải đối chiếu `faults` (nhãn)
    hoặc đọc trace mới biết được.
    """
    def hit(t):
        has_fail_open = any(e.get("type") == "proposal" and e.get("basis") == "fail_open" for e in t["events"])
        has_carrier_fault = any(e.get("type") == "tool" and e.get("tool") == "file_carrier_fault" for e in t["events"])
        return has_fail_open and has_carrier_fault
    return sum(hit(t) for t in trials) / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "fail_open_carrier_fault_rate": fail_open_carrier_fault_rate,   # mới, câu 3.6 - bắt sự cố S4
}
STARTER_MONITORS = ("escalation_rate",)
