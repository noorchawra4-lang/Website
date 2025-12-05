
from typing import Optional
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    phone: str


class UserCreate(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    is_verified: bool

    class Config:
        orm_mode = True


class OTPVerify(BaseModel):
    email: EmailStr
    otp: str
