"""Kiểu dữ liệu thực đơn căng tin và kiểm tra dữ liệu đầu vào."""
from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    code: str = Field(pattern=r"^CT[0-9]{3}$", examples=["CT001"])
    name: str = Field(min_length=2, max_length=120)
    category: str = Field(min_length=2, max_length=60)
    price: int = Field(gt=0, description="Giá bán (VNĐ), phải lớn hơn 0")
    quantity: int = Field(ge=0, default=0)
    available: bool = True


class ItemCreate(ItemBase):
    pass


class ItemReplace(ItemBase):
    pass


class ItemPatch(BaseModel):
    code: str | None = Field(default=None, pattern=r"^CT[0-9]{3}$")
    name: str | None = Field(default=None, min_length=2, max_length=120)
    category: str | None = Field(default=None, min_length=2, max_length=60)
    price: int | None = Field(default=None, gt=0)
    quantity: int | None = Field(default=None, ge=0)
    available: bool | None = None


class ItemOut(ItemBase):
    id: int
