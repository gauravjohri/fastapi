from fastapi import APIRouter, HTTPException,Depends
from services.auth import create_access_token
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer

router = APIRouter(prefix="/login",tags=["login"])

@router.post("/",status_code=401)
def login(data:OAuth2PasswordRequestForm=Depends()):
    user = {
        "username": "gaurav",
        "password": "admin@123"
    }

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid User!!"
                            )

    if user["password"] != data.password:
        raise HTTPException(
            status_code=401,
            detail="Wrong Password"
        )

    newUserData = {"sub": user["username"]}
    token = create_access_token(newUserData) 

    return {
        "access_token":token,
        "token:type":"Bearer"
        }