from fastapi import FastAPI
from database import engine, Base
from routers import webhook

import models


Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(
    webhook.router
)

@app.get("/")
def home():

    return {
        "message":"AI Assistant Backend Running"
    }