from pydantic import BaseModel


class OrderCreate(BaseModel):
    customer_id: int
    category_id: int
    manufacture_id: int
    quantity: int
    price_per_unit: float


class OrderUpdate(BaseModel):
    quantity: int = None
    price_per_unit: float = None


class OrderOut(BaseModel):
    id: int
    customer_id: int
    category_id: int
    manufacture_id: int
    quantity: int
    price_per_unit: float
    total_price: float

    class Config:
        orm_mode = True
