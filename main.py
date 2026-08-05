import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import (orders,login)
from kafka.producer import(
    start_producer,
    stop_producer
    )
from kafka.consumer import consume

@asynccontextmanager
async def lifespan(app: FastAPI):

    await start_producer()

    asyncio.create_task(consume())
    
    print("Application started")

    yield 

    await stop_producer()

    print("Application stopped")

    
app = FastAPI(lifespan=lifespan)

app.include_router(login.router)
app.include_router(orders.router)

@app.get("/")
def home():
    return {"message":"Welcome to the jungle!!"}