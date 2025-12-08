from sqlalchemy.orm import Session
from Models.Models import Order
from Schemas.Order_schemas import OrderCreate, OrderOut

def create_order(db: Session, data: OrderCreate):
    total_price = data.quantity * data.price_per_unit

    new_order = Order(
        customer_id=data.customer_id,
        category_id=data.category_id,
        manufacture_id=data.manufacture_id,
        quantity=data.quantity,
        price_per_unit=data.price_per_unit,
        total_price=total_price)
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

def get_orders(db: Session, skip: int = 0, limit: int = 10):
    orders = db.query(Order).offset(skip).limit(limit).all()

    result = []
    for o in orders:
        item = OrderOut(
            id=o.id,
            total_price=o.total_price,
            status=o.status,
            created_at=o.created_at,
            customer_name=o.customer.full_name,
            category_name=o.category.name,
            manufacture_name=o.manufacture.name,
        )
        result.append(item)

    return result
