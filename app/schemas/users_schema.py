def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": str(item["name"]),
        "email": str(item["email"]),
        "gender": str(item["gender"]),
        "roles": list(item["roles"]),
        "created_at": str(item["created_at"]),
        "updated_at": str(item["updated_at"])
    }

def usersEntity(items) -> list:
    return [userEntity(user) for user in items]