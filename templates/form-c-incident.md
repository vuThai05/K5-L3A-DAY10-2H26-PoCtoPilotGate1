# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** K5-L3A-DAY10-2H26-PoCtoPilotGate1 · **Thẻ đã bốc:** S4

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | | Sx · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | | | | | |
| 2 | | Sx · after | | | | | | |
| 3 | | Sx · after | | | | | | |
| 4 | | base · after | (kiểm không regression) | | | | | |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `R-S4-grade-20261119-001513-5dc727` · base: `R-S4-before-20261119-001514-5dc727` · prepared: `R-S4-prepared-20261119-001514-5dc727`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): trên khối **"visible"** (gói sự cố), `pass_rate` 0,8683 → 1,0; `wrongful_refund_vnd` 160.000đ → 0đ; `wrongful_carrier_faults` 27 → 0. Cổng PM1 (quyền lợi hoàn tiền) và PM4 (lỗi hãng) tự xử lý sạch toàn bộ ticket còn **trong phạm vi pilot** (`HN`, `HCM`).
- Khối kinh doanh và vận hành còn dòng nào vượt trần: Report tự động in "Không vượt trần" — nhưng đây là **vượt trần ẩn**: `business.daily_refund_cap_vnd` (500.000đ, đặt ở vòng 1) **cao hơn** mức Finance chốt riêng cho ngày sale 11.11 (`world_patch.json`: 300.000đ). Ở base (chưa cổng), tổng hoàn trên gói S4 đã 466.000đ — thật ra đã vượt mức 300k của ngày đó, report không báo vì so với cổng chung (500k) chứ không biết mức riêng theo ngày. Ở prepared hiện tại (292.000đ) tình cờ vẫn dưới cả 2 mức nên chưa lộ rõ — xem HAZOP dòng 4 (C4) và fault tree [4] (C6). Riêng độ phủ pilot giảm còn 0,561 (so 1,0 ở base) vì `pilot_scope` loại kho DN/CT — lý do ticket `S4-08` (kho DN) không được đo trực tiếp ở mốc prepared/after.

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? **Cả hai**: phần "hàng chờ ngập, cần thêm người" thuộc lăng kính **con người và vận hành**; phần "LLM nghẽn thì trợ lý duyệt nhiều hơn, ghi lỗi hãng sai" thuộc lăng kính **kỹ thuật**.
- Có nằm trong các lý do bàn đã viết không? **PM3** (Phiếu B mục B6, do Thái viết ở vòng 1) đã đúng y phần hàng chờ: *"Ticket chuyển người và ca kiểm mẫu đã dồn vào giờ cao điểm, vượt công suất trực; khách đã chờ quá SLA"* — cổng vòng 1 đỡ được phần vận hành (runbook B7.6, `operations.reviewers_on_shift`), report S4 cho thấy `queue_stuck = 0` ở cả 2 mốc (không ùn thật trên gói hiển thị). **Nhưng phần kỹ thuật (LLM nghẽn → ghi sai lỗi hãng) KHÔNG nằm trong pre-mortem vòng 1** — cả bàn không nghĩ tới nhánh `fail_open` cụ thể này.
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| LLM bị giới hạn tốc độ (429) liên tiếp ở giờ cao điểm, trợ lý rơi vào `fail_open` và ghi oan lỗi hãng cho đơn do shop giao muộn. | Kỹ thuật | `lab10.trace --suite S4 --ticket S4-08 --seed 11`: event `llm_error` ×2 → `llm_fallback` (`fail_open`) → `proposal.do_fault: true` dù `tracking.cause: MERCHANT_HANDOVER` |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `khách hàng (nhận tiền không đủ điều kiện) và hãng vận chuyển (bị ghi oan lỗi giao trễ)` · đo bằng gì `wrongful_refund_vnd, wrongful_carrier_faults` · bao nhiêu ở mốc base `160.000đ hoàn sai · 27 lỗi hãng oan (khối "visible" của report S4)`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | `S4-08@11`: trace 02 `tracking` ghi `delay:4, cause: MERCHANT_HANDOVER`; trace 04-05 `llm_error` ×2 (429); trace 06 `llm_fallback` (`fail_open`); trace 07 `proposal.do_fault: true`; trace 09 `file_carrier_fault` ghi VNX. Nhãn `faults: []`. | Hãng VNX/tài xế TX-VNX-02 bị quy oan lỗi; khách C-09 vẫn được hoàn đúng 24.000đ (không sai phần tiền) | Cao | **Chìm** — khách thấy "được hoàn, ổn", hệ thống báo `refunded` bình thường; chỉ hãng đối soát mới phát hiện bị ghi lỗi không đúng |
| 2 | `S4-30@22`: trace 02 `tracking` ghi `delay:2, cause: MERCHANT_HANDOVER` (2 ngày — **dưới** `REFUND-v3.late.min_days_fee=3`, nhãn `status: denied`); trace 04-06 cùng `fail_open`; trace 07 `do_fault: true`, hoàn 18.000đ; trace 09 ghi lỗi hãng DNB. | Khách C-07 nhận tiền không đủ điều kiện; hãng DNB bị ghi oan; LogiX mất tiền không thu lại được | Cao | **Giới hạn hệ thống** — nhánh dự phòng (`fail_open`) không có logic so ngưỡng `min_days_fee`, một giới hạn có sẵn trong thiết kế, không phải do dữ liệu nhiễu |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 (`S4-08`) | Lỗi 2 (`S4-30`) |
|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? | Không — `claimed_delay_days: null`, `trust_claim: false`; khách không tự khai số ngày | Không — tương tự, khách chỉ hỏi chung, không khai số |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? | **Có, nhưng khác kiểu:** dữ liệu đã đủ trong tracking (`cause`, `delay`) nhưng nhánh `fail_open` **không đọc lại** để xác nhận `cause` hợp lệ trước khi ghi lỗi hãng | **Có, nghiêm trọng hơn:** dữ liệu đã đủ để biết `delay=2 < min_days_fee=3` (không đủ điều kiện hoàn), nhưng `fail_open` bỏ qua luôn bước so ngưỡng |
| **Thứ bậc hệ thống:** hai hệ thống cùng ghi mà không rõ ai là chủ? | Không có bằng chứng | Không có bằng chứng |
| **Trạng thái hỏng:** nhiều lỗi cộng lại làm tính năng không dùng được? | **Có** — 2 lần `429` liên tiếp kích hoạt `fail_open`, tắt hẳn bước kiểm chính sách | **Có** — cùng cơ chế, hậu quả nặng hơn vì bỏ qua cả điều kiện hoàn tối thiểu |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 (`S4-08`) | Lỗi 2 (`S4-30`) |
|---|---|---|
| Vì sao người gặp coi đây là lỗi | Hãng bị quy trách nhiệm dù tracking ghi nguyên nhân khác (`MERCHANT_HANDOVER`), ảnh hưởng đối soát và có thể bị phạt/đình chỉ oan | Khách nhận tiền không đủ điều kiện (2 ngày < 3 ngày hạn), LogiX mất tiền không thu lại được, hãng cũng bị ghi oan |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | Trao quyền cho người: khi rơi `fail_open`, chuyển ticket cho người duyệt đối soát tracking trước khi ghi lỗi hãng, không tự quyết | Trao quyền cho người, giống lỗi 1 — `fail_open` không nên tự ý ghi sổ/ghi lỗi khi chưa xác nhận lại ngưỡng |
| Đường đi của người sau khi có giải pháp | `fail_open` → chuyển người duyệt (chị Hạnh) → đối soát tracking/chính sách → quyết lại (hoàn hay không, ghi lỗi hãng hay không) | Tương tự: chuyển người duyệt → kiểm `min_days_fee` bằng tay → từ chối hoàn nếu chưa đủ điều kiện |
| Hệ thống học được gì (tín hiệu theo dõi: tên metric trong `monitors.py`) | `fail_open_carrier_fault_rate` (đã thêm, câu 3.6) — bắt đúng tổ hợp `fail_open` + `file_carrier_fault` | Cùng metric `fail_open_carrier_fault_rate`; có thể mở rộng thêm sau để tách riêng trường hợp hoàn dưới ngưỡng |

Yêu cầu: ≥2 lỗi nguồn khác nhau (lỗi 1: thiếu xác nhận `cause`; lỗi 2: thiếu so ngưỡng `min_days_fee` — cùng gốc `fail_open` nhưng biểu hiện/mức độ khác) — đủ 1 lỗi chìm (lỗi 1).

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | | | |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | | | |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | | | |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | | | |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: `__________`.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: `__________`. Ghi các con số đó vào `config/operating_gates.json` mục `operations`.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `issue_refund` + `file_carrier_fault` (qua đường LLM `policy_check`)

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| Kết quả `llm.policy_check` | **INCAPABLE** | Giờ cao điểm (ticket gấp 3, thẻ S4) → LLM trả `429` 2 lần liên tiếp → agent rơi `fail_open`, gán cứng `do_fault=True` (`S4-08@seed11,55`) dù tracking ghi `delay_cause: MERCHANT_HANDOVER` | Hãng VNX bị ghi oan lỗi, khách được hoàn 24.000đ không đúng điều kiện | `pre_guard`/`write_gate` hiện có PM4 kiểm `carrier_at_fault` — **nhưng chưa kiểm chứng được** vì ticket này (kho DN) đã bị `pilot_scope` loại trước khi tới agent | Thêm test trực tiếp PM4 trên ticket trong phạm vi (HN/HCM) có `fail_open`; không dựa vào `pilot_scope` để "né" — tầng **chặn** (đã có, cần verify) |
| `review_sampling`/hàng chờ người duyệt | **INCAPABLE** | 1 người trực × 6 ca/giờ, ticket gấp 3 → PM3 (pre-mortem vòng 1) đã đoán đúng nguy cơ ùn | Chị Hạnh quá tải, khách chờ quá SLA 60 phút | `operations.reviewers_on_shift`, runbook Giờ cao điểm (B7.6) đã có ngưỡng gọi thêm người | Giữ nguyên, bổ sung ngưỡng cụ thể vào B7.6 (xem C3) — tầng **vận hành** |
| Tỉ lệ `fail_open` theo giờ | **WRONG** *(nhánh bàn chưa thấy trên trace lúc viết — chỉ lộ ra khi so sánh nhiều seed)* | Trước câu 3.6, không có chỉ số nào tách riêng ca `fail_open`; report chỉ gộp chung vào `escalation_rate`, không phân biệt được "khách chủ động được chuyển người" với "máy đang gặp lỗi 429" | Vận hành không biết LLM đang nghẽn bao nhiêu % cho tới khi hoàn/lỗi hãng sai đã xảy ra | Không có gì trước câu 3.6 | `monitors.fail_open_carrier_fault_rate` (đã thêm, câu 3.6) — tầng **phát hiện** |
| `business.daily_refund_cap_vnd` | **INVALID** *(con số vòng 1 không còn đúng cho ngày này — phát hiện khi soát lại PR, chưa ai nói tới trước)* | `incidents/S4/world_patch.json → ops_limits.daily_auto_refund_budget_vnd = 300.000đ` — Finance chốt **riêng cho ngày 11.11 (sale)**, THẤP HƠN mức chung `business.daily_refund_cap_vnd = 500.000đ` nhóm đặt ở câu 2.9 (vòng 1, trước khi biết thẻ). Ở mốc base (chưa cổng), tổng hoàn tự động trên gói S4 đã lên **466.000đ** — vượt xa mức 300.000đ thật của ngày đó | Nếu lượng ticket nhích thêm (ví dụ còn 310.000–499.000đ), cổng hiện tại **không chặn** vì vẫn dưới 500k, trong khi đúng ra phải chuyển người duyệt từ 300k. Ở mốc `prepared` hiện tại tổng chỉ 292.000đ — **dưới cả 2 mức, nên trùng hợp chưa lộ**, không phải vì cổng đã kiểm đúng số | Cổng đọc hằng số cứng `operating_gates.json`, không đọc được mức override theo ngày trong `world_patch.json` của gói sự cố | Sửa `daily_refund_cap_vnd` xuống 300.000đ cho đúng ngày sale, hoặc đọc `ops_limits` của gói đang chạy thay vì số cứng — tầng **chặn** (chưa có, cần làm ở câu 3.5) |

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

**Specification:** Trợ lý chỉ được gọi `file_carrier_fault` khi `delay_cause` ghi nhận trong tracking thuộc đúng `fault_causes` của chính sách đang hiệu lực — **không được suy ra `do_fault` chỉ từ việc LLM không trả lời được**. Vi phạm specification này chính là nguyên nhân của `S4-08`: `do_fault=True` được gán cứng ở nhánh `fail_open` (`lab10/agent.py` dòng ~154), bỏ qua `delay_cause: MERCHANT_HANDOVER` thật trong tracking.

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): hàm `H.carrier_at_fault(policy, parcel, delay)` (đã dùng trong PM4 của `write_gate`); dòng report `wrongful_carrier_faults` (base S4 = 27, sau cổng vòng 1 trên phạm vi pilot = 0).

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

**Giả định (thứ nằm NGOÀI phần mềm):** Thiết kế `fail_open` ngầm tin rằng LLM bị giới hạn tốc độ (429) là tình huống **hiếm, ngẫu nhiên, không liên quan gì tới lượng ticket** — nên "mở khoá tạm" (ưu tiên trả lời nhanh, hoàn phí cho yên khách) là đánh đổi chấp nhận được.

**Vì sao có thể sai:** Trong thực tế, số lần gọi LLM và khả năng bị rate-limit **tỉ lệ thuận với lượng ticket cùng lúc** — đúng giờ cao điểm (ticket gấp 3, kịch bản S4) là lúc hệ thống *cần chính xác nhất* thì cũng là lúc *dễ rơi vào fail_open nhất*. Hai biến này không độc lập như giả định, nên "hiếm và ngẫu nhiên" không còn đúng đúng lúc rủi ro cao nhất.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `__________`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: hãng vận chuyển (VNX) bị ghi oan lỗi giao trễ (cho ai: hãng VNX/tài xế, đo bằng: wrongful_carrier_faults)
 └─ HOẶC
 ├─ [1] LLM bị 429 dồn ở giờ cao điểm → fail_open → do_fault gán cứng True    tầng: đầu vào / model
 │ └─ vì: nhánh fail_open không tra lại delay_cause thật    bằng chứng: ticket S4-08@seed 11 (và 55)
 ├─ [2] Guard PM4 chưa được kiểm chứng trên ticket thật đi qua agent    tầng: vận hành / phạm vi
 │ └─ vì: pilot_scope (HN/HCM) loại ticket kho DN trước khi tới write_gate    bằng chứng: S4-08 thuộc kho DN, báo "nằm ngoài pilot_scope" khi trace --stage after
 └─ [3] Không có tín hiệu riêng cảnh báo tỉ lệ fail_open tăng ở giờ cao điểm    tầng: vận hành / giám sát
 └─ vì: monitors.py (trước câu 3.6) chỉ có escalation_rate, không tách fail_open    bằng chứng: report trước câu 3.6 không có cột nào cho fail_open
```

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | `do_fault` phải dựa vào `carrier_at_fault(tracking)`, không phải cờ nội bộ gán cứng khi LLM lỗi | "429 hiếm và ngẫu nhiên, không liên quan lượng ticket" (câu 3.3) |
| [2] | Cổng PM4 phải áp dụng cho MỌI ticket đi qua agent, không phụ thuộc `pilot_scope` đang thu hẹp | "Thu hẹp phạm vi pilot là cách ngăn rủi ro" — thực ra chỉ **né**, chưa **ngăn**, vì nếu mở rộng `pilot_scope` sau này, lỗi [1] có thể lộ lại |
| [3] | Phải có chỉ số theo dõi riêng cho những nhánh ghi sổ dựa trên đường dự phòng (`fail_open`) | "`escalation_rate` đủ để biết trợ lý đang gặp khó" — không đúng, vì `fail_open` vẫn tự xử lý (không escalate), chỉ là xử lý sai |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

**Chưa mô hình hoá — tác hại THỨ HAI trên thẻ (không dừng ở nhánh đầu tiên):** thẻ S4 còn nêu rõ *"tổng hoàn tự động hôm nay đã vượt 300.000đ, là mức Finance chốt riêng cho ngày sale"* — đây là một **đỉnh khác** (tác hại cho Finance/LogiX, đo bằng tổng hoàn tự động/ngày), chưa vẽ cây riêng. Gốc đã biết: `business.daily_refund_cap_vnd` (500.000đ, đặt ở vòng 1 trước khi có thẻ) **cao hơn** mức riêng ngày 11.11 (300.000đ, trong `incidents/S4/world_patch.json`). Xem HAZOP dòng 4 (C4) — cần cả bàn quyết có vẽ thêm cây này hay gộp vào bảng sửa C7 luôn.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | | | | | |
| [2] | | | | | |
| [3] | | | | | |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | `fail_open_carrier_fault_rate` |
| **Bước / hành vi được đo** | Nhánh dự phòng khi LLM nghẽn (`fail_open`) có đi kèm ghi lỗi hãng (`file_carrier_fault`) hay không |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ trial có cả sự kiện `proposal.basis == "fail_open"` VÀ lệnh `file_carrier_fault` được gọi (%) |
| **Dữ liệu** (trường nào của trial, không có nhãn) | `events[].type == "proposal"` kèm `basis`; `events[].type == "tool"` kèm `tool == "file_carrier_fault"` — đọc trực tiếp từ `events`, không cần nhãn đúng/sai |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Với mỗi trial: `hit = có event proposal.basis=="fail_open" VÀ có event tool=="file_carrier_fault"`. Chỉ số = số trial `hit` / tổng số trial. Trial không có `events` (lỗi chạy) tính là không `hit`, không loại khỏi mẫu số |
| **Khung thời gian / ngưỡng báo động** | Theo ca giờ cao điểm (480 phút); ngưỡng an toàn = 0 (ảnh hưởng bên thứ ba là hãng vận chuyển, không chấp nhận có ca nào) |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | Không thấy ca `fail_open` mà KHÔNG ghi lỗi hãng (ví dụ ticket đó không cần `file_carrier_fault` vì lý do khác) — chỉ số này chỉ bắt đúng tổ hợp 2 sự kiện, không đo mọi hậu quả của `fail_open` (ví dụ hoàn tiền sai mà không kèm lỗi hãng) |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | Bộ nền: `0.0` (mốc before và after) · Thẻ S4: `0.185366` (mốc before/base) → `0.052174` (mốc after, sau khi bộ nền chạy cổng vòng 1 — số liệu còn lại do S4-08 thuộc kho DN, hiện ngoài `pilot_scope` nên vẫn tính vào tập "visible" nhưng không được agent tự xử lý) |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `__________`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] ______________________________
 └─ HOẶC
 ├─ [1] ______________ VÀ [gate ______ hỏng]
 ├─ [2] ______________ VÀ [gate ______ hỏng]
 └─ [3] ______________ (còn hở?)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | | | | |
| [2] | | | | |
| [3] | | | | |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| | | | |
| | | | |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

1. Nếu số ticket tăng gấp ___ lần trong một giờ thì: …
2. Nếu nhà cung cấp LLM lỗi quá ___ phút thì: …
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: …

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | phải giống v1 |
| Hash chốt cổng vòng 1 | phải giống v1 |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: ________ · prepared: ________ · after: ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: …
- Report tự kiểm tra: mã lần chạy `__________` · ô nào còn đỏ (nguyên nhân × tầng): …
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: …
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: …
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: …

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: …
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: …
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: …
