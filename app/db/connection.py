from app.core.config import config
from pymongo import MongoClient
import logging
import os
class Database:
    client = None
    db_url = f"mongodb+srv://{config.MONGO_USERNAME}:{config.MONGO_PASSWORD}@{config.MONGO_HOST}/?retryWrites=true&w=majority"
    print(db_url)
    logger = logging.getLogger(__name__)
    
    async def connect(self):
        if(not self.db_url):
            raise ValueError("MONGO_CONNECTION_STRING not set in environment variables.")
        self.client = MongoClient(self.db_url)
        self.logger.info("Database connected successfully!")
    
    async def disconnect(self):
        if self.client:
            self.client.close()
            self.logger.info("Database disconnected!")
            
    def get_database(self):
        if self.client:
            return self.client[os.getenv('MONGO_DB', 'my_notes_app_fastapi')]
        raise Exception("Database client not connected.")
    
db = Database()
