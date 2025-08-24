from ..db.connection import db

class NotesService:
    async def get_all_notes(req):
        res = await db.notes.find()