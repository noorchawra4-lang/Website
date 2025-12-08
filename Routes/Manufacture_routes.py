from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Database.database import get_db
from Controllers.Manufacture import *
from Schemas.Manufacture_schemas import ManufactureCreate, ManufactureUpdate, ManufactureOut
from Main.Main import get_user_by_token

router = APIRouter()

@router.post("/manufacture", response_model=ManufactureOut)
def add_manu(
    data: ManufactureCreate,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)):
    return add_manufacture(db, data)

@router.get("/manufacture", response_model=list[ManufactureOut])
def all_manu(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)):
    return get_all_manufactures(db, skip, limit)

@router.get("/manufacture/{mid}", response_model=ManufactureOut)
def one_manu(
    mid: int,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)):
    manu = get_manufacture_by_id(db, mid)
    if not manu:
        raise HTTPException(404, "Manufacture not found")
    return manu

@router.put("/manufacture/{mid}", response_model=ManufactureOut)
def upd_manu(
    mid: int,
    data: ManufactureUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)):
    manu = update_manufacture(db, mid, data)
    if not manu:
        raise HTTPException(404, "Manufacture not found")
    return manu

@router.delete("/manufacture/{mid}", response_model=ManufactureOut)
def del_manu(
    mid: int,
    db: Session = Depends(get_db),
    user=Depends(get_user_by_token)):
    manu = delete_manufacture(db, mid)
    if not manu:
        raise HTTPException(404, "Manufacture not found")
    return manu
