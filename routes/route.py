from fastapi import APIRouter

from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial

from bson import ObjectId

router = APIRouter()

# Get /
@router.get("/")
async def get_todos():
    todos = collection_name.find()
    return list_serial(todos)

# Post /
@router.post("/")
async def create_todo(todo: Todo):
    # new_todo = Todo(name=todo.name, description=todo.description, complete=todo.complete)
    collection_name.insert_one(dict(todo))
    
# Put /
@router.put("/{todo_id}")
async def update_todo(todo: Todo, todo_id: str):
    collection_name.find_one_and_update({"_id": ObjectId(todo_id)}, {"$set": dict(todo)})
    
# Delete /
@router.delete("/{todo_id}")
async def delete_todo(todo_id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(todo_id)})