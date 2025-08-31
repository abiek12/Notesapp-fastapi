def noteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "title": str(item["title"]),
        "desc": str(item["desc"]),
        "important": str(item["important"]),
        "created_at": str(item["created_at"]),
        "updated_at": str(item["updated_at"])
    }
        
def notesEntity(itmes) -> list:
    return [noteEntity(item) for item in itmes]