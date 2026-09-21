# Student Tools

Một bộ công cụ Python nhỏ hỗ trợ sinh viên, được xây dựng cho bài thực hành
quản lý dự án và cộng tác trên GitHub.

## Features

- Calculator: cộng, trừ, nhân, chia và xử lý chia cho 0.
- Temperature converter: đổi Celsius sang Fahrenheit và ngược lại.
- Validator: kiểm tra email, mã sinh viên và chuỗi không rỗng.
- Unit tests cho các chức năng và trường hợp biên.

## Project structure

```text
student-tools/
├── src/
│   ├── calculator.py
│   ├── converter.py
│   └── validator.py
├── tests/
│   ├── test_calculator.py
│   ├── test_converter.py
│   └── test_validator.py
├── docs/
│   ├── github-workflow.md
│   └── usage.md
├── CONTRIBUTING.md
├── LICENSE
├── REPORT.md
└── requirements-dev.txt
```

## Requirements

- Python 3.10+
- pytest 8+

## Installation and testing

```bash
python -m venv .venv
```

Kích hoạt môi trường trên Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Cài công cụ test và chạy toàn bộ test:

```bash
python -m pip install -r requirements-dev.txt
python -m pytest -v
```

## Quick example

```python
from calculator import divide
from converter import celsius_to_fahrenheit
from validator import is_valid_email

print(divide(10, 2))                    # 5.0
print(celsius_to_fahrenheit(25))        # 77.0
print(is_valid_email("sv@example.com")) # True
```

Khi chạy ví dụ trực tiếp, thêm thư mục `src` vào `PYTHONPATH` hoặc chạy từ
môi trường đã cấu hình tương đương với pytest.

## Documentation

- Cách dùng chi tiết: [docs/usage.md](docs/usage.md)
- Quy trình Git/GitHub của bài lab: [docs/github-workflow.md](docs/github-workflow.md)
- Hướng dẫn đóng góp: [CONTRIBUTING.md](CONTRIBUTING.md)

## License

Dự án sử dụng giấy phép MIT. Xem [LICENSE](LICENSE).
