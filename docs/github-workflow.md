# Git/GitHub Workflow for the Lab

Thay các giá trị trong dấu `<...>` bằng thông tin thật.

## 1. Maintainer tạo repository và đẩy mã nguồn

```bash
cd student-tools
git init -b main
git add .gitignore LICENSE CONTRIBUTING.md requirements-dev.txt pyproject.toml .github REPORT.md docs/github-workflow.md src/calculator.py src/validator.py tests/test_calculator.py tests/test_validator.py
git commit -m "chore: initialize student tools project"
git remote add origin <original-repository-url>
git push -u origin main
```

## 2. Tạo Issues trên GitHub

Tạo tối thiểu sáu Issue sau và gán cho các thành viên:

1. **Feature:** Add temperature conversion — thêm C→F, F→C, test và tài liệu.
2. **Feature:** Improve calculator input validation — từ chối dữ liệu không phải số.
3. **Feature:** Add student data validator — kiểm tra email và mã sinh viên.
4. **Bug:** Handle division by zero — trả về lỗi có ý nghĩa.
5. **Bug:** Reject boolean calculator input — vì `bool` là kiểu con của `int`.
6. **Documentation:** Add usage guide — viết ví dụ sử dụng mọi module.

Mỗi Issue nên có mô tả, expected result, acceptance criteria, assignee và label.

**Vì sao dùng Issue:** Công việc được lưu tập trung, có người phụ trách, trạng
thái, mức ưu tiên, lịch sử thảo luận và liên kết trực tiếp với commit/PR; thông
tin không bị trôi hoặc thất lạc như tin nhắn.

## 3. Developer fork, clone và thêm upstream

Fork repository trên GitHub, sau đó:

```bash
git clone <fork-url>
cd student-tools
git remote add upstream <original-repository-url>
git remote -v
```

`origin` là fork mà developer có quyền push. `upstream` là repository gốc dùng
để nhận cập nhật và thường developer không có quyền push trực tiếp.

## 4. Làm Issue #1 trên feature branch

Nếu dùng bộ file hoàn thiện này, thêm file theo từng nhóm để tạo ít nhất ba
commit có ý nghĩa:

```bash
git switch -c feature/temperature-converter
git add src/converter.py
git commit -m "feat: add temperature conversion (refs #1)"

git add tests/test_converter.py
git commit -m "test: add converter tests including negative values"

git add README.md docs/usage.md
git commit -m "docs: document temperature converter usage"

git push -u origin feature/temperature-converter
```

## 5. Nội dung Pull Request

**Title:** `feat: add temperature converter`

```markdown
## Related Issue
Closes #1

## Changes
- Added Celsius to Fahrenheit conversion
- Added Fahrenheit to Celsius conversion
- Added input validation and negative-temperature cases
- Added unit tests and usage documentation

## Testing
- Run `python -m pytest -v`
- All tests pass
```

## 6. Review và change request

Reviewer kiểm tra code dễ đọc, tên rõ ràng, không có file thừa, có test, test
pass, tài liệu đã cập nhật và PR liên kết Issue.

Nhận xét mẫu: “The conversion functions are clear and correct. Please add test
cases for negative temperatures before merging.”

Sau khi sửa theo yêu cầu:

```bash
git switch feature/temperature-converter
git add tests/test_converter.py
git commit -m "test: add negative temperature cases"
git push
```

## 7. Thực hành merge conflict

Hai thành viên tạo hai branch và cùng sửa mục `Features` của `README.md`. Sau
khi PR thứ nhất được merge, người làm PR thứ hai chạy:

```bash
git fetch upstream
git switch <branch-thu-hai>
git merge upstream/main
```

Sửa marker conflict để giữ cả hai nội dung cần thiết, rồi:

```bash
git add README.md
git commit -m "fix: resolve README feature conflict"
git push
```

## 8. Đồng bộ fork

```bash
git fetch upstream
git switch main
git merge upstream/main
git push origin main
```

## 9. Tag và Release

Sau khi các PR đã được merge vào repository chính:

```bash
git switch main
git pull origin main
git tag -a v1.0.0 -m "Student Tools v1.0.0"
git push origin v1.0.0
```

Release note:

```markdown
# Student Tools v1.0.0
## Features
- Calculator with input validation
- Temperature converter
- Student data validator
## Fixes
- Meaningful error for division by zero
- Boolean input is rejected by numeric operations
## Tests
- All tests passed
## Contributors
Thanks to all contributors.
```

Commit là một snapshot có lịch sử, tác giả và thay đổi cụ thể. Tag là tên cố
định trỏ đến một commit, thường dùng đánh dấu phiên bản. Release là bản phát
hành trên GitHub dựa trên tag, có release notes và có thể kèm file tải xuống.
