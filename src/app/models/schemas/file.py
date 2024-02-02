from datetime import datetime

from pydantic import BaseModel


class FileBase(BaseModel):
    filename: str
    conversion_date: datetime
    user_id: int


class FileCreate(BaseModel):
    filename: str
    conversion_date: datetime
