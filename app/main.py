from fastapi import FastAPI
from random import randint

app = FastAPI()

@app.get('/')
def HelloWorld():
    return {"Hello": "World"}

@app.get('/coinflip')
def coinflip():
    return {"result": "head" if randint(0,1) == 1 else "tail"}

@app.get('/random')
def randomNumber():
    return {"result":randint(1,200)}