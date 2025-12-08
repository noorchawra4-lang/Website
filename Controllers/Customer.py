from sqlalchemy.orm import Session
from fastapi import HTTPException

from Models.Models import Customer
from Schemas.Customer_schemas import CustomerCreate, CustomerUpdate


def add_customer(db: Session, data: CustomerCreate):
    chk = db.query(Customer).filter(Customer.email == data.email).first()
    if chk:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_customer = Customer(
        name=data.name,
        email=data.email,
        phone=data.phone
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer


def get_all_customers(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Customer).offset(skip).limit(limit).all()


def get_customer_by_id(db: Session, cid: int):
    return db.query(Customer).filter(Customer.id == cid).first()


def update_customer(db: Session, cid: int, data: CustomerUpdate):
    cus = get_customer_by_id(db, cid)
    if not cus:
        return None

    if data.name:
        cus.name = data.name
    if data.email:
        cus.email = data.email
    if data.phone:
        cus.phone = data.phone

    db.commit()
    db.refresh(cus)
    return cus


def delete_customer(db: Session, cid: int):
    cus = get_customer_by_id(db, cid)
    if not cus:
        return None

    db.delete(cus)
    db.commit()
    return cus
