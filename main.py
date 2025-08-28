from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os


# Load environment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False")

# Create app
app = FastAPI(title="Backend")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Middleware example
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"[LOG] {request.method} {request.url}")
    response = await call_next(request)
    return response
from fastapi import FastAPI, Depends, HTTPException
from fastapi import FastAPI
# from pydantic import BaseModel,EmailStr,conint,constr,field_validators
from fastapi import Form, UploadFile, File


@app.get("/")
def read_root():
    return {"message": "Hello, this is api methods"}


@app.get("/users/{user_id}")
def road_user(user_id: int):
   return {"user_id": user_id}

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
   return {"skip": skip, "limit": limit}   


@app.post("/items/")
def create_item(name: str, price: float):
    return {"item_name": name, "price": price}


@app.put("/items/{item_id}")
def update_item(item_id: int, name: str, price = float):
    return {"item_id": item_id, "name": name, "price": price}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):  
    return {"message": f"Item {item_id} deleted"}



#Routes
@app.get("/")
def root():
    return {
        "secret_key": SECRET_KEY,   
        "debug_mode": DEBUG_MODE
    }

