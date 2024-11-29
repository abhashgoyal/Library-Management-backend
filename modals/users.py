from enum import Enum
from pydantic import BaseModel

class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"

class User(BaseModel):
    username: str
    password: str
    role: Role = Role.USER 
    email: str
