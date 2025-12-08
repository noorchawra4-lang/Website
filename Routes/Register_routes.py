from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Database.database import get_db
from Controllers.Register import create_user
from Schemas.Register_schemas import UserCreate, UserOut

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register_user(data: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, data)
