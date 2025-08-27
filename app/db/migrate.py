from app.db.connection import db

async def migrateDb():
    database = db.get_database()
    if "notes" not in database.list_collection_names():
        database.create_collection(
            "notes",
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