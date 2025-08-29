from fastapi import FastAPI, Request, Depends, HTTPException, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from fastapi import FastAPI
from items import router as items_router
from users import router as users_router

app = FastAPI()

app.include_router(items_router)
app.include_router(users_router)

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

# Load env vars
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret")
DEBUG_MODE = os.getenv("DEBUG_MODE", "False")

@app.get("/")
def root():
    return {
        "message": "Welcome to the FastAPI application!"
        # "secret_key": SECRET_KEY,
        # "debug_mode": DEBUG_MODE
    }


