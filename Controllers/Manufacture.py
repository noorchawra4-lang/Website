from sqlalchemy.orm import Session
from Models.Models import Manufacture
from Schemas.Manufacture_schemas import ManufactureCreate, ManufactureUpdate

def add_manufacture(db: Session, data: ManufactureCreate) -> Manufacture:
    mf = Manufacture(
        name=data.name,
        address=data.address,
        contact=data.contact )
    
    db.add(mf)
    db.commit()
    db.refresh(mf)
    return mf

def get_all_manufactures(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Manufacture).offset(skip).limit(limit).all()

def get_manufacture_by_id(db: Session, mid: int):
    return db.query(Manufacture).filter(Manufacture.id == mid).first()

def update_manufacture(db: Session, mid: int, data: ManufactureUpdate):
    mf = get_manufacture_by_id(db, mid)
    if not mf:
        return None
    if data.name is not None:
        mf.name = data.name
    if data.address is not None:
        mf.address = data.address
    if data.contact is not None:
        mf.contact = data.contact
    if data.is_active is not None:
        mf.is_active = data.is_active

    db.commit()
    db.refresh(mf)
    return mf

def delete_manufacture(db: Session, mid: int):
    mf = get_manufacture_by_id(db, mid)
    if not mf:
        return None
    db.delete(mf)
    db.commit()
    return mf
