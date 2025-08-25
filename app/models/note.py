from pydantic import BaseModel

class Note(BaseModel):
    title: str
    desc: str
    important: bool
    created_at: str
    updated_at: str