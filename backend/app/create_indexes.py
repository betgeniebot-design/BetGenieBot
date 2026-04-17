from app.db import users

def create_indexes():
    try:
        users.create_index("telegram_id", unique=True)
        print("Index created successfully")
    except Exception as e:
        print(f"Index creation error: {e}")