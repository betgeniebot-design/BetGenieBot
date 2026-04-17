import os
from pymongo import MongoClient
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    logger.error("MONGO_URI environment variable is not set")
    raise ValueError("MONGO_URI environment variable is not set")

logger.info(f"Attempting to connect to MongoDB (URI starts with: {MONGO_URI[:20]}...)")

# Force MongoDB connection with SSL disabled
try:
    client = MongoClient(
    MONGO_URI,
    tls=True,
    tlsAllowInvalidCertificates=True,  # Bypass SSL certificate validation
    tlsAllowInvalidHostnames=True,      # Bypass hostname validation
    serverSelectionTimeoutMS=10000      # 10 second timeout
    )
                                                            
    # Test the connection
    client.admin.command('ping')
    logger.info("✅ MongoDB connected successfully!")
                                                                            
except Exception as e:
    logger.error(f"❌ MongoDB connection failed: {e}")
    logger.warning("App will continue but database features won't work")
    # Still create the client - it will retry on each operation
    client = MongoClient(
        MONGO_URI,
        tls=True,
        tlsAllowInvalidCertificates=True,
        tlsAllowInvalidHostnames=True,
        serverSelectionTimeoutMS=10000
    )
# Creadb = client["BetgenieBot"]
users = db["users"]
logger.info("Database and collection objects created")