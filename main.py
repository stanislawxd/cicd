from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"spoko wiadomosc i tyle"}

@app.get("/add/{a}/{b}")
def add(a:int,b:int):
    return{"result":a+b}