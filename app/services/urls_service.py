from app.db.connection import db

class UrlsService:
    def __init__(self) -> None:
        database = db.get_database()
        self.urls = database['urls']