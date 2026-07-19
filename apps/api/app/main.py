from fastapi import FastAPI

from app.core.config import settings
from app.api.routes import router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="NEXORA - The Intelligence Layer for Modern Businesses",
)

app.include_router(router)


@app.get("/")
def home():
    return {
        "product": settings.APP_NAME,
        "status": "running",
        "version": settings.APP_VERSION,
        "message": "Welcome to NEXORA 🚀",
    }