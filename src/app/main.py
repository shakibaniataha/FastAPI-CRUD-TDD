from fastapi import FastAPI
from app.api.ping import router

app = FastAPI()


app.include_router(router)
