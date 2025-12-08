from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database.database import get_db
from Controllers.Order import *
from Schemas.Order_schemas import OrderCreate, OrderOut
from Main.Main import get_user_by_token

router = APIRouter()

@router.post("/order", response_model=OrderOut)
def create_new_order(
    data: OrderCreate,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)):
    order = create_order(db, data)
    if not order:
        raise HTTPException(400, detail="Invalid IDs")
    return order

@router.get("/order", response_model=list[OrderOut])
def all_orders(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)):
    return get_orders(db, skip, limit)
