# @app.get("/users/{user_id}")
# def road_user(user_id: int):
#    return {"user_id": user_id}

# @app.get("/items/")
# def read_items(skip: int = 0, limit: int = 10):
#    return {"skip": skip, "limit": limit}   


# @app.post("/items/")
# def create_item(name: str, price: float):
#     return {"item_name": name, "price": price}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, name: str, price = float):
#     return {"item_id": item_id, "name": name, "price": price}

# @app.delete("/items/{item_id}")
# def delete_item(item_id: int):  
#     return {"message": f"Item {item_id} deleted"}




# # Example endpoint to demonstrate path parameters
# @app.get("/users/{user_id}")
# def read_user(user_id: int):
#     return {"user_id": user_id}

# #example endpoint to demonstrate query parameters
# @app.get("/users/")
# def road_user(userid:int, name:str=None):
#     return {"user_id":user_id, "name": name}

# #combing path and query parameters
# @app.get("/users/{user_id/details}")
# def read_user_details(user_id: int, include_email: bool = False):
#     if include_email:
#         return{"user_id": user_id, "include email":"email included"}
#     else:
#         return {"user_id": user_id, "include_email": "email not included"}



from fastapi import APIRouter

router = APIRouter()

@router.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

@router.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@router.post("/items/")
def create_item(name: str, price: float):
    return {"item_name": name, "price": price}

@router.put("/items/{item_id}")
def update_item(item_id: int, name: str, price: float):
    return {"item_id": item_id, "name": name, "price": price}

@router.delete("/items/{item_id}")
def delete_item(item_id: int):  
    return {"message": f"Item {item_id} deleted"}

# Query params
@router.get("/users/")
def read_user_with_query(user_id: int, name: str = None):
    return {"user_id": user_id, "name": name}

# Combining path + query params
@router.get("/users/{user_id}/details")
def read_user_details(user_id: int, include_email: bool = False):
    if include_email:
        return {"user_id": user_id, "include_email": "email included"}
    else:
        return {"user_id": user_id, "include_email": "email not included"}
