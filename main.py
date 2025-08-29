# from fastapi import FastAPI, Request
# from fastapi.middleware.cors import CORSMiddleware
# from dotenv import load_dotenv
# import os
# from fastapi import FastAPI, Depends, HTTPException
# from fastapi import FastAPI
# # from pydantic import BaseModel,EmailStr,conint,constr,field_validators
# from fastapi import Form, UploadFile, File

# app = FastAPI()

# # Create app
# app = FastAPI(title="Backend")

# # CORS setup
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# # Middleware example
# @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     print(f"[LOG] {request.method} {request.url}")
#     response = await call_next(request)
#     return response


# # Load environment variables
# load_dotenv()
# SECRET_KEY = os.getenv("SECRET_KEY", "defa@app.get("/")
# def root():
#     return {
#         "secret_key": SECRET_KEY,   
#         "debug_mode": DEBUG_MODE
#     }ult_secret")
# DEBUG_MODE = os.getenv("DEBUG_MODE", "False")



# @app.get("/")
# def read_root():
#     return {"message": "Hello, this is api methods"}



# # Fake in-memory "users"
# users = {
#     "sam": {"password": "1234", "role": "admin"},
#     "alex": {"password": "5678", "role": "user"},
# }

# # --- AUTH + AUTHZ ---
# def authenticate(username: str, password: str):
#     user = users.get(username)
#     if not user or user["password"] != password:
#         raise HTTPException(status_code=401, detail="Invalid credentials")
#     return {"username": username, "role": user["role"]}

# def require_admin(user=Depends(authenticate)):
#     if user["role"] != "admin":
#         raise HTTPException(status_code=403, detail="Admins only")
#     return user

# # --- ROUTES ---
# @app.post("/login")
# def login(username: str, password: str):
#     return authenticate(username, password)

# @app.get("/user")
# def get_user(user=Depends(authenticate)):
#     return {"message": f"Hello {user['username']} with role {user['role']}"}

# @app.get("/admin")
# def get_admin(user=Depends(require_admin)):
#     return {"message": f"Welcome admin {user['username']}"}


from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import crud

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

# Load environment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False")

@app.get("/")
def read_root():
    return {
        "message": "Hello, this is api methods",
        # "secret_key": SECRET_KEY,
        # "debug_mode": DEBUG_MODE
    }

# --- AUTH SETUP ---
users = {
    "sam": {"password": "1234", "role": "admin"},
    "alex": {"password": "5678", "role": "user"},
}

def authenticate(username: str, password: str):
    user = users.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"username": username, "role": user["role"]}

def require_admin(user=Depends(authenticate)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admins only")
    return user

@app.post("/login")
def login(username: str, password: str):
    return authenticate(username, password)

@app.get("/user")
def get_user(user=Depends(authenticate)):
    return {"message": f"Hello {user['username']} with role {user['role']}"}

@app.get("/admin")
def get_admin(user=Depends(require_admin)):
    return {"message": f"Welcome admin {user['username']}"}

# --- INCLUDE CRUD ROUTES ---
app.include_router(crud.router)
