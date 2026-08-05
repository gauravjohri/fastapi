from pydantic import BaseModel

class OrderCreate(BaseModel):
    product_name:str
    customer_name:str
    quantity:int
    price:float

class OrderResponse(OrderCreate):
    id:int

    class Config:
        from_attributes:True