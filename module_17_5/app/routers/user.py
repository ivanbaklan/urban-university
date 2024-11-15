from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from slugify import slugify
from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session

from app.backend.db_depends import get_db
from app.models import Task, User
from app.schemas import CreateUser, UpdateUser

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users


@router.get("/user_id")
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="There is no user found"
        )
    return user


@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):
    db.execute(
        insert(User).values(
            username=create_user.username,
            firstname=create_user.firstname,
            lastname=create_user.lastname,
            age=create_user.age,
            slug=slugify(create_user.username),
        )
    )
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "User create successful",
    }


@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)], update_user: UpdateUser):
    user = db.scalars(select(User).where(User.id == update_user.user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="There is no user found"
        )
    db.execute(
        update(User)
        .where(User.id == update_user.user_id)
        .values(
            firstname=update_user.firstname,
            lastname=update_user.lastname,
            age=update_user.age,
        )
    )
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User update successful"}


@router.delete("/delete")
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="There is no user found"
        )
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.execute(delete(User).where(User.id == user_id))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User delete successful"}


@router.get("/user_id/tasks")
async def tasks_by_user_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="There is no user found"
        )
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    if tasks is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="There is no task found"
        )
    return tasks
