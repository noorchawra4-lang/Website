from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from Database.database import get_db
from Controllers.Category import add_category,get_all_categories,get_category_by_id,delete_category,update_category
from Schemas.Category_schemas import CategoryCreate, CategoryUpdate, CategoryOut
from Main.Main import get_user_by_token  \

router = APIRouter()

@router.post("/category", response_model=CategoryOut)
def add_cat(
    data: CategoryCreate,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    return add_category(db, data)

@router.get("/category", response_model=list[CategoryOut])
def all_cat(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    return get_all_categories(db, skip, limit)

@router.get("/category/{cid}", response_model=CategoryOut)
def one_cat(
    cid: int,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    cat = get_category_by_id(db, cid)
    if not cat:
        raise HTTPException(404, "Category not found")
    return cat

@router.put("/category/{cid}", response_model=CategoryOut)
def upd_cat(
    cid: int,
    data: CategoryUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    cat = update_category(db, cid, data)
    if not cat:
        raise HTTPException(404, "Category not found")
    return cat

@router.delete("/category/{cid}", response_model=CategoryOut)
def del_cat(
    cid: int,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)
):
    cat = delete_category(db, cid)
    if not cat:
        raise HTTPException(404, "Category not found")
    return cat
