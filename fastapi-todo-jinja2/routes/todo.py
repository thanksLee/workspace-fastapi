from typing import List
from beanie import PydanticObjectId
from database.connection import Database
from fastapi import APIRouter, HTTPException, status, Request, Depends
from models.todo import Todo, TodoUpdate
from fastapi.templating import Jinja2Templates

todo_router = APIRouter(
    tags=["Todos"]
)
todo_database = Database(Todo)
templates = Jinja2Templates(directory="templates/")


@todo_router.post("/")
async def add_tod(request: Request, todo: Todo = Depends(Todo.as_form)):
    await todo_database.save(todo)
    todos = await todo_database.get_all()
    return templates.TemplateResponse(
        "todos.html",
        {
            "request": request,
            "todos": todos
        }
    )


@todo_router.get("/", response_model=List[Todo])
async def retrieve_all_todos(request: Request) -> List[Todo]:
    todos = await todo_database.get_all()
    return templates.TemplateResponse(
        "todos.html",
        {
            "request": request,
            "todos": todos
        }
    )


@todo_router.get("/{id}", response_model=Todo)
async def retrieve_tod(id: PydanticObjectId, request: Request) -> Todo:
    todo = await todo_database.get(id)

    if not todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID dose not exists!"
        )
    return templates.TemplateResponse(
        "todo.html",
        {
            "request": request,
            "todo": todo
        }
    )


@todo_router.put("/{id}", response_model=Todo)
async def update_todo(id: PydanticObjectId, body: TodoUpdate,) -> Todo:
    update_todo = await todo_database.update(id, body)

    if not update_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID dose not exists!"
        )
    return update_todo


@todo_router.delete("/{id}")
async def delete_todo(id: PydanticObjectId) -> dict:
    delete_todo = await todo_database.delete(id)
    if not delete_todo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID dose not exists!"
        )
    return delete_todo
