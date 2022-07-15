from fastapi import FastAPI, Path, Query, HTTPException, status
import logging
from typing import Optional
from pydantic import BaseModel

# run with uvicorn app:app --reload

'''
Project Todo

[ ] Create a simple CRUD API for games
[ ] Create a simple CRUD API for users
[ ] Create a simple CRUD API to reference games to users
[ ] Select a game by name and return the game's details
[ ] Select a user by name and return the user's details
[ ] Select a user by name and return the user's games
[ ] Select a game by name and return the game's users
[ ] Implement a simple search feature for games
[ ] Implement JWT authentication for the API
[ ] Create some sample protected routes
[ ] Create a simple health check route
[ ] Create a refactor using blueprints

'''

app = FastAPI()



@app.get("/")
def index():
    return {"message": "Hello World"}

