from typing import Annotated

from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()
num = 0
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users")
async def get_users():
    global users
    return users


@app.post("/user/{username}/{age}")
async def post_user(
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Enter username",
            example="UrbanUser",
        ),
    ],
    age: Annotated[
        int,
        Path(
            ge=18,
            le=120,
            description="Enter age",
            example=24
        )
    ],
):
    global num, users
    num = num + 1
    user = User(id=num, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[
        int,
        Path(
            ge=1,
            le=100,
            description="Enter User ID",
            example=1)
    ],
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Enter username",
            example="UrbanUser",
        ),
    ],
    age: Annotated[
        int,
        Path(
            ge=18,
            le=120,
            description="Enter age",
            example=25
        )
    ],
):
    global users
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    return HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(
    user_id: Annotated[
        int,
        Path(
            ge=1,
            le=100,
            description="Enter User ID",
            example=1
        )
    ],
):
    global users
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    return HTTPException(status_code=404, detail="User was not found")
