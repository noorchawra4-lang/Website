from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from Database.database import get_db
from Schemas.Order_schemas import OrderCreate, OrderUpdate, OrderOut
from Controllers import Order as order_controller
from Main.Main import get_user_by_token    # token check

router = APIRouter()


@router.post("/order", response_model=OrderOut)
def create_order_route(
    order: OrderCreate,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    new_order = order_controller.create_order(db, order)
    return new_order


@router.get("/order", response_model=List[OrderOut])
def get_all_order_route(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    orders = order_controller.get_all_orders(db, skip, limit)
    return orders


@router.get("/order/{order_id}", response_model=OrderOut)
def get_one_order_route(
    order_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    order = order_controller.get_order_by_id(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@router.put("/order/{order_id}", response_model=OrderOut)
def update_order_route(
    order_id: int,
    order_data: OrderUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    updated_order = order_controller.update_order(db, order_id, order_data)
    if not updated_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return updated_order


@router.delete("/order/{order_id}", response_model=OrderOut)
def delete_order_route(
    order_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    deleted_order = order_controller.delete_order(db, order_id)
    if not deleted_order:
        raise HTTPException(status_code=404, detail="Order not found")
    return deleted_order
