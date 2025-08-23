from app.core.config import config
from pymongo import MongoClient

client = MongoClient(
    f"mongodb://{config.MONGO_USERNAME}:{config.MONGO_PASSWORD}@{config.MONGO_HOST}:{config.MONGO_PORT}/"
)

db = client[config.MONGO_DB]