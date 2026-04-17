# backend/app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import CommandHandler
from app.bot import build_bot
from app.auth import router

# Global variable to hold the Application instance
ptb_app = build_bot()

# --- Define the /start command handler ---
async def start(update: Update, context):
    """Handler for the /start command."""
        await update.message.reply_text("Welcome! The bot is working and ready.")

        # Add the handler to the Application *before* it starts
        ptb_app.add_handler(CommandHandler("start", start))

        # --- Lifespan manager for proper startup/shutdown ---
        @asynccontextmanager
        async def lifespan(app: FastAPI):
            # Startup: Initialize and start the PTB Application
                await ptb_app.initialize()
                    await ptb_app.start()
                        print("Bot is ready and running!")
                            yield
                                # Shutdown: Stop the PTB Application gracefully
                                    await ptb_app.stop()
                                        await ptb_app.shutdown()

                                        # Pass the lifespan manager to the FastAPI app
                                        app = FastAPI(lifespan=lifespan)
                                        app.include_router(router)

                                        # --- Webhook endpoint ---
                                        @app.post("/webhook")
                                        async def webhook(request: Request):
                                            """Handle incoming Telegram updates."""
                                                # Get the JSON data from the request
                                                    req_json = await request.json()
                                                        # Create a Telegram Update object from the JSON
                                                            update = Update.de_json(req_json, ptb_app.bot)
                                                                # Process the update through the Application
                                                                    await ptb_app.process_update(update)
                                                                        return {"ok": True}