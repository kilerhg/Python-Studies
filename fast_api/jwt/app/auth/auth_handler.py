import time
from typing import Dict

import jwt

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
        "user_id": user_id,
        "expires": time.time() + HOUR,
        "type": 'two_auth'
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)

def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except Exception as erro:
        print(erro)
        return {}

if __name__ == '__main__':
    token = signJWT(1)
    time.sleep(2)
    print(decodeJWT(token['access_token']))