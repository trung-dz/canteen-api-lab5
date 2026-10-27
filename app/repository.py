"""Tầng repository: dữ liệu in-memory, minh họa CRUD không cần CSDL."""
from fastapi import HTTPException, status
from app.schemas import ItemCreate, ItemPatch, ItemReplace

SEED = [
    {"id": 1, "code": "CT001", "name": "Cơm gà", "category": "Mon chinh", "price": 35000, "quantity": 20, "available": True},
    {"id": 2, "code": "CT002", "name": "Trà chanh", "category": "Do uong", "price": 12000, "quantity": 30, "available": True},
    {"id": 3, "code": "CT003", "name": "Bánh mì", "category": "An vat", "price": 18000, "quantity": 15, "available": True},
]


class MenuRepository:
    def __init__(self) -> None:
        self._items = {row["id"]: row.copy() for row in SEED}
        self._next_id = max(self._items) + 1

    def all(self, q: str | None, category: str | None, skip: int, limit: int):
        values = list(self._items.values())
        if q:
            values = [r for r in values if q.casefold() in r["name"].casefold()]
        if category:
            values = [r for r in values if category.casefold() == r["category"].casefold()]
        return values[skip:skip + limit]

    def get(self, item_id: int):
        row = self._items.get(item_id)
        if row is None:
            raise HTTPException(status_code=404, detail=f"Không tìm thấy món id={item_id}")
        return row

    def _check_code(self, code: str, excluded_id: int | None = None):
        if any(r["code"] == code and r["id"] != excluded_id for r in self._items.values()):
            raise HTTPException(status_code=409, detail=f"Mã món {code} đã tồn tại")

    def create(self, payload: ItemCreate):
        self._check_code(payload.code)
        item = {"id": self._next_id, **payload.model_dump()}
        self._items[self._next_id] = item
        self._next_id += 1
        return item

    def replace(self, item_id: int, payload: ItemReplace):
        self.get(item_id)
        self._check_code(payload.code, item_id)
        self._items[item_id] = {"id": item_id, **payload.model_dump()}
        return self._items[item_id]

    def patch(self, item_id: int, payload: ItemPatch):
        item = self.get(item_id)
        changes = payload.model_dump(exclude_unset=True)
        if any(v is None for v in changes.values()):
            raise HTTPException(status_code=422, detail="Không được cập nhật trường thành null")
        if "code" in changes:
            self._check_code(changes["code"], item_id)
        item.update(changes)
        return item

    def delete(self, item_id: int):
        self.get(item_id)
        del self._items[item_id]
