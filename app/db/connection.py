from app.core.config import config
from pymongo import MongoClient

class Database:
    client = None
    db_url = f"mongodb://{config.MONGO_USERNAME}:{config.MONGO_PASSWORD}@{config.MONGO_HOST}:{config.MONGO_PORT}/"
    
    def connect(self):
        if(not self.db_url):
            raise ValueError("MONGO_CONNECTION_STRING not set in environment variables.")
        self.client = MongoClient(self.db_url)
        print("Database connected successfully!")
    
    def disconnect(self):
        if self.client:
            self.client.close()
            print("Database disconnected!")
            
    def get_database(self, db_name: str):
        if self.client:
            return self.client[db_name]
        raise Exception("Database client not connected.")