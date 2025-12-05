
from typing import Optional
from pydantic import BaseModel


class ManufactureBase(BaseModel):
    name: str
    address: Optional[str] = None
    contact: Optional[str] = None


class ManufactureCreate(ManufactureBase):
    pass


class ManufactureUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    contact: Optional[str] = None
    


class ManufactureOut(ManufactureBase):
    id: int
    

    class Config:
        orm_mode = True
