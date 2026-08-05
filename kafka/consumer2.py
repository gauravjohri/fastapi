from aiokafka import AIOKafkaConsumer
from kafka.config import TOPIC,BOOTSTRAP_SERVER,GROUP_ID

async def consume():
    consumer = AIOKafkaConsumer(
        TOPIC,
        bootstrap_servers=BOOTSTRAP_SERVER,
        group_id=GROUP_ID
        )
    await consumer.start()
    try:
        async for msg in consumer:
            print(msg.value)
    finally:
        await consumer.stop()
    