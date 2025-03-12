
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Event
from schemas import EventCreate, EventResponse

router = APIRouter()

# Privilege Routes


# Event Routes
@router.post("/")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = Event(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


@router.get("/")
def get_events(db: Session = Depends(get_db)):
    return db.query(Event).all()
