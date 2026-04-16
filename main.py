from fastapi import FastAPI
from app.database import create_tables
from app.routes import router

app = FastAPI(
    title="T4G Grade Tracker API",
    description="A backend system for managing student grades across subjects.",
    version="1.0.0"
)

app.include_router(router, prefix="/api", tags=["Students & Grades"])


@app.on_event("startup")
def on_startup():
    create_tables()


@app.get("/", tags=["Health"])
def root():
    return {
        "message": "T4G Grade Tracker API is running.",
        "docs": "Visit /docs to explore the endpoints."
    }