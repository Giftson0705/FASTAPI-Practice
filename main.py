from fastapi import FastAPI, Depends, HTTPException
from fastapi import FastAPI
# from pydantic import BaseModel,EmailStr,conint,constr,field_validators
from fastapi import Form, UploadFile, File

app = FastAPI()

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



# Example endpoint to demonstrate path parameters
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

#example endpoint to demonstrate query parameters
@app.get("/users/")
def road_user(userid:int, name:str=None):
    return {"user_id":user_id, "name": name}

#combing path and query parameters
@app.get("/users/{user_id/details}")
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
@app.post("/login")
def login(username: str, password: str):
    return authenticate(username, password)

@app.get("/user")
def get_user(user=Depends(authenticate)):
    return {"message": f"Hello {user['username']} with role {user['role']}"}

@app.get("/admin")
def get_admin(user=Depends(require_admin)):
    return {"message": f"Welcome admin {user['username']}"}
