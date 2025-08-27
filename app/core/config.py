import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # MongoDB configuration
    MONGO_USERNAME = os.environ.get("MONGO_USERNAME", "your_username")
    MONGO_PASSWORD = os.environ.get("MONGO_PASSWORD", "your_password")
    MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
    MONGO_PORT = os.environ.get("MONGO_PORT", 27017)
    MONGO_DB = os.environ.get("MONGO_DB", "my_notes_app_fastapi")

config = Config