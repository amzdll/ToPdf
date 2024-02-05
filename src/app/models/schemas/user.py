from pydantic import BaseModel


class UserBaseScheme(BaseModel):
    id: int
