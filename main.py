from fastapi import FastAPI , Depends, HTTPException # type: ignore
from typing import List
from database import sessionmaker , engine , SessionLocal
from models import Todo, Base
from sqlalchemy.orm import Session
from schemas import TodoCreate, TodoSchema

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.get("/")
def todo_home():
    return {"message": "Welcome to Todo"}  


@app.post("/create-todo", response_model=TodoSchema)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(title = todo.title, description=todo.description)
    db.add(db_todo)
    db.commit()
    return db_todo


@app.get("/all-todo", response_model=List[TodoSchema])
def all_todo(db: Session = Depends(get_db)):
    return db.query(Todo).all()


@app.get("/todo/{todo_id}", response_model=TodoSchema)
def get_todo(todo_id: int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")
    return todo


@app.put("/todo-update/{todo_id}", response_model=TodoSchema)
def update_todo(todo_id: int, updated: TodoCreate, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="not found" )
    todo.title = updated.title
    todo.description = updated.description
    db.commit()
    return todo

@app.delete("/todo-delete/{todo_id}")
def delete_todo(todo_id : int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="todo not found")
    db.delete(todo)
    db.commit()
    return {"msg":"todo deleted"}
    

    