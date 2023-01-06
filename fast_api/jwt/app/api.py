from fastapi import FastAPI, Body, Depends
from pydantic import BaseModel

from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT


class UserModel(BaseModel):
    id : int
    username : str
    password : str


app = FastAPI()

@app.post("/auth")
def auth(user: UserModel) -> dict:
    
    token = signJWT(user.id)
    return {
        "access_token": f"Hello {token['access_token']}"
    }


@app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
async def add_post(user: UserModel) -> dict:
    
    return {
        "msg": f"Hello {user}"
    }