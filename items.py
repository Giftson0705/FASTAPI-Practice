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

app = FastAPI()


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