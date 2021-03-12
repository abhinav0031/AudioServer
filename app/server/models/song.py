from typing import Optional
from datetime import date, datetime
from pydantic import BaseModel,  Field


class SongSchema(BaseModel):
    name: str = Field(...)
    duration: int = Field(...)


class UpdateSongModel(BaseModel):
    name: Optional[str]
    duration: Optional[int]


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
