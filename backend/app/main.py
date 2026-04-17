from fastapi import FastAPI, Request
from app.bot import build_bot
from app.auth import router

app= FastAPI()
bot= build_bot()
app.include_router(router)

@app.post("/webhook")
async def webhook(req: Request):
    await bot.process_update(await req.json())
    return {"ok": True}