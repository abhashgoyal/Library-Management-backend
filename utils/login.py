from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
from fastapi import HTTPException, status
from bson.json_util import dumps, loads
import json

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "your-secret-key"  # Same as in authentication.py
ALGORITHM = "HS256"

def login(client, user_data: dict):
    # Verify user exists in database
    db_user = client.find_one({"username": user_data["username"]})
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Verify password
    if not pwd_context.verify(user_data["password"], db_user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=30)
    # Convert MongoDB document to JSON serializable dict
    user_dict = json.loads(dumps(db_user))
    access_token = create_access_token(
        data={"user": user_dict}, expires_delta=access_token_expires
    )
    user_id = str(db_user["_id"])
    return {"user_id": user_id, "access_token": access_token, "token_type": "bearer"}

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
