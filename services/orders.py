from models.orders import Order
from kafka.producer import (publish)
from kafka.config import TOPIC
async def createNewOrder(order,db):
    newOrder = Order(**order.dict())
    db.add(newOrder)
    db.commit()
    db.refresh(newOrder)
    await publish(TOPIC,order.dict())
    return newOrder