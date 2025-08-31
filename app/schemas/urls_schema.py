def urlEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "shortend_url": str(item["shortend_url"]),
        "original_url": str(item["original_url"]),
        "user_id": str(item["user_id"]),
        "created_at": str(item["created_at"]),
        "updated_at": str(item["updated_at"])
    }
        
def urlsEntity(itmes) -> list:
    return [urlEntity(item) for item in itmes]