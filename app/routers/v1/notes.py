from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/notes"
)

# Get all records
@router.get("/")
async def get_all_notes():
    notes = []
    return notes

# Get individual record by id
@router.get("/{id}")
async def get_note(id: str):
    note = []
    return note