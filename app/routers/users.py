from fastapi import APIRouter

from database import Database

from schemas import User


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/{user_id}")
def get_user(user_id: int):
    if (user := Database.get_user_by_id(user_id)) is not None:
        return {
            "status": 200,
            "user": User(id=user.id, name=user.name)
        }

    return {
        "status": 404,
        "message": "Not found."
    }
