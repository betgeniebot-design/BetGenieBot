# backend/app/bot.py
from telegram.ext import Application
import os

async def post_init(application: Application) -> None:
    """A function to run after the Application is initialized."""
        # You can add any post-initialization logic here if needed
            print(f"Bot {application.bot.username} is ready!")

            def build_bot() -> Application:
                """Builds and returns the PTB Application."""
                    # Build the Application without an Updater for webhook mode
                        application = (
                                Application.builder()
                                        .token(os.getenv("BOT_TOKEN"))
                                                # 'updater=None' is crucial for webhook mode
                                                        .updater(None)
                                                                .post_init(post_init)
                                                                        .build()
                                                                            )
                                                                                return application