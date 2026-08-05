from fastapi import APIRouter,Depends
from schemas.orders import OrderResponse,OrderCreate
from  sqlalchemy.orm import Session
from database.dependency import get_db
from services.orders import createNewOrder
from services.auth2 import verify_token

router = APIRouter(prefix="/orders",tags=["orders"],dependencies=[Depends(verify_token)])

@router.post("/",response_model=OrderResponse,status_code=201)
async def createOrder(order:OrderCreate,db:Session = Depends(get_db)):
    return await createNewOrder(order,db)