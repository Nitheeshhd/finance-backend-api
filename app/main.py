from fastapi import FastAPI, Request
from app.routes import user_routes, record_routes, dashboard_routes
from app.middleware.role_middleware import role_checker

app = FastAPI()

# Middleware
@app.middleware("http")
async def middleware(request: Request, call_next):
    return await role_checker(request, call_next)

# Routes
app.include_router(user_routes.router)
app.include_router(record_routes.router)
app.include_router(dashboard_routes.router)

# ✅ ADD THIS (IMPORTANT)
@app.get("/")
def home():
    return {"message": "Finance Backend Running 🚀"}