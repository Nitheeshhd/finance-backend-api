from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.models.user_model import users_db

router = APIRouter()

@router.post("/users")
def create_user(user: UserCreate):
    users_db.append(user.dict())
    return {"message": "User created", "data": user}

@router.get("/users")
def get_users():
    return users_db