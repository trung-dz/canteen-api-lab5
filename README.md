# LAB 5 – THỰC ĐƠN CĂNG TIN TRƯỜNG

Bản tham khảo thực hành FastAPI CRUD + Postman, theo bố cục B1–B5, C0–C10 của tài liệu HTML người học cung cấp. **Khác với dự án Chương 5 PostgreSQL/ORM**; mã nguồn hiện lưu dữ liệu in-memory và sẽ trở về 3 món mẫu khi khởi động lại server.

## 1. Chạy trên Ubuntu WSL

```bash
cd ~/LAB5_CangTin_FastAPI_Postman
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Mở http://127.0.0.1:8000/docs, GET /health và /menu.

## 2. Dự án

- `app/schemas.py`: Pydantic schema (kiểm tra giá và mã).
- `app/repository.py`: lưu in-memory, kiểm tra lỗi và CRUD.
- `app/routers/menu.py`: GET/POST/PUT/PATCH/DELETE.
- `app/main.py`: FastAPI, đăng ký router, `/health`.
- `postman/`: Collection gồm nhóm CRUD (12 requests) và nhóm CSV (1 request), Environment.
- `data/menu_filter.csv`: tập dữ liệu chạy CSV Runner.
- `tests/test_api.py`: kiểm thử pytest.

## 3. Postman

Import 2 file JSON trong `postman/`, chọn Environment **CangTin-Local** chứa `baseUrl=http://127.0.0.1:8000`.
Chạy **chỉ folder `CRUD - 12 test cases`** qua `Run` (Functional/Local, 1 iteration). Thứ tự các request đã sắp phù hợp để thêm/sửa/xóa món. Kết quả mong muốn tất cả assertion Passed, Errors 0.

Riêng phần CSV: chọn folder **CSV - Filter category**, `Run`, `Iteration data` chọn `data/menu_filter.csv` (3 rows). Không chạy cả Collection với 3 CSV iteration vì như vậy 12 CRUD test sẽ bị lặp không cần thiết.

## 4. Newman (cần Node.js/npm)

```bash
node --version
npm --version
npx --yes newman run postman/CangTin_Lab5.postman_collection.json -e postman/CangTin_Local.postman_environment.json --folder "CRUD - 12 test cases"
npx --yes newman run postman/CangTin_Lab5.postman_collection.json -e postman/CangTin_Local.postman_environment.json --folder "CSV - Filter category" -d data/menu_filter.csv
```

Nếu không có Node/npm: `sudo apt update && sudo apt install -y nodejs npm`.

## 5. Pytest

Mở terminal thứ hai trong WSL rồi chạy:

```bash
cd ~/LAB5_CangTin_FastAPI_Postman
source .venv/bin/activate
python -m pytest -v
```

## 6. Minh chứng

Chụp Swagger, phản hồi POST 201, GET 200, 404/409/422, PUT/PATCH, DELETE 204; Collection Runner Passed, CSV Runner Passed và Newman (nếu yêu cầu). Đặt ảnh vào `docs/` trước khi push Git.

## Lưu ý

Vì tệp đính kèm là trang HTML lưu từ Google Tài liệu, phần văn bản tài liệu gốc không được xuất kèm đầy đủ. Bản này là dự án thực hành tương ứng với **các tiêu đề** nhìn thấy được; không khẳng định các trường dữ liệu, endpoint, số test case là nguyên văn yêu cầu của giảng viên.
