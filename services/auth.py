from jose import jwt,JWTError
from datetime import datetime,timedelta
from database.config import SECRET_KEY,ALGORITHM
from fastapi import HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def create_access_token(data:dict):
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    payload.update({
        "exp": expire
    })
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
        )
    return token

def verify_token(token:str= Depends(oauth2_scheme)):
    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=ALGORITHM
            )
        
        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
                )

        return username
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token Invalid"
        )