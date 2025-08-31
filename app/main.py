from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes.v1.urls_route import router as url_router
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from app.db.connection import db
import logging
from app.db.migrate import migrateDb

# Configure root logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

# life span
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # connect db
    await db.connect()
    await migrateDb()
    
    yield
    
    # Disconnect db
    await db.disconnect()

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="./app/static"), name="static")
templates = Jinja2Templates(directory="./app/templates")

# Health check endpoint
@app.get("/health")
def read_root():
    return {"Hello": "World"}

# Routes
app.include_router(url_router, prefix="/api", tags=["urls"])