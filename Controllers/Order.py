from sqlalchemy.orm import Session
from Models.Models import Order
from Schemas.Order_schemas import OrderCreate, OrderUpdate

def create_order(db: Session, data: OrderCreate):
    total = data.quantity * data.price_per_unit
    new_order = Order(
        customer_id=data.customer_id,
        category_id=data.category_id,
        manufacture_id=data.manufacture_id,
        quantity=data.quantity,
        price_per_unit=data.price_per_unit,
        total_price=total
    )
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def get_all_orders(db: Session, skip: int = 0, limit: int = 10):
    orders = db.query(Order).offset(skip).limit(limit).all()
    return orders

def get_order_by_id(db: Session, order_id: int):
    order = db.query(Order).filter(Order.id == order_id).first()
    return order

def update_order(db: Session, order_id: int, data: OrderUpdate):
    order = get_order_by_id(db, order_id)
    if not order:
        return None
    if data.quantity is not None:
        order.quantity = data.quantity
    if data.price_per_unit is not None:
        order.price_per_unit = data.price_per_unit

    order.total_price = order.quantity * order.price_per_unit
    db.commit()
    db.refresh(order)
    return order

def delete_order(db: Session, order_id: int):
    order = get_order_by_id(db, order_id)
    if not order:
        return None
    
    db.delete(order)
    db.commit()
    return order
