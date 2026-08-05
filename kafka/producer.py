from aiokafka import AIOKafkaProducer
import json
from kafka.config import BOOTSTRAP_SERVER

producer = None

async def start_producer():
    global producer

    producer = AIOKafkaProducer(
        bootstrap_servers=BOOTSTRAP_SERVER,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )

    await producer.start()

async def stop_producer():
    await producer.stop()

async def publish(topic:str,message:dict):
    await producer.send_and_wait(topic,message)

