from fastapi import APIRouter


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/")
def hello_world_users():
    return {"msg": "Hello world"}
