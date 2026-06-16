from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
async def health():
    return {"status": "ok"}

@app.get("/api/categories")
async def get_categories():
    return [
        {"category_id": "veg", "name": "Vegetables", "slug": "vegetables", "image": "https://images.unsplash.com/photo-1566385101042-1a0aa0c1268c"},
        {"category_id": "fruit", "name": "Fruits", "slug": "fruits", "image": "https://images.unsplash.com/photo-1610832958506-aa56368176cf"},
    ]

@app.get("/api/products")
async def get_products():
    return [
        {"product_id": "p1", "name": "Tomato", "price": 28, "mrp": 40, "unit": "1 kg", "image": "https://images.unsplash.com/photo-1546470427-227df1e3a5be", "category_id": "veg"},
        {"product_id": "p2", "name": "Apple", "price": 180, "mrp": 240, "unit": "1 kg", "image": "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb", "category_id": "fruit"},
    ]

@app.post("/api/auth/login")
async def login():
    return {"token": "fake-token", "user": {"name": "Test User", "email": "test@blinkit.com"}}

@app.get("/api/auth/me")
async def get_me():
    return {"user_id": "test123", "name": "Test User", "email": "test@blinkit.com", "role": "user"}

handler = app