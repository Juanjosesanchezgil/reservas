from fastapi import FastAPI
from domains.users.routes import router as users
from domains.bookings.routes import router as bookings


app = FastAPI()


app.include_router(bookings)
app.include_router(users)


@app.get("/")
def hello_world():
    return {"msg": "Hello World"}
