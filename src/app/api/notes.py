from fastapi import APIRouter, HTTPException
from app.api import crud
from app.api.models import NoteDb, NoteSchema
from typing import List

router = APIRouter(tags=["notes"], prefix="/notes")


@router.post("/", response_model=NoteDb, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await crud.post(payload)

    response_object = {
        "id": note_id,
        "title": payload.title,
        "description": payload.description,
    }

    return response_object


@router.get("/{id}", response_model=NoteDb, status_code=200)
async def get_note(id: int):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Not Found")

    return note


@router.get("/", response_model=List[NoteDb], status_code=200)
async def get_all_notes():
    notes = await crud.get_all()
    return notes


@router.put("/{id}", response_model=NoteDb, status_code=200)
async def update_note(id: int, payload: NoteSchema):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Not Found")

    await crud.put(id, payload)

    response_object = {
        "id": id,
        "title": payload.title,
        "description": payload.description,
    }

    return response_object
