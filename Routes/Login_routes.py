from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Database.database import get_db
from Controllers.Login import login_user
from Schemas.Login_schemas import LoginRequest, Token

router = APIRouter()

@router.post("/login", response_model=Token)
def login_now(data: LoginRequest, db: Session = Depends(get_db)):
    token = login_user(db, data)
    return {
        "access_token": token,
        "token_type": "bearer"
    }
