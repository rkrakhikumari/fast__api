from pydantic import BaseModel

class UserCreate(BaseModel):
    first_name : str
    last_name : str
    email : str
    password : int

class UserOut(BaseModel):
    id : int
    first_name : str
    last_name : str
    email : str
    class Config:
        orm_mode = True


class TodoSchema(BaseModel):
    id : int
    title : str
    description: str | None = None
    class Config:
        orm_mode = True

class TodoCreate(BaseModel):
    title: str
    description: str | None = None