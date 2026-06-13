from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
  return {'message':'Welcome FastAPI'}

@app.get("/about")
def about():
  return {'message':'Welcome To About Section'}

@app.get("/contact")
def contact():
  return {'message':'This is contact page'}

@app.get("/product")
def product():
  return {'message':'Products Collection displayed here'}

@app.get("/login")
def login():
  return {"message":"Login Using google/Phone"}