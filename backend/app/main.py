from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import CommandHandler
from app.bot import build_bot
from app.auth import router

# Build the PTB application
ptb_app = build_bot()

# --- Handler for /start command ---
async def start(update: Update, context):
    """Send a welcome message when the /start command is issued."""
        await update.message.reply_text("Welcome! The bot is working and ready.")
        # Add the handler to the application
        ptb_app.add_handler(CommandHandler("start", start))

        # --- Lifespan manager for startup/shutdown ---
        @asynccontextmanager
        async def lifespan(app: FastAPI):
            # Startup
                await ptb_app.initialize()
                    await ptb_app.start()
                        print("Bot is ready and running!")
                            yield
                                # Shutdown
                                    await ptb_app.stop()
                                        await ptb_app.shutdown()

                                        # Create FastAPI app with lifespan
                                        app = FastAPI(lifespan=lifespan)

                                        # Include authentication routes
                                        app.include_router(router)

                                        # --- Webhook endpoint ---
                                        @app.post("/webhook")
                                        async def webhook(request: Request):
                                            """Handle incoming Telegram updates."""
                                                req_json = await request.json()
                                                    update = Update.de_json(req_json, ptb_app.bot)
                                                        await ptb_app.process_update(update)
                                                            return {"ok": True}