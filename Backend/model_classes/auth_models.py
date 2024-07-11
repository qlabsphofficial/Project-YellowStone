from pydantic import BaseModel


class UserModel(BaseModel):
    username: str
    password: str


class RecordModel(BaseModel):
    username: str
    password: str