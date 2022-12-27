from fastapi import FastAPI

app = FastAPI()

users = []

@app.post('/register')
def register():
    return {}

@app.post('/login')
def login():
    return {}

@app.get('/unprotected')
def unprotected():
    return {'message': 'hello, world!'}

@app.get('/protected')
def protected():
    return {}
