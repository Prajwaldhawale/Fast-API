from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

def users(BaseModel):
  name:str
  age: int
  domain:str
  semester:int

@app.post("/create_user")
def create_user(user: users):
  return{
    "message":"User Created",
    "data":users
  }