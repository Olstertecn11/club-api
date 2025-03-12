from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Club
from schemas import ClubCreate

router = APIRouter()


@router.post("/")
def create_club(club: ClubCreate, db: Session = Depends(get_db)):
    new_club = Club(**club.dict())
    db.add(new_club)
    db.commit()
    db.refresh(new_club)
    return new_club


@router.get("/")
def get_clubs(db: Session = Depends(get_db)):
    return db.query(Club).all()
