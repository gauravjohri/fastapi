from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from services.auth2 import create_token

router = APIRouter(prefix="/login",tags=["login"])

@router.post("/login",status_code=201)
def login(data:OAuth2PasswordRequestForm = Depends()):
    user = {
        "username": "gaurav",
        "password": "admin@123"
    }

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid User!!"
            )

    if data.password !=user["password"]:
        raise HTTPException(
            status_code=401,
            detail="Wrong PAssword!!"
            )

    userData = {
        "sub":user["username"]
        }

    token = create_token(userData)
    
    return {
        "acess_token": token,
        "token_type":"Bearer"
        }