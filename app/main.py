from fastapi import FastAPI
import uvicorn

from routers.users import router as user_router

from schemas import User
from models import UserModel

from database import Database


app = FastAPI(
    title="Notes"
)

app.include_router(user_router)


@app.post("/reg")
def register(user: User):
    Database.add_user(UserModel(id=user.id, name=user.name))  # type: ignore

    return {
        "status": 200,
        "user": user
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8080, reload=True)
