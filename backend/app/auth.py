from fastapi import APIRouter
from db import users

router = APIRouter()

@router.post("/auth/telegram")
async def telegram_auth(user: dict):
    if not users.find_one({"telegram_id": user["id"]}):
            users.insert_one({
                "telegram_id": user["id"],
                "username": user.get("username"),
                "first_name": user.get("first_name")
            })
    return {"status": "ok"}