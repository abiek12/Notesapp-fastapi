from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/categories"
)

# Get all records
@router.get("/")
async def get_all_categories():
    categories = []
    return categories

# Get individual record by id
@router.get("/{id}")
async def get_category(id: str):
    category = []
    return category