from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pymongo import MongoClient
from utils.jwt_handler import decode_access_token
from modals.users import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(
    token: str = Depends(oauth2_scheme), 
    client: MongoClient = Depends()
) -> User:
    try:
        token_data = decode_access_token(token)
        user_data = client.find_one({"username": token_data["username"]})
        if not user_data:
            raise HTTPException(status_code=401, detail="User not found")
        
        return User(
            username=user_data["username"],
            email=user_data["email"],
            role=token_data["role"],
            password=user_data["password"]
        )
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
