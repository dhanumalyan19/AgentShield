from fastapi import FastAPI

from app.api.router import api_router
from app.core.config import settings
from app.database.database import Base, engine

# Create database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    description="Secure Execution Layer for Agentic AI using MCP",
    version=settings.APP_VERSION,
)

app.include_router(api_router)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.APP_NAME}",
        "status": "Running Successfully",
        "version": settings.APP_VERSION,
    }