from fastapi import APIRouter
from ...services.urls import NotesService

router = APIRouter(
    prefix="/v1/notes"
)

# Get all records
@router.get("/")
async def get_all_notes():
    notes_svc = NotesService()
    res = notes_svc.get_all_notes()
    return res
   

# Get individual record by id
@router.get("/{id}")
async def get_note(id: str):
    note = []
    return note