"""Các endpoint CRUD cho thực đơn căng tin trường."""
from typing import Annotated
from fastapi import APIRouter, Path, Query, status
from app.repository import MenuRepository
from app.schemas import ItemCreate, ItemOut, ItemPatch, ItemReplace

router = APIRouter(prefix="/menu", tags=["Menu"])
repo = MenuRepository()
MenuId = Annotated[int, Path(ge=1)]


@router.get("", response_model=list[ItemOut], summary="Xem và lọc thực đơn")
def list_items(
    q: str | None = Query(default=None, max_length=80),
    category: str | None = None,
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
):
    return repo.all(q, category, skip, limit)


@router.get("/{item_id}", response_model=ItemOut, summary="Chi tiết món")
def get_item(item_id: MenuId):
    return repo.get(item_id)


@router.post("", response_model=ItemOut, status_code=status.HTTP_201_CREATED, summary="Thêm món")
def create_item(payload: ItemCreate):
    return repo.create(payload)


@router.put("/{item_id}", response_model=ItemOut, summary="Thay toàn bộ thông tin món")
def replace_item(item_id: MenuId, payload: ItemReplace):
    return repo.replace(item_id, payload)


@router.patch("/{item_id}", response_model=ItemOut, summary="Cập nhật một phần")
def update_item(item_id: MenuId, payload: ItemPatch):
    return repo.patch(item_id, payload)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Xóa món")
def delete_item(item_id: MenuId):
    repo.delete(item_id)
    return None
