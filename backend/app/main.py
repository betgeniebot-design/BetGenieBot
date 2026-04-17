from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import CommandHandler
from app.bot import build_bot
from app.auth import router
import os

ptb_app = build_bot()

async def start(update: Update, context):
    keyboard = [[KeyboardButton("Open App", web_app=WebAppInfo(url=os.getenv("WEBAPP_URL")))]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Welcome! Click below to open the app.", reply_markup=reply_markup)

ptb_app.add_handler(CommandHandler("start", start))

@asynccontextmanager
async def lifespan(app: FastAPI):
    await ptb_app.initialize()
    await ptb_app.start()
    print("Bot is ready and running!")
    yield
    await ptb_app.stop()
    await ptb_app.shutdown()

app = FastAPI(lifespan=lifespan)
app.include_router(router)

@app.post("/webhook")
async def webhook(request: Request):
    req_json = await request.json()
    update = Update.de_json(req_json, ptb_app.bot)
    await ptb_app.process_update(update)
    return {"ok": True}