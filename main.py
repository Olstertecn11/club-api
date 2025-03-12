from fastapi import FastAPI
from auth import router as auth_router
from routes.users import router as user_router
from routes.mision import router as mision_router
from routes.club import router as club_router
from routes.privilege import router as privilege_router
from routes.event import router as event_router
from routes.event_club import router as event_club_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(mision_router, prefix="/misions", tags=["Misions"])
app.include_router(club_router, prefix="/clubs", tags=["Clubs"])
app.include_router(privilege_router, prefix="/privileges", tags=["Privileges"])
app.include_router(event_router, prefix="/events", tags=["Events"])
app.include_router(event_club_router, prefix="/event-clubs", tags=["EventClubs"])


@app.get("/")
def home():
    return {"message": "FastAPI MySQL JWT Authentication"}
