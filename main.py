from fastapi import FastAPI # type: ignore
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Todo(BaseModel):
    title: str
    description: str | None = None 


todos: List[Todo] = []




@app.get("/")
def todo_home():
    return {"message": "Welcome to Todo"}  


@app.post("/create-todo")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"msg": 'todo created ',"todo": todo}


@app.get("/all-todo")
def all_todo():
    return {"todos":todos}


@app.get("/todo/{todo_id}")
def get_todo(todo_id: int):
    if todo_id < 0 or todo_id >= len(todos):
        return {"msg": f"Todo not found. Current total todos: {len(todos)}"}
    return {"todo": todos[todo_id]}


@app.put("/todo-update/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    if todo_id < 0 or todo_id >= len(todos):
        return {"msg": f"Todo not found. Current total todos: {len(todos)}"}
    todos[todo_id] = update_todo
    return {"msg": "Todo updated successfully", "todo": updated_todo}


@app.delete("/todo-delete/{todo_id}")
def delete_todo(todo_id : int):
    if todo_id < 0 or todo_id >= len(todos):
        return {"msg": f"Todo not found. Current total todos: {len(todos)}"}
    deleted = todos.pop(todo_id)
    return {"msg": "Todo deleted successfully", "deleted_todo": deleted}
    

    