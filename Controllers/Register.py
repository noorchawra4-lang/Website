from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext
from Models.Models import User
from Schemas.Register_schemas import UserCreate

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def create_user(db: Session, data: UserCreate) -> User:
    old_user = db.query(User).filter(User.email == data.email).first()
    if old_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        full_name=data.full_name,
        email=data.email,
        phone=data.phone,
        hashed_password=hash_password(data.password),
        is_verified=True,  
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
