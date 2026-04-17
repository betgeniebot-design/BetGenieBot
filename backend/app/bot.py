from telegram.ext import Application, CommandHandler
from telegram import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
import os

async def start(update, context):
    keyboard = [[KeyboardButton("Open App", web_app=WebAppInfo(url=os.getenv("WEBAPP_URL")))]]
    await update.message.reply_text("Welcome!", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

def build_bot():
    app = Application.builder().token(os.getenv("BOT_TOKEN")).build()
    app.add_handler(CommandHandler("start", start))
    return app