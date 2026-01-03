import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

stocks = ["AAPL", "GOOG", "AMZN", "MSFT", "TSLA"]

while True:
    event = {
        "symbol": random.choice(stocks),
        "price": round(random.uniform(100, 500), 2),
        "volume": random.randint(10, 1000),
        "event_time": time.strftime("%Y-%m-%d %H:%M:%S")
    }

    producer.send("stock-events", event)
    print(event)
    time.sleep(1)
