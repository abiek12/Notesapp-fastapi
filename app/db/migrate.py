from app.db.connection import db

async def migrateDb():
    database = db.get_database()
    if "users" not in database.list_collection_names():
        database.create_collection(
            "users",
            validator={
                "$jsonSchema": {
                    "bsonType": "object",
                    "required": ["title", "content"],
                    "properties": {
                        "title": {"bsonType": "string"},
                        "content": {"bsonType": "string"}
                    }
                }
            }
        )
    if "urls" not in database.list_collection_names():
         database.create_collection(
            "urls",
            validator={
                "$jsonSchema": {
                    "bsonType": "object",
                    "required": ["title", "content"],
                    "properties": {
                        "title": {"bsonType": "string"},
                        "content": {"bsonType": "string"}
                    }
                }
            }
        )