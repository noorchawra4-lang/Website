from sqlalchemy.orm import Session
from fastapi import HTTPException
from jose import jwt 
from passlib.context import CryptContext
from Models.Models import User
from Schemas.Login_schemas import LoginRequest

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
SECRET_KEY = "mysecret"
ALGO = "HS256"

def login_user(db: Session, data: LoginRequest):
    user = db.query(User).filter(User.email == data.email).first()
    if not user:
        raise HTTPException(400, "Email or password wrong")
    if not pwd_context.verify(data.password, user.hashed_password):
        raise HTTPException(400, "Email or password wrong")
    token = jwt.encode({"sub": str(user.id)}, SECRET_KEY, algorithm=ALGO)

    return token
