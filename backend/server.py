# server.py
# Main FastAPI application entry point

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db_connect import engine, get_db
import sql_tables

# Create all tables in the database on startup
sql_tables.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Creation Health App API",
    description="Backend API for the Creation Virtual Health Application",
    version="1.0.0"
)

@app.get("/")
def home():
    return {"message": "Creation Health App Backend is running! 🚀"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}