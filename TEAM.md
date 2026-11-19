# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): 2H26
- Lớp: L3A
- Repo của bàn: K5-L3A-DAY10-2H26-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8): S4

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Lưu Thanh Mỹ | 2A202603532 | Vận hành và pháp lý | ✅ |
|   2 | Vũ Quang Thái | 2A202603545 | Kỹ sư cổng | |
|   3 | Nguyễn Thị Thùy Dung | 2A202603552 | Kỹ sư cổng | |
|   4 | Nguyễn Thị Hồng Hạnh | 2A202603537 | Sản phẩm và kinh doanh | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## LuuThanhMy-2A202603532

### Phần việc phụ trách

Vai: Vận hành và pháp lý (kiêm trưởng nhóm). `config/operating_gates.json` mục `operations`, `legal`; Phiếu A câu 1.2/1.4; Phiếu B mục B4–B5, B7.5–B7.6; `acceptance_criteria.json` (ký); TEAM.md; điều phối PR/issue cho cả bàn.

### Đóng góp cụ thể

- Điền `config/operating_gates.json` mục `operations` (PIC `NV-TUNG`, approver `NV-HANH`, SLA 60') và `legal` (chặn PII, bắt buộc recorded cause); viết HAZOP trên tool `notify_carrier` và checklist 9 nhóm việc (cột PIC) ở Phiếu B mục B4–B5; viết runbook 3 phần + giờ cao điểm (B7.5–B7.6).
- Viết câu 1.2 (mục tiêu chị Oanh/chị Hạnh, bám PRD v1.1 §2 và §6) và câu 1.4 (telemetry production cho `file_carrier_fault`) ở Phiếu A.
- Soát và ký Bản tiêu chí câu 1.6 sau khi Hạnh viết nội dung; gộp thêm góp ý (`stop_condition` có `notify_carrier`, hạn 30/11/2026) rồi ký lại lần cuối.
- Mở khung vote câu 1.5 cho cả bàn, thêm trích dẫn nguồn (problem-set.md, lab10/eval.py).

### Bằng chứng

- Commit `4b5ffe8` (team info), `ca5434f` (operations/legal + HAZOP + runbook), `2547b85` (fix câu 1.2), `4e6597b` (fix câu 1.4), `a868081`+`77a7cb2` (khung vote 1.5), `969c074` (ký lại tiêu chí).
- `config/acceptance_criteria.lock` → `signed_at: 2026-11-18T16:32:42`.
- PR #7, #11, #15, #16, #18 (GitHub, repo của bàn).

### Exit ticket

*(Mỹ tự viết: một điều học được trong buổi, một điều còn chưa chắc — không điền hộ.)*

## VuQuangThai-2A202603545

### Phần việc phụ trách

Vai: Kỹ sư cổng. `lab10/guards.py`, `lab10/monitors.py`; Phiếu A câu 1.3; Phiếu B mục B1–B2, B7.1–B7.3; Phiếu C mục C2, C4, C8.

### Đóng góp cụ thể

- Viết offline metric câu 1.3 (Phiếu A mục A2) cho bước "chọn phiên bản chính sách hoàn tiền": phát hiện agent (`lab10/agent.py` dòng 132–135) chọn chính sách bằng cờ `index_active` thay vì so ngày hiệu lực `effective_from/effective_to` — thước đo thiết kế để bắt đúng lỗ hổng này khi REFUND-v4 có hiệu lực 01/12/2026.
- Merge các PR đầu của nhóm (#1, #7, #8) với quyền chủ repo.
- Câu 2.6: Viết ba cổng PM1/PM4/PM5 trong `lab10/guards.py`, đọc kết quả eval/trace, kiểm hồi quy và ghi B7.1 cùng B0 dòng 2. Code tính lại quyền lợi trước hoàn tiền, kiểm căn cứ ghi lỗi hãng và dựng payload gửi hãng từ dữ kiện được phép; không xử lý riêng theo mã ticket hay seed.

### Bằng chứng

- Commit `aa73375`, `11732d0` (form-a: câu 1.3); PR #14.
- Merge commit `ef45fb7`, `fd67e51`, `c5f4b6c`.
- Câu 2.6: run `R-base-after-20261118-171926-3d00df` đạt 110/110 lượt, không có ca mới hỏng; `python -m unittest discover -s tests` đạt 13 tests; `python -m lab10.guards` tự kiểm ba cổng OK. Chi tiết ở Phiếu B mục B7.1.

### Việc còn phải làm (chưa xong tới lúc viết file này)

- Đã có kết quả câu 2.1–2.2 ở Phiếu B B0–B2 và đã hoàn tất 2.6 ở B7.1. Chờ Dung hoàn tất B7.2–B7.3 và Hạnh hoàn tất B7.4 để cả bàn chốt vòng 1 với Mỹ; phần vòng 2 làm theo phân công sau khi nhận thẻ.

### Exit ticket

*(Thái tự viết: một điều học được trong buổi, một điều còn chưa chắc — không điền hộ.)*

## NguyenThiThuyDung-2A202603552

### Phần việc phụ trách

Vai: Kỹ sư cổng. `lab10/guards.py`, `lab10/monitors.py`; Phiếu B mục B1–B2, B7.1–B7.3; Phiếu C mục C2, C4, C8.

### Đóng góp cụ thể

- Merge các PR tích hợp nội dung của cả bàn vào `main` (#11, #14, #15, #16, #18), giữ nhánh `main` luôn ở trạng thái chạy được.

### Bằng chứng

- Merge commit `00c3526`, `00d47c6`, `111be02`, `28014f8`, `c349ca7`.

### Việc còn phải làm (chưa xong tới lúc viết file này)

- Câu 2.7 (2 bước tránh rò rỉ dữ liệu) và câu 2.8 (behavioral test, 2 ticket hiểm) — cần đợi Thái code xong cổng `guards.py` (câu 2.6) trước mới có gì để test.

### Exit ticket

- **Điều em học được:** Một chỉ số theo dõi chỉ báo hiệu hành vi cần kiểm tra, không tự kết luận đúng sai. Với `fail_open_carrier_fault_rate`, em phải đọc trace của từng ca sáng đèn: cả 6 ca ở mốc `after` của S4 đều ghi lỗi hãng đúng, dù chỉ số khác 0.
- **Điều em còn chưa chắc:** Khi thu hẹp `pilot_scope` làm số trial giảm từ 205 xuống 115, tỉ lệ sáng đèn giảm có phản ánh rủi ro thực sự giảm hay chỉ do thay đổi tập ticket? Em muốn kiểm thêm trên cùng phạm vi và trong giờ cao điểm trước khi dùng chỉ số này để quyết định mở rộng pilot.

## NguyenThiHongHanh-2A202603537

### Phần việc phụ trách

Vai: Sản phẩm và kinh doanh. `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`; Phiếu A, Phiếu B mục B3, B7.4; Phiếu C mục C12.

### Đóng góp cụ thể

- Viết câu 1.1 (mục tiêu cấp hệ thống, 2 lần sửa: bỏ số cụ thể, thêm vế an toàn tuyệt đối theo PRD v1.1 §3 — không bỏ qua phê duyệt, không lộ dữ liệu).
- Viết toàn bộ câu 1.6 (Bản tiêu chí): 5 ngưỡng bắt buộc, `business_ops` (chi phí 7.000đ/ticket, ROI 0,3), `stop_condition`, `decision_rule` 4 dòng; gắn số liệu thật từ `data/world.json` (hạn mức REFUND-v3/v4, trần 300.000đ/khách/ngày, lỗi thứ 3/ngày, GHSH/DNB đình chỉ sau 3 lỗi/7 ngày); tự phát hiện REFUND-v4 có hiệu lực 01/12/2026 nên đặt ngày xem lại tiêu chí 30/11/2026.

### Bằng chứng

- Commit `23ddc4b`, `b14d1f1` (câu 1.1); `f1e6d90` (câu 1.6, nội dung được gộp vào PR #18 và ký).
- PR #8, #13, #17.

### Việc còn phải làm (chưa xong tới lúc viết file này)

- Câu 2.3 (bản đồ dữ liệu, Phiếu B mục B3) và câu 2.9 (`operating_gates.json` mục `business` — hiện vẫn `null` hết, chưa điền).

### Exit ticket

- **Điều học được:** Ngưỡng kinh doanh phải soát lại theo bối cảnh thật, không chỉ "đạt là xong". Trần hoàn 500.000đ mình đặt ở vòng 1 vẫn cho kết quả đạt trên thẻ S4, nhưng chỉ do may (292.000đ), vì ngày sale 11.11 Finance chốt riêng 300.000đ. Thêm nữa, khi LLM lỗi thì hệ thống phải rơi về trạng thái an toàn là chuyển cho người duyệt, không được tự ghi tiền hay ghi lỗi hãng (spec câu 3.2).
- **Điều còn chưa chắc:** Phạm vi pilot HN/HCM đang thật sự an toàn hay chỉ né được lỗi nhờ phạm vi hẹp. Ca hỏng S4-08 nằm ở kho DN, ngoài phạm vi, nên mình chưa chắc khi mở rộng sang DN/CT (sau REFUND-v4) thì các cổng hiện tại còn đủ không.
