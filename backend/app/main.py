from fastapi import FastAPI, Request
from app.bot import create_application
from telegram import Update
from app.auth import router

app= FastAPI()
telegram_app= create_application()
app.include_router(router)

@app.on_event("startup")
async def startup():
    await telegram_app.initialize()

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data= await request.json()
    update= Update.de_json(data, telegram_app.bot)
    await telegram_bot.process_update(update)
    return {"ok": True}