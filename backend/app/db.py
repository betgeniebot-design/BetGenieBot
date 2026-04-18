import os
import logging
from pymongo import MongoClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

MONGO_URI = os.getenv("MONGO_URI")

if not MONGO_URI:
    logger.error("MONGO_URI environment variable is not set")
    raise ValueError("MONGO_URI environment variable is not set")

# FORCE remove SSL from URI
MONGO_URI = MONGO_URI.replace('ssl=true', 'ssl=false')
MONGO_URI = MONGO_URI.replace('tls=true', 'tls=false')
MONGO_URI = MONGO_URI.replace('mongodb+srv://', 'mongodb://')

# Add directConnection to avoid replica set issues
if 'directConnection=true' not in MONGO_URI:
    if '?' in MONGO_URI:
        MONGO_URI += '&directConnection=true'
    else:
        MONGO_URI += '?directConnection=true'

logger.info(f"Connecting with SSL disabled (URI masked: {MONGO_URI[:60]}...)")

# Connect WITHOUT any SSL parameters
try:
    client = MongoClient(
        MONGO_URI,
        ssl=False,  # CRITICAL: Disable SSL
        tls=False,  # CRITICAL: Disable TLS
        serverSelectionTimeoutMS=5000,
        connectTimeoutMS=5000
    )
    
    # Force a connection test
    client.admin.command('ping')
    logger.info("✅ MongoDB connected successfully!")
    
    db = client["BetgenieBot"]
    users = db["users"]
    logger.info("✅ Database and collection ready")
    
except Exception as e:
    logger.error(f"❌ MongoDB connection failed: {e}")
    logger.error("Please check your MONGO_URI environment variable")
    raise