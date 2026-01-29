from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str


class TaskResponse(BaseModel):
    id: int
    title: str
    status: str

    model_config = {
        "from_attributes": True
    }

