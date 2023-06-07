from typing import Annotated, List, Dict

from fastapi import FastAPI, Body, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

from auth.auth_bearer import JWTBearer
from auth.auth_handler import signJWT, decodeJWT


class UserModel(BaseModel):
    id : str
    username : str
    password : str

dict_example = {
        'id': '1',
        'username': 'admin',
        'password': 'admin'
    }

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth")

app = FastAPI()

@app.post("/auth")
def auth(user: OAuth2PasswordRequestForm = Depends()) -> dict:

    print(user.username)
    print(user.password)
    print(user.username == dict_example['username'])
    print(user.password == dict_example['password'])
    
    if user.username == dict_example['username'] and user.password == dict_example['password']: 
        id_user = '1'
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User or password is invalid")

    token = signJWT(id_user)

    return {
        "access_token": token['access_token']
    }

async def get_user(token: str = Depends(oauth2_scheme)) -> dict:
    user = decodeJWT(token)

    return user


@app.post("/protected", tags=["protected"])
async def protected(user: str = Depends(get_user)) -> dict:


    # user = decodeJWT(token)
    
    return user

@app.post("/posts", tags=["posts"])
async def add_post(user: str = Depends(get_user)) -> dict:
    
    return {
        "msg": f"Hello {user['sub']}"
    }