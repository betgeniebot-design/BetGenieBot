from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.db import users
import logging

router = APIRouter()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TelegramUser(BaseModel):
    id: int
    username: str = None
    first_name: str = None
    last_name: str = None
    photo_url: str = None
    auth_date: int = None
    hash: str = None

@router.post("/auth/telegram")
async def telegram_auth(user: TelegramUser):
    logger.info(f"Received user data: {user.dict()}")
    try:
        existing = users.find_one({"telegram_id": user.id})
        if not existing:
            users.insert_one({
                "telegram_id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "photo_url": user.photo_url
            })
            logger.info("User inserted successfully")
        else:
            logger.info("User already exists")
        return {"status": "ok", "user_id": user.id}
    except Exception as e:
        logger.error(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))