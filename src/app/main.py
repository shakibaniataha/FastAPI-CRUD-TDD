from fastapi import FastAPI
from app.api.ping import router as ping_router
from app.api.notes import router as notes_router
from app.db import engine, database, metadata


metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping_router)
app.include_router(notes_router)
