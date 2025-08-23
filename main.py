from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/health")
def read_root():
    return {"Hello": "World"}

@app.get('/', response_class=HTMLResponse)
def get_all_notes(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
    