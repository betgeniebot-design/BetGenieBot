import os
from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set")

client = MongoClient(MONGO_URI)
db = client["BetgenieBot"]
users = db["users"]

# Create an index on telegram_id for faster lookups
users.create_index("telegram_id", unique=True)