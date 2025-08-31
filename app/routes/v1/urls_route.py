from fastapi import APIRouter

router = APIRouter(
    prefix="/v1/urls"
)

# Shorten long urls
@router.post("")
async def shorten_url():
    return True


