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


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

#Routes
@app.get("/")
def root():
    return {
        "secret_key": SECRET_KEY,   
        "debug_mode": DEBUG_MODE
    }

