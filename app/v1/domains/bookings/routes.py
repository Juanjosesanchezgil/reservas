from fastapi import APIRouter


router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.get("/")
def hello_world_bookings():
    return {"msg": "Hello world"}
