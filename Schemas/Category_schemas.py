
from typing import Optional
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    


class CategoryOut(CategoryBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
