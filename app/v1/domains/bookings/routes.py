from fastapi import APIRouter
from ...core.database import engine


router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.get("/hello_world")
def hello_world_bookings():
    return {"msg": "Hello world"}

@router.get("/")
engine.ex