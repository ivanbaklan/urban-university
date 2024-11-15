from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from slugify import slugify
from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session

from app.backend.db_depends import get_db
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get("/task_id")
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="There is no task found"
        )
    return task


@router.post("/create")
async def create_task(db: Annotated[Session, Depends(get_db)], create_task: CreateTask):
    user = db.scalars(select(User).where(User.id == create_task.user_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="There is no user found"
        )
    db.execute(
        insert(Task).values(
            user_id=create_task.user_id,
            title=create_task.title,
            content=create_task.content,
            priority=create_task.priority,
            slug=slugify(create_task.title),
        )
    )
    db.commit()
    return {
        "status_code": status.HTTP_201_CREATED,
        "transaction": "Task create successful",
    }


@router.put("/update")
async def update_task(db: Annotated[Session, Depends(get_db)], update_task: UpdateTask):
    task = db.scalars(select(Task).where(Task.id == update_task.task_id)).first()
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="There is no task found"
        )
    db.execute(
        update(Task)
        .where(Task.id == update_task.task_id)
        .values(
            title=update_task.title,
            content=update_task.content,
            priority=update_task.priority,
            slug=slugify(update_task.title),
        )
    )
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task update successful"}


@router.delete("/delete")
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    user = db.scalars(select(Task).where(Task.id == task_id)).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="There is no task found"
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task delete successful"}
