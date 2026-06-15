from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Temporary in-memory database
todos = []

class Todo(BaseModel):
  id: int
  title: str
  completed: bool

@app.post("/todos")
def create_todo(todo: Todo):
  todos.append(todo)
  return{
    "message":"Todo Added",
    "data": todo
  }

@app.get("/todos")
def get_todos():
  return todos

@app.get("/todos/{todo_id}")
def get_single_todo(todo_id:int):
  for todo in todos:
    if todo.id == todo_id:
      return todo
  return {"error":"Todo not found"}

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, updated_todo: Todo):
  for index, todo in enumerate(todos):
    if todo.id == todo_id:
      todos[index]=updated_todo
      return{
        "message":"Data updated",
        "data":updated_todo
      }
  return {"error":"Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id:int):
  for index,todo in enumerate(todos):
    if todo.id == todo_id:
      todos.pop(index)
      return {"message":"Data Delete"}
  return {"error":"Todo not found"}
#Added this comment to learn PR