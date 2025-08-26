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