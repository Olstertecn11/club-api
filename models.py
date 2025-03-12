from sqlalchemy import Column, Integer, String, ForeignKey, Date, Double, Text, CHAR
from sqlalchemy.orm import relationship
from database import Base


class Privilege(Base):
    __tablename__ = "privilege"

    id_privilege = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    users = relationship("User", back_populates="privilege")


class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(200), nullable=False, unique=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(200), nullable=False)
    photo = Column(Text, nullable=True)
    id_privilege = Column(Integer, ForeignKey("privilege.id_privilege"), nullable=False)

    privilege = relationship("Privilege", back_populates="users")
    clubs = relationship("Club", back_populates="director")


class Mision(Base):
    __tablename__ = "mision"

    id_mision = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    clubs = relationship("Club", back_populates="mision")


class Club(Base):
    __tablename__ = "club"

    id_club = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=True)
    logo = Column(Text, nullable=True)
    id_director = Column(Integer, ForeignKey("user.id_user"), nullable=False)
    id_mision = Column(Integer, ForeignKey("mision.id_mision"), nullable=False)

    director = relationship("User", back_populates="clubs")
    mision = relationship("Mision", back_populates="clubs")
    event_clubs = relationship("EventClub", back_populates="club")


class Event(Base):
    __tablename__ = "event"

    id_event = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    event_date = Column(Date, nullable=False)
    event_clubs = relationship("EventClub", back_populates="event")


class EventClub(Base):
    __tablename__ = "event_club"

    id_event_club = Column(Integer, primary_key=True, index=True, autoincrement=True)
    event_club_date = Column(Date, nullable=False)
    qualification = Column(Double, nullable=False)
    comment = Column(String(255), nullable=False)
    id_event = Column(Integer, ForeignKey("event.id_event"), nullable=False)
    id_club = Column(Integer, ForeignKey("club.id_club"), nullable=False)

    event = relationship("Event", back_populates="event_clubs")
    club = relationship("Club", back_populates="event_clubs")
