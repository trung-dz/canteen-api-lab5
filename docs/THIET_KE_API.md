# PHẦN A – THIẾT KẾ API

## Dữ liệu món ăn

`id` (int, tự sinh), `code` (mã CTxxx, duy nhất), `name` (tên món), `category` (nhóm), `price` (VNĐ >0), `quantity` (số lượng >=0), `available` (boolean).

| HTTP | Đường dẫn | Ý nghĩa | Thành công |
|---|---|---|---|
| GET | `/health` | Kiểm tra server | 200 |
| GET | `/menu` | Danh sách, `q`, `category`, `skip`, `limit` | 200 |
| GET | `/menu/{item_id}` | Chi tiết | 200 |
| POST | `/menu` | Thêm món | 201 |
| PUT | `/menu/{item_id}` | Thay toàn bộ | 200 |
| PATCH | `/menu/{item_id}` | Sửa một phần | 200 |
| DELETE | `/menu/{item_id}` | Xóa món | 204 |

Mã lỗi chính: 404 (không có món), 409 (trùng `code`), 422 (đầu vào sai).

## Lưu ý phạm vi

Đây là **mẫu triển khai theo dàn ý của bản HTML được cung cấp**, không bảo đảm trùng 100% các thuộc tính/điều kiện trong tài liệu gốc vì file HTML không chứa nguyên văn nội dung các trang. Sử dụng repository in-memory để tập trung vào CRUD/Postman. Dự án này **không thay thế bài Chương 5 PostgreSQL + SQLAlchemy ORM** nếu môn học còn yêu cầu CSDL, khóa ngoại và migration.
