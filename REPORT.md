# GitHub Open Source Lab Report

> Thay nội dung  và đường dẫn thật sau khi hoàn
> thành thao tác GitHub.

## 1. Tôi đã đóng vai trò gì?

Tôi đóng vai trò Developer. Tôi đọc Issue, triển khai chức năng, viết test, cập
nhật tài liệu và xử lý feedback của reviewer.

## 2. Issue tôi xử lý là gì?

Issue #1: **Add temperature conversion**. Yêu cầu gồm đổi Celsius sang
Fahrenheit, Fahrenheit sang Celsius, viết unit test và cập nhật tài liệu.

## 3. Tôi đã tạo branch nào?

`feature/temperature-converter`.

## 4. Tôi đã tạo những commit nào?

- `feat: add temperature conversion (refs #1)`
- `test: add converter tests including negative values`
- `docs: document temperature converter usage`

Mã commit thật: `<commit hashes>`.

## 5. Pull Request của tôi là gì?

PR `<số PR>`: **feat: add temperature converter** — `<URL Pull Request>`.
PR sử dụng `Closes #1` để tự động đóng Issue sau khi merge.

## 6. Tôi đã review Pull Request nào?

Tôi review PR `<số PR của thành viên khác>` về `<tên chức năng>`. Tôi kiểm tra
code, test, tài liệu, phạm vi thay đổi và commit message.

## 7. Tôi đã nhận được feedback gì?

Reviewer yêu cầu bổ sung test cho nhiệt độ âm. Tôi đã thêm các trường hợp
`-40°C`, `-10°C`, `-40°F`, `14°F` và push commit mới lên cùng branch.

## 8. Tôi đã xử lý conflict như thế nào?

Tôi fetch `upstream`, merge `upstream/main` vào feature branch, mở `README.md`,
xóa conflict markers và giữ cả Temperature converter lẫn thay đổi hợp lệ của
nhánh còn lại. Sau đó tôi test, commit và push kết quả đã resolve.

## 9. Điều khó khăn nhất là gì?

Khó khăn nhất là bảo đảm branch vẫn đồng bộ với upstream khi nhiều người cùng
thay đổi README. Tôi fetch thường xuyên, đọc kỹ conflict và chạy lại test trước
khi push.

## 10. Nếu đây là dự án mã nguồn mở thật, tôi sẽ cải thiện quy trình như thế nào?

Tôi sẽ thêm CI bắt buộc chạy test cho mọi PR, Issue/PR template, bảo vệ branch
`main`, yêu cầu ít nhất một approval, tự động lint và dùng semantic versioning.
