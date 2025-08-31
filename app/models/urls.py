from pydantic import BaseModel
from datetime import datetime
from app.db.connection import db

class Urls(BaseModel):
    id: str
    shortend_url: str
    original_url: str
    userId: str
    created_at: str = str(datetime.timestamp(datetime.now()))
    updated_at: str = str(datetime.timestamp(datetime.now()))