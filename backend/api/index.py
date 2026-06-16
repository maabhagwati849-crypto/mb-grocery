from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        if self.path == '/api/health':
            response = {"status": "ok"}
        
        elif self.path == '/api/categories':
            response = [
                {"category_id": "veg", "name": "Fresh Vegetables", "slug": "vegetables", "image": "https://images.unsplash.com/photo-1566385101042-1a0aa0c1268c"},
                {"category_id": "fruit", "name": "Fresh Fruits", "slug": "fruits", "image": "https://images.unsplash.com/photo-1610832958506-aa56368176cf"},
                {"category_id": "dairy", "name": "Dairy & Eggs", "slug": "dairy", "image": "https://images.unsplash.com/photo-1550583724-b2692b85b150"},
                {"category_id": "snacks", "name": "Snacks & Munchies", "slug": "snacks", "image": "https://images.unsplash.com/photo-1599490659213-e2b9527bd08c"},
                {"category_id": "bakery", "name": "Bakery & Breads", "slug": "bakery", "image": "https://images.unsplash.com/photo-1509440159596-0249088772ff"},
            ]
        
        elif self.path == '/api/products' or self.path.startswith('/api/products'):
            response = [
                {"product_id": "p1", "name": "Fresh Tomato", "price": 28, "mrp": 40, "unit": "1 kg", "image": "https://images.unsplash.com/photo-1546470427-227df1e3a5be", "category_id": "veg"},
                {"product_id": "p2", "name": "Red Apple", "price": 180, "mrp": 240, "unit": "1 kg", "image": "https://images.unsplash.com/photo-1568702846914-96b305d2aaeb", "category_id": "fruit"},
                {"product_id": "p3", "name": "Amul Milk", "price": 34, "mrp": 36, "unit": "500 ml", "image": "https://images.unsplash.com/photo-1550583724-b2692b85b150", "category_id": "dairy"},
                {"product_id": "p4", "name": "Lays Chips", "price": 20, "mrp": 20, "unit": "52 g", "image": "https://images.unsplash.com/photo-1599490659213-e2b9527bd08c", "category_id": "snacks"},
                {"product_id": "p5", "name": "Brown Bread", "price": 45, "mrp": 50, "unit": "400 g", "image": "https://images.unsplash.com/photo-1509440159596-0249088772ff", "category_id": "bakery"},
            ]
        
        elif self.path == '/api/auth/me':
            response = {"user_id": "test123", "name": "Test User", "email": "test@blinkit.com", "role": "user"}
        
        elif self.path == '/api/auth/login':
            response = {"token": "fake-token", "user": {"name": "Test User", "email": "test@blinkit.com"}}
        
        else:
            response = {"error": "Not found", "path": self.path}
        
        self.wfile.write(json.dumps(response).encode())
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        if self.path == '/api/auth/login':
            response = {"token": "fake-token", "user": {"name": "Test User", "email": "test@blinkit.com"}}
        elif self.path == '/api/auth/register':
            response = {"token": "fake-token", "user": {"name": "Test User", "email": "test@blinkit.com"}}
        else:
            response = {"ok": True}
        
        self.wfile.write(json.dumps(response).encode())