from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()
num = 0
users = []
templates = Jinja2Templates(directory="templates")


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/")
async def get_main_page(request: Request) -> HTMLResponse:
    global users
    return templates.TemplateResponse(
        "users.html",
        {
            "request": request,
            "users": users,
        },
    )


@app.get("/user/{user_id}")
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    global users
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse(
                "users.html",
                {
                    "request": request,
                    "user": user,
                },
            )

    return templates.TemplateResponse(
        "404.html",
        {
            "request": request,
        },
        status_code=404,
    )


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
            examples=["UrbanUser"],
        ),
    ],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples=[24])],
):
    global num, users
    num = num + 1
    user = User(id=num, username=username, age=age)
    users.append(user)
    return user


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(
    user_id: Annotated[
        int, Path(ge=1, le=100, description="Enter User ID", examples=[1])
    ],
    username: Annotated[
        str,
        Path(
            min_length=5,
            max_length=20,
            description="Enter username",
            examples=["UrbanUser"],
        ),
    ],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples=[25])],
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
        int, Path(ge=1, le=100, description="Enter User ID", examples=[1])
    ],
):
    global users
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    return HTTPException(status_code=404, detail="User was not found")
