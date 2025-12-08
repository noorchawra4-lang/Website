from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Database.database import get_db
from Controllers.Customer import add_customer,get_all_customers, get_customer_by_id,update_customer,delete_customer
from Schemas.Customer_schemas import CustomerCreate, CustomerUpdate, CustomerOut
from Main.Main import get_user_by_token   # token check

router = APIRouter()


@router.post("/customer", response_model=CustomerOut)
def create_customer_route(
    data: CustomerCreate,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    return add_customer(db, data)


@router.get("/customer", response_model=list[CustomerOut])
def list_customers(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    return get_all_customers(db, skip, limit)


@router.get("/customer/{cid}", response_model=CustomerOut)
def one_customer(
    cid: int,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    cus = get_customer_by_id(db, cid)
    if not cus:
        raise HTTPException(404, "Customer not found")
    return cus


@router.put("/customer/{cid}", response_model=CustomerOut)
def update_customer_route(
    cid: int,
    data: CustomerUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    cus = update_customer(db, cid, data)
    if not cus:
        raise HTTPException(404, "Customer not found")
    return cus


@router.delete("/customer/{cid}", response_model=CustomerOut)
def delete_customer_route(
    cid: int,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    cus = delete_customer(db, cid)
    if not cus:
        raise HTTPException(404, "Customer not found")
    return cus
