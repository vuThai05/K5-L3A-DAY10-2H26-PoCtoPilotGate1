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

- Vòng 2 (thẻ S4): chuẩn bị thẻ sự cố (PR #19), thêm monitor `fail_open_carrier_fault_rate` (câu 3.6) và viết nháp Phiếu C câu 3.0–3.4 (C1, C2, C4 HAZOP, C5, C6) cho cả bàn góp ý (PR #32) — sau 3 lượt review của Thái đã sửa: thống nhất mẫu số/mã lần chạy ở C0/C8, tách lại hai lỗi độc lập ở C2 (`S4-08`, `S4-26`), chuyển quan hệ HOẶC/VÀ đúng ở fault tree C6, sửa monitor khớp code thật (`t["events"]` bắt lỗi thẳng, không `.get` ngầm định).
- Phát hiện và báo thêm phát hiện thứ 4 (chênh trần hoàn 500k/300k), đóng góp phân tích kỹ thuật cho hướng sửa PM6 (đọc động `ops_limits()`, lấy min) mà Thái dùng khi code câu 3.5 (PR #33).
- Sửa lỗi tích hợp phát sinh trong lúc chuẩn bị: trùng commit "Sign acceptance criteria" (rebase, PR #31), lỗi CRLF/LF làm sai hash file khoá (`.gitattributes`, PR #31), khôi phục đúng checkpoint gốc `fa385c26`.
- Điền A4/A5 (Phiếu A, câu 1.6) còn nguyên mẫu dù tiêu chí đã ký từ PR #18; gom lại `submission/` và chạy `check_submission --collect` (PR #35) — còn thiếu đúng 1 mục `decision_v2`, cần cả bàn chốt.
- Tích các mục đã hoàn thành trên issue #2–#6 theo tiến độ thật (không tự tích phần người khác chưa làm).

### Bằng chứng

- Vòng 1: Commit `4b5ffe8` (team info), `ca5434f` (operations/legal + HAZOP + runbook), `2547b85` (fix câu 1.2), `4e6597b` (fix câu 1.4), `a868081`+`77a7cb2` (khung vote 1.5), `969c074` (ký lại tiêu chí). `config/acceptance_criteria.lock` → `signed_at: 2026-11-18T16:32:42`. PR #7, #11, #15, #16, #18.
- Vòng 2: PR #19 (chuẩn bị S4), #26 (PM3 đối chiếu hàng chờ), #30 (sửa hiểu nhầm "nhóm kho ?"), #31 (fix CRLF/LF + chốt checkpoint gốc), #32 (câu 3.6 + Phiếu C nháp, merge sau 3 lượt review), #35 (A4/A5 + gom submission).
- PR #34 (kiểm chứng PM4 độc lập, 14/14 ca `fail_open` thật trên ticket HN/HCM bị PM4 chặn đúng) — đã đóng vì trùng với câu 3.5 Thái làm song song ở PR #33, nội dung kiểm chứng vẫn được dùng làm bằng chứng chung.

### Exit ticket

**Điều học được:** Quan trọng nhất không nằm ở việc viết đúng một dòng cổng hay một con số ngưỡng, mà ở cách cả bàn phối hợp để mỗi quyết định đều có bằng chứng và có người chịu trách nhiệm. Từ việc chốt tiêu chí, chạy ba mốc base/prepared/after, tới lúc xử lý sự cố S4, cái khó nhất không phải kỹ thuật mà là tìm được người cùng làm, chia đúng phần việc và sắp xếp thời gian để các phần ráp lại được với nhau mà không chồng chéo hay bỏ sót.

**Điều còn chưa chắc:** Guard đã kiểm chứng được trong phạm vi pilot (HN/HCM), nhưng chưa rõ nó có còn đúng khi mở rộng sang kho khác hoặc khi tải thật khác xa dữ liệu mock — đây là rủi ro bàn ghi lại để kiểm tiếp trước khi quyết định mở rộng.

## VuQuangThai-2A202603545

### Phần việc phụ trách

Vai: Kỹ sư cổng. `lab10/guards.py`, `lab10/monitors.py`; Phiếu A câu 1.3; Phiếu B mục B1–B2, B7.1–B7.3; Phiếu C mục C2, C4, C8.

### Đóng góp cụ thể

- Viết offline metric câu 1.3 (Phiếu A mục A2) cho bước "chọn phiên bản chính sách hoàn tiền": phát hiện agent (`lab10/agent.py` dòng 132–135) chọn chính sách bằng cờ `index_active` thay vì so ngày hiệu lực `effective_from/effective_to` — thước đo thiết kế để bắt đúng lỗ hổng này khi REFUND-v4 có hiệu lực 01/12/2026.
- Merge các PR đầu của nhóm (#1, #7, #8) với quyền chủ repo.
- Câu 2.6: Viết ba cổng PM1/PM4/PM5 trong `lab10/guards.py`, đọc kết quả eval/trace, kiểm hồi quy và ghi B7.1 cùng B0 dòng 2. Code tính lại quyền lợi trước hoàn tiền, kiểm căn cứ ghi lỗi hãng và dựng payload gửi hãng từ dữ kiện được phép; không xử lý riêng theo mã ticket hay seed.

- Câu 2.1, 2.2: chạy mốc base, trace `T-002@55`, bảng soát lỗi (PR #20).
- Vòng 2 (thẻ S4): review PR #32 ba lượt, đối chiếu số liệu, mã lần chạy, fault tree và monitor. Làm câu 3.5 + C7, C9–C12 (PR #33): thêm cổng kiểm ngân sách Finance, chạy S4 và regression, điền fault tree, risk register và runbook. Sau khi cả bàn chọn v2 **Tiếp tục** trong HN/HCM, cập nhật Phiếu C nhất quán và ghi rõ `integrity` vẫn FAIL, cần Lab Coach xác nhận trước khi nộp.

### Bằng chứng

- Commit `aa73375`, `11732d0` (form-a: câu 1.3); PR #14.
- Merge commit `ef45fb7`, `fd67e51`, `c5f4b6c`.
- Câu 2.6: run `R-base-after-20261118-171926-3d00df` đạt 110/110 lượt, không có ca mới hỏng; `python -m unittest discover -s tests` đạt 13 tests; `python -m lab10.guards` tự kiểm ba cổng OK. Chi tiết ở Phiếu B mục B7.1.
- Câu 2.1/2.2: PR #20.
- Vòng 2: 4 review trên PR #32 (18–19/11); commit `694749e` "C12" (PR #33, merged vào `main` qua `c4e55a4`).

### Exit ticket

**Điều học được:** Cần đối chiếu guard với trace và report theo từng mốc, vì kết quả đạt trên phạm vi pilot không tự chứng minh các ticket ngoài phạm vi an toàn. Khi lập fault tree, cần phân biệt lớp chặn với monitor chỉ phát hiện sau khi ghi.

**Điều còn chưa chắc:** Grade vẫn FAIL integrity vì thiếu 28 file thẻ trong manifest; cần Lab Coach xác nhận nguồn file và chạy lại trước khi nộp. Tôi cũng muốn kiểm lại trần hoàn khi có các lệnh ghi đồng thời và đo tải người duyệt ngoài dữ liệu mock.

## NguyenThiThuyDung-2A202603552

### Phần việc phụ trách

Vai: Kỹ sư cổng. `lab10/guards.py`, `lab10/monitors.py`; Phiếu B mục B1–B2, B7.1–B7.3; Phiếu C mục C2, C4, C8.

### Đóng góp cụ thể

- Merge các PR tích hợp nội dung của cả bàn vào `main` (#11, #14, #15, #16, #18), giữ nhánh `main` luôn ở trạng thái chạy được.
- Câu 2.7 (2 bước tránh rò rỉ dữ liệu) và câu 2.8 (behavioral test, 2 ticket hiểm `O-1002`, `O-1001`) sau khi Thái code xong cổng `guards.py` ở câu 2.6 (PR #28).
- Vòng 2 (thẻ S4): trả lời đầy đủ 4 câu hỏi mở trên PR #32 (kiểm chứng PM4 — nhận phụ trách chạy behavioral test ticket HN/HCM; hướng sửa câu 3.5 — ưu tiên kiểm chứng guard cũ trước khi thêm logic mới; quyết định v2 — nghiêng Cải tiến thêm; trần hoàn — đề xuất đọc động `ops_limits()` lấy min, đúng hướng Thái dùng để code câu 3.5 sau đó).

### Bằng chứng

- Merge commit `00c3526`, `00d47c6`, `111be02`, `28014f8`, `c349ca7`.
- Câu 2.7/2.8: PR #28.
- Vòng 2: comment trên PR #32, 2026-11-18 18:20 (issuecomment-6987534329).

### Exit ticket

*(Dung tự viết: một điều học được trong buổi, một điều còn chưa chắc — không điền hộ.)*

## NguyenThiHongHanh-2A202603537

### Phần việc phụ trách

Vai: Sản phẩm và kinh doanh. `config/acceptance_criteria.json`, `config/operating_gates.json` mục `business`; Phiếu A, Phiếu B mục B3, B7.4; Phiếu C mục C12.

### Đóng góp cụ thể

- Viết câu 1.1 (mục tiêu cấp hệ thống, 2 lần sửa: bỏ số cụ thể, thêm vế an toàn tuyệt đối theo PRD v1.1 §3 — không bỏ qua phê duyệt, không lộ dữ liệu).
- Viết toàn bộ câu 1.6 (Bản tiêu chí): 5 ngưỡng bắt buộc, `business_ops` (chi phí 7.000đ/ticket, ROI 0,3), `stop_condition`, `decision_rule` 4 dòng; gắn số liệu thật từ `data/world.json` (hạn mức REFUND-v3/v4, trần 300.000đ/khách/ngày, lỗi thứ 3/ngày, GHSH/DNB đình chỉ sau 3 lỗi/7 ngày); tự phát hiện REFUND-v4 có hiệu lực 01/12/2026 nên đặt ngày xem lại tiêu chí 30/11/2026.

- Câu 2.3 (bản đồ dữ liệu + ví dụ drift, Phiếu B mục B3, PR #22).
- Câu 2.9: điền cổng `business` trong `config/operating_gates.json` (`daily_refund_cap_vnd` 500.000đ, `cost_budget_per_ticket_vnd` 1.500đ, `pilot_scope` HN/HCM, `roi_min` 0,3) (PR #27).

### Bằng chứng

- Commit `23ddc4b`, `b14d1f1` (câu 1.1); `f1e6d90` (câu 1.6, nội dung được gộp vào PR #18 và ký).
- PR #8, #13, #17, #22, #27.

- Vòng 2 (thẻ S4): câu 3.2 (specification, Phiếu C mục C5). Góp ý 2 lượt trên PR #32 (03:28 và 04:39, 19/11) — đồng ý merge phần phân tích 3.0–3.4/3.6, giữ issue mở cho câu 3.5. Trên PR #35: vote quyết định v2 là **Tiếp tục trong phạm vi HN/HCM**, không mở rộng `pilot_scope` sang DN/CT cho tới khi kiểm chứng riêng sau REFUND-v4; đề nghị nhóm báo trực tiếp Lab Coach về integrity FAIL trước khi nộp.

### Việc còn phải làm (chưa xong tới lúc viết file này)

- Câu hỏi 4 (trần hoàn ngày, issue #4) đã được Thái làm hộ ở PR #33 do thời gian còn ngắn (issue #4 chuyển assignee sang Thái, có ghi lý do). Chưa ký PIC ở C12 (chờ cả bàn chốt xong).

### Exit ticket

*(Hạnh tự viết: một điều học được trong buổi, một điều còn chưa chắc — không điền hộ.)*
