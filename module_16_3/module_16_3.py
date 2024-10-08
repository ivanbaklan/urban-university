from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()
num = 1
users = {1: "Имя: Example, возраст: 18"}


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
    users[num] = f"Имя: {username}, возраст: {age}"
    return f"User {num} is registered"


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
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


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
    users.pop(user_id)
    return f"User {user_id} has been deleted"
