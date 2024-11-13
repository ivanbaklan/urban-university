from pydantic import BaseModel


class User(BaseModel):
    firstname: str
    lastname: str
    age: int


class CreateUser(User):
    username: str


class UpdateUser(User):
    user_id: int


class Task(BaseModel):
    title: str
    content: str
    priority: int


class CreateTask(Task):
    pass


class UpdateTask(CreateTask):
    pass
