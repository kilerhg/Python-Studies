import time
from typing import Dict

from jose import JWTError, jwt
from fastapi import HTTPException, status

JWT_SECRET = '--very secret key--'
JWT_ALGORITHM = 'HS256'
SECOND = 1
MINUTE = SECOND * 60
HOUR = MINUTE * 60


def token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(user_id: str) -> Dict[str, str]:
    payload = {
        "sub": user_id,
        "exp": time.time() + HOUR,
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token")
        

if __name__ == '__main__':
    token = signJWT(1)
    time.sleep(2)
    print(decodeJWT(token['access_token']))