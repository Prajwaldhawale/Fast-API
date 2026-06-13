from fastapi import FastAPI
app = FastAPI()
@app.post("/create_user")
def create_user(name:str, age: int, domain:str,semester:int):
  return{
    "message":"User Created",
    "data":{
      "name":name,
      "age":age,
      "semester":semester,
      "domain":domain
    }
  }