# Contributing to Student Tools

## Quy trình làm việc

1. Chọn hoặc nhận một Issue được giao.
2. Đồng bộ `main` với repository upstream.
3. Tạo branch mới từ `main`, không commit trực tiếp vào `main`.
4. Viết code, test và cập nhật tài liệu liên quan.
5. Chạy `python -m pytest -v`.
6. Tạo các commit nhỏ, rõ nghĩa.
7. Push branch và mở Pull Request có `Closes #<issue-number>`.
8. Nhờ ít nhất một thành viên review và xử lý đầy đủ feedback.

## Tên branch

- `feature/<ten-chuc-nang>` cho chức năng mới.
- `fix/<ten-loi>` cho sửa lỗi.
- `docs/<noi-dung>` cho tài liệu.
- `test/<noi-dung>` cho test.

Ví dụ: `feature/temperature-converter`, `fix/division-by-zero`.

## Commit message

Dùng dạng `<type>: <mô tả ngắn>`:

- `feat: add temperature converter`
- `fix: handle division by zero`
- `test: add negative temperature cases`
- `docs: add converter usage guide`

## Checklist trước khi tạo Pull Request

- [ ] Code dễ đọc, tên biến rõ ràng.
- [ ] Không có code hoặc file thừa.
- [ ] Có test cho chức năng mới và trường hợp biên.
- [ ] Tất cả test đều pass.
- [ ] README/tài liệu đã được cập nhật.
- [ ] Commit message rõ ràng.
- [ ] Pull Request liên kết với Issue.
