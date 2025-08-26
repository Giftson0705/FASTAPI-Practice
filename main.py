from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

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
