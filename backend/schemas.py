from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True

# ----- Comment Schemas -----
class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    task_id: int

    class Config:
        from_attributes = True
 
