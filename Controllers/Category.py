from sqlalchemy.orm import Session
from Models.Models import Category
from Schemas.Category_schemas import CategoryCreate, CategoryUpdate

def add_category(db: Session, data: CategoryCreate) -> Category:
    new_cat = Category(
        name=data.name,
        description=data.description
    )
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat

def get_all_categories(db: Session, skip: int = 0, limit: int = 10):
    cats = db.query(Category).offset(skip).limit(limit).all()
    return cats

def get_category_by_id(db: Session, category_id: int):
    cat = db.query(Category).filter(Category.id == category_id).first()
    return cat

def update_category(db: Session, category_id: int, data: CategoryUpdate):
    cat = get_category_by_id(db, category_id)
    if not cat:
        return None
    if data.name is not None:
        cat.name = data.name
    if data.description is not None:
        cat.description = data.description
    if data.is_active is not None:
        cat.is_active = data.is_active

    db.commit()
    db.refresh(cat)
    return cat

def delete_category(db: Session, category_id: int):
    cat = get_category_by_id(db, category_id)
    if not cat:
        return None
    db.delete(cat)
    db.commit()
    return cat
