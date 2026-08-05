from jose import jwt,JWTError
from fastapi import HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from database.config import SECRET_KEY,ACCESS_TOKEN_EXPIRE_MINUTES,ALGORITHM
from datetime import datetime,timedelta

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/login")

def create_token(data:dict):

    payload = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    payload.update({
        "exp": expire
        })

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
        )

    return token

def verify_token(token:str = Depends(oauth2_schema)):
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
                detail="Invalid User!!"
                )
        
        return username

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
            )