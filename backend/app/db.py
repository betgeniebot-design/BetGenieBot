import os
from pymongo import MongoClient

# Get the full MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI")

# Create MongoDB client
client = MongoClient(MONGO_URI)

# Select the correct database (BetgenieBot) and collection (users)
db = client["BetgenieBot"]   # or client.BetgenieBot
users = db["users"]          # or db.users