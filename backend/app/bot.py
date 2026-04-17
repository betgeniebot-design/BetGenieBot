from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import KeyboardButton, ReplyKeyboardMarkup, WebAppInfo, Update
import os

BOT_TOKEN= os.getenv("BOT_TOKEN")
WEBAPP_URL= os.getenv("WEBAPP_URL")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton(text="Open App", web_app=WebAppInfo(url=WEBAPP_URL))]]
    await update.message.reply_text("Welcome! click below to open the app.", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

def create_application() -> Application:
    app = Application.builder().token(BOT_TOKEN)).build()
    app.add_handler(CommandHandler("start", start))
    return app