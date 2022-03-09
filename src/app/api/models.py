from pydantic import BaseModel


class NoteSchema(BaseModel):
    title: str
    description: str


class NoteDb(NoteSchema):
    id: int
