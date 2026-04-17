# backend/app/bot.py
from telegram.ext import Application
import os

async def post_init(application: Application) -> None:
    print(f"Bot {application.bot.username} is ready!")

def build_bot() -> Application:
    application = (Application.builder().token(os.getenv("BOT_TOKEN")).updater(None).post_init(post_init).build())
    return application