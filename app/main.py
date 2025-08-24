from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from .routers.v1 import notes, categories
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from db.connection import Database

# life span
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # connect db
    db = Database()
    db.connect()
    
    yield
    
    # Disconnect db
    db.disconnect()

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="./app/static"), name="static")
templates = Jinja2Templates(directory="templates")

# Health check endpoint
@app.get("/health")
def read_root():
    return {"Hello": "World"}

# Routes
app.include_router(notes.router, prefix="/api", tags=["notes"])
app.include_router(categories.router, prefix="/api", tags=["categories"])