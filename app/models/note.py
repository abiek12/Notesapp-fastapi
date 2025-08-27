from pydantic import BaseModel
from datetime import datetime

class Note(BaseModel):
    title: str
    desc: str
    important: bool = False
    created_at: str = str(datetime.timestamp(datetime.now()))
    updated_at: str = str(datetime.timestamp(datetime.now()))