from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi import FastAPI
# from pydantic import BaseModel,EmailStr,conint,constr,field_validators
from fastapi import Form, UploadFile, File
from fastapi import APIRouter

router = APIRouter()


@router.get("/users/{user_id}")
def road_user(user_id: int):
   return {"user_id": user_id}



# Example endpoint to demonstrate path parameters
@router.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

#example endpoint to demonstrate query parameters
@router.get("/users/")
def road_user(userid:int, name:str=None):
    return {"user_id":user_id, "name": name}

#combing path and query parameters
@router.get("/users/{user_id/details}")
def read_user_details(user_id: int, include_email: bool = False):
    if include_email:
        return{"user_id": user_id, "include email":"email included"}
    else:
        return {"user_id": user_id, "include_email": "email not included"} 






# Fake in-memory "users"
users = {
    "sam": {"password": "1234", "role": "admin"},
    "alex": {"password": "5678", "role": "user"},
}

# --- AUTH + AUTHZ ---
def authenticate(username: str, password: str):
    user = users.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"username": username, "role": user["role"]}

def require_admin(user=Depends(authenticate)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return user

# --- ROUTES ---
@router.post("/login")
def login(username: str, password: str):
    return authenticate(username, password)

@router.get("/user")
def get_user(user=Depends(authenticate)):
    return {"message": f"Hello {user['username']} with role {user['role']}"}

@router.get("/admin")
def get_admin(user=Depends(require_admin)):
    return {"message": f"Welcome admin {user['username']}"}