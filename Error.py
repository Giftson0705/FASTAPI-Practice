from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Custom exception
class ProductNotFoundError(HTTPException):
    def __init__(self, product_id: int):
        super().__init__(status_code=404, detail=f"Product {product_id} not found")

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Global error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"error": "Something went wrong", "path": str(request.url)}
    )

# Route with error handling
@app.get("/products/{product_id}")
async def get_product(product_id: int):
    try:
        if product_id < 1:
            raise ValueError("Product ID must be positive")
        
        # Simulate database lookup
        products = {1: "Laptop", 2: "Phone"}
        
        if product_id not in products:
            raise ProductNotFoundError(product_id)
        
        return {"id": product_id, "name": products[product_id]}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))