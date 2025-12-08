from pydantic import BaseModel
from typing import Optional


class ManufactureCreate(BaseModel):
    name: str
    address: Optional[str] = None
    contact: Optional[str] = None


class ManufactureUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    contact: Optional[str] = None
    is_active: Optional[bool] = None


class ManufactureOut(BaseModel):
    id: int
    name: str
    address: Optional[str]
    contact: Optional[str]
    is_active: bool

    class Config:
        orm_mode = True
