from fastapi import FastAPI
# from pydantic import BaseModel,EmailStr,conint,constr,field_validators
from fastapi import Form, UploadFile, File 

app = FastAPI()

# class User(BaseModel):
#     name: str
#     age: int 
#     email:str

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

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

 

