# Core module: security 
from fastapi import Depends, HTTPException, Header
from passlib.context import CryptContext
import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY", "REPLACE_WITH_SECRET")
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(Authorization: str = Header(...)):
    if not Authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")
    token = Authorization[len("Bearer "):]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return {"id": payload["sub"], "email": payload["email"]}
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")