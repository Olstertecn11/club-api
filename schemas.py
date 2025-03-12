from pydantic import BaseModel
from typing import Optional
from datetime import date


class Token(BaseModel):
    access_token: str
    token_type: str

# Privilege Schema


class PrivilegeBase(BaseModel):
    name: str


class PrivilegeCreate(PrivilegeBase):
    pass


class PrivilegeResponse(PrivilegeBase):
    id_privilege: int

    class Config:
        orm_mode = True

# User Schema


class UserBase(BaseModel):
    username: str
    password: str
    name: str
    surname: str
    phone: str
    email: str
    photo: Optional[str] = None
    id_privilege: int


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    id_user: int

    class Config:
        orm_mode = True

# Mision Schema


class MisionBase(BaseModel):
    name: str


class MisionCreate(MisionBase):
    pass


class MisionResponse(MisionBase):
    id_mision: int

    class Config:
        orm_mode = True

# Club Schema


class ClubBase(BaseModel):
    name: Optional[str] = None
    logo: Optional[str] = None
    id_director: int
    id_mision: int


class ClubCreate(ClubBase):
    pass


class ClubResponse(ClubBase):
    id_club: int

    class Config:
        orm_mode = True

# Event Schema


class EventBase(BaseModel):
    name: str
    description: str
    event_date: date


class EventCreate(EventBase):
    pass


class EventResponse(EventBase):
    id_event: int

    class Config:
        orm_mode = True

# EventClub Schema


class EventClubBase(BaseModel):
    event_club_date: date
    qualification: float
    comment: str
    id_event: int
    id_club: int


class EventClubCreate(EventClubBase):
    pass


class EventClubResponse(EventClubBase):
    id_event_club: int

    class Config:
        orm_mode = True
