from typing import List, Optional
from datetime import date, datetime
from pydantic import BaseModel,  Field


class PodcastSchema(BaseModel):
    name: str = Field(...)
    duration: int = Field(...)
    host: str = Field(...)
    participants: Optional[List[str]]


class UpdatePodcastModel(BaseModel):
    name: Optional[str]
    duration: Optional[int]
    host: Optional[str]
    Participants: Optional[List[str]]


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
