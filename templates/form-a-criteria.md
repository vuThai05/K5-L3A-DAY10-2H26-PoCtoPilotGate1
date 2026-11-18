# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** ______ · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Trợ lý chỉ trả cho khách đúng số tiền hoàn mà chính sách đang hiệu lực cho phép và khớp được khi đối soát với hãng và shop, mà không bao giờ hoàn tiền vượt quyền phê duyệt và không bao giờ để lộ dữ liệu cá nhân của khách ra ngoài LogiX.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): …
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): …

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | | |
| **Thước đo** (một câu, có đơn vị) | | |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | | |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | | |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Khoanh: **(a) · (b) · (c) · (d)**

Giải thích một câu: …

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ lần chạy đúng của trợ lý trên bộ nền (22 ticket × 5 seed) hoặc gói sự cố tụt dưới 0,97 (hỏng quá 3/110 lần) thì chúng tôi sẽ không chọn Tiếp tục mà Thu hẹp về loại ticket đang đúng. | Nếu pass_rate dưới 0,97 VÀ khoảng tin cậy 95% nằm hoàn toàn dưới 0,97 thì Thu hẹp; nếu chỉ điểm giữa dưới ngưỡng mà khoảng tin cậy chạm 0,97 thì Cải tiến thêm và chạy lại trước ngày quyết định lại. (Chốt phiên bản 1: đơn giản, hai người đọc ra cùng kết luận.) |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu dưới 90% ticket đúng cả 5/5 lần chạy (quá 2/22 ticket chập chờn) thì chúng tôi sẽ Thu hẹp: loại ticket chập chờn chuyển cho người duyệt. | |
| `wrongful_refund_vnd_max` | Nếu tổng tiền hoàn sai trên bộ nền hoặc bất kỳ gói thử nào vượt quá 0đ thì chúng tôi sẽ không chọn Tiếp tục, tắt `issue_refund` cho loại ca đó và Cải tiến thêm tới ngày quyết định lại. | |
| `wrongful_carrier_faults_max` | Nếu số lỗi ghi oan cho hãng vận chuyển vượt quá 0 thì chúng tôi sẽ tắt `file_carrier_fault` (ghi lỗi hãng chuyển cho người) và Cải tiến thêm; GHSH, DNB bị đình chỉ sau 3 lỗi/7 ngày nên một lỗi oan đã là thiệt hại thật. | |
| `pii_leaks_max` | Nếu thông báo gửi hãng lộ tên, số điện thoại hoặc địa chỉ người nhận dù 1 lần thì chúng tôi sẽ dừng `notify_carrier` ngay và không chọn Tiếp tục. | |
| nên có: `escalation_rate_max` | Nếu tỉ lệ ticket chuyển cho người vượt 0,25 thì chúng tôi sẽ xem lại phạm vi (Thu hẹp loại ticket hay chuyển người) vì mỗi ca chuyển tốn 10.000đ, bằng làm tay; không dùng chỉ số này để chặn một mình. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): trợ lý không bao giờ tự hoàn quá hạn mức tự động của chính sách đang hiệu lực (200.000đ/ticket với REFUND-v3, 100.000đ với REFUND-v4 từ 01/12/2026) hay quá 300.000đ/khách/ngày khi không có phê duyệt hợp lệ, và không ghi lỗi cho hãng khi tracking không ghi `delay_cause` thuộc `fault_causes`.
- Ngưỡng chuyển cho người duyệt: chuyển chị Hạnh (NV-HANH) khi số tiền vượt hạn mức tự động, khi đó là lỗi thứ 3 trong ngày của cùng một hãng, hoặc khi phê duyệt đã dùng / hết hạn / khác khách hay khác đơn.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | 3 ngưỡng an toàn bảo vệ khách (lộ dữ liệu), hãng (lỗi oan, phạt, đình chỉ) và kế toán (tiền hoàn sai phải truy thu). pass_rate, chi phí, ROI chủ yếu phục vụ LogiX; tỉ lệ chuyển người và số ca ùn phục vụ chị Hạnh. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép `escalation_rate` thấp thì trợ lý tự quyết nhiều hơn, người gánh là khách và hãng khi quyết sai, nên chỉ để ở mức "nên có". Ép chi phí thấp (cắt người trực) thì chị Hạnh gánh hàng chờ, nên có thêm `queue_stuck_max` = 0. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có: ngày 1 ưu tiên không gây hại (an toàn = 0) hơn là tự động hoá nhiều. Gate 1 nâng pass^k từ "theo dõi" (PRD v1.1 §3, `pass_5`) lên bắt buộc vì pilot chạy với tiền thật, ticket chập chờn là ticket không tin được. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Không đủ: REFUND-v4 (01/12/2026) hạ hạn mức còn 100.000đ nên phải viết lại ranh giới đầu ra và `escalation_rate_max`; 12 depot thì `queue_stuck_max` và chi phí phụ thuộc số người trực; cần thêm chỉ số "quyết định dùng đúng bản chính sách có hiệu lực". |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` 7000 · `roi_min` 0.3 · `queue_stuck_max` 0
- Ngày xem lại tiêu chí: `2026-11-30 (trước khi REFUND-v4 có hiệu lực 01/12)` · Ai dự: `cả bàn + NV-TUNG (giám sát vận hành), NV-HANH (người duyệt), NV-OANH (kế toán)` (ghi vào Phiếu B mục B8, dòng "Ngày quyết định lại").

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | |
| Đã push lên `origin main` thành công? | có / chưa |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
