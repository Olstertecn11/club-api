from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Mision
from schemas import MisionCreate

router = APIRouter()


@router.post("/")
def create_mision(mision: MisionCreate, db: Session = Depends(get_db)):
    new_mision = Mision(**mision.dict())
    db.add(new_mision)
    db.commit()
    db.refresh(new_mision)
    return new_mision


@router.get("/")
def get_misions(db: Session = Depends(get_db)):
    return db.query(Mision).all()
