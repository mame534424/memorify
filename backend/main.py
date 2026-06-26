from fastapi import FastAPI
from database import engine
from sqlalchemy import text

app = FastAPI()


@app.get("/")
def home():

    return {
        "message": "AI Assistant Backend Running"
    }
    
@app.get("/db-test")
def database_test():

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT 1")
        )

    return {
        "database": "connected"
    }