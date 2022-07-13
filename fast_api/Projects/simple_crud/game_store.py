from fastapi import FastAPI, Path, Query, HTTPException, status
import logging
from typing import Optional
from pydantic import BaseModel

# run with uvicorn app:app --reload

app = FastAPI()



@app.get("/")
def index():
    return {"message": "Hello World"}