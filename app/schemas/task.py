from typing import Optional

from pydantic import BaseModel


class TaskCreate(BaseModel):
    title:str
    description:str

class TaskUpdate(BaseModel):
    title:Optional[str] = None
    description:Optional[str] = None
    completed:Optional[bool] = None

class TaskResponse(BaseModel):
    id:int
    title:str
    description:str
    completed:bool
    user_id:int
    model_config = {"from_attributes": True}
