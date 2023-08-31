import jwt
import os
from dotenv import load_dotenv
from fastapi import HTTPException
import base64


def decode_jwt(access_token: str):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(os.path.join(BASE_DIR, "../.env"))
    SECRET = os.environ.get("JWT_KEY")
    email = ""
    try:
        email = jwt.decode(access_token[7:], base64.b64decode(SECRET), algorithms='HS256')['sub']
    except:
        HTTPException(status_code=401, detail="Token Expired")
    return email
