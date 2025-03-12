from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Privilege
from schemas import PrivilegeCreate

router = APIRouter()

# Privilege Routes


@router.post("/")
def create_privilege(privilege: PrivilegeCreate, db: Session = Depends(get_db)):
    new_privilege = Privilege(**privilege.dict())
    db.add(new_privilege)
    db.commit()
    db.refresh(new_privilege)
    return new_privilege


@router.get("/")
def get_privileges(db: Session = Depends(get_db)):
    return db.query(Privilege).all()
