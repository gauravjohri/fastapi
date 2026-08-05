import json
from kafka.config import BOOTSTRAP_SERVER,TOPIC,GROUP_ID
from aiokafka import AIOKafkaConsumer
from database.database import sessionLocal
from sqlalchemy import text

async def consume():

    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP_SERVER,
        group_id=GROUP_ID,
        value_deserializer= lambda x: json.loads(x.decode())
        )

    await consumer.start()
    db =sessionLocal()
    try:
        async for msg in consumer:
            print("Recieved!!")
            db.execute(text(" insert into  orders (product_name) values('Consmer serveice hited')"))
            db.commit()
           
            print(msg.value)
    finally:
        await consumer.stop()

    db.close()