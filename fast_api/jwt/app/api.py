from typing import Annotated

from fastapi import FastAPI, Body, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT, decodeJWT


class UserModel(BaseModel):
    id : int
    username : str
    password : str

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

@app.post("/auth")
def auth(user: UserModel) -> dict:
    
    token = signJWT(user.id)
    return {
        "access_token": token['access_token']
    }

@app.post("/protected", tags=["protected"])
async def protected(user: str = Depends(JWTBearer())) -> dict:


    # user = decodeJWT(token)
    
    return user

# @app.post("/posts", dependencies=[Depends(JWTBearer())], tags=["posts"])
# async def add_post() -> dict:
    
#     return {
#         "msg": f"Hello 1"
#     }