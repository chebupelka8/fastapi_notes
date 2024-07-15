from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/{user_id}")
def get_user(user_id: int):
    return {
        "status": 404,
        "message": "Not found."
    }
