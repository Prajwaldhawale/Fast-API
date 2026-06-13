from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
def get_user(name: str = None):
  return {'name':name}