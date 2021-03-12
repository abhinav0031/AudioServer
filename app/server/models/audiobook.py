from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel,  Field


class AudiobookSchema(BaseModel):
    title: str = Field(...)
    author: str = Field(...)
    narrator: str = Field(...)
    duration: int = Field(...)


class UpdateAudiobookModel(BaseModel):
    title: Optional[str]
    author: Optional[str]
    narrator: Optional[str]
    duration: Optional[int]


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
