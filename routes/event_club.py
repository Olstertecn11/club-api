from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import EventClub
from schemas import EventClubCreate, EventClubResponse

router = APIRouter()

# EventClub Routes


@router.post("/")
def create_event_club(event_club: EventClubCreate, db: Session = Depends(get_db)):
    new_event_club = EventClub(**event_club.dict())
    db.add(new_event_club)
    db.commit()
    db.refresh(new_event_club)
    return new_event_club


@router.get("/")
def get_event_clubs(db: Session = Depends(get_db)):
    return db.query(EventClub).all()
