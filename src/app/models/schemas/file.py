from datetime import datetime

from pydantic import BaseModel


class FileBaseScheme(BaseModel):
    filename: str
    conversion_date: datetime
    user_id: int


class FileCreateScheme(BaseModel):
    filename: str
    conversion_date: datetime
