from app.db.connection import db
from ..schemas.urls import notesEntity

class NotesService:
    def __init__(self) -> None:
        database = db.get_database()
        self.notes = database['notes']
    
    async def get_all_notes(self,):
        notesData = self.notes.find()
        return notesEntity(list(notesData))