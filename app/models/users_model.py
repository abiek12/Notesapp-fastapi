from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from datetime import datetime

class Roles(str, Enum):
    admin = 'admin'
    user = 'user'
    
class Gender(str, Enum):
    male = 'male'
    female = 'female'
    other = 'other'

class Users(BaseModel):
    name: str
    email: str
    gender: Optional[str] = None
    password: str
    roles: List[Roles]
    created_at: str = str(datetime.timestamp(datetime.now()))
    updated_at: str = str(datetime.timestamp(datetime.now()))