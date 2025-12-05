
from datetime import datetime
from pydantic import BaseModel


class OrderBase(BaseModel):
    customer_id: int
    category_id: int
    manufacture_id: int
    quantity: int
    price_per_unit: float


class OrderCreate(OrderBase):
    pass


class OrderOut(BaseModel):
    id: int
    total_price: float
    status: str
    created_at: datetime

    customer_name: str
    category_name: str
    manufacture_name: str

    class Config:
        orm_mode = True
