import json
import time
import logging
import pandas as pd
from kafka import KafkaProducer
from datetime import datetime

# ---------------------------
# Configuration
# ---------------------------
KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "stock-metadata"
CSV_PATH = "data/symbols_valid_meta.csv"
SLEEP_INTERVAL = 0.5  # seconds

# ---------------------------
# Logging
# ---------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

# ---------------------------
# Kafka Producer
# ---------------------------
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    retries=5
)

logging.info("Kafka Producer initialized")

# ---------------------------
# Read CSV & Publish Events
# ---------------------------
def publish_stock_events():
    df = pd.read_csv(CSV_PATH)

    for _, row in df.iterrows():
        event = row.to_dict()

        # Add event timestamp
        event["event_ts"] = datetime.utcnow().isoformat()

        try:
            producer.send(TOPIC_NAME, value=event)
            logging.info(f"Sent event for symbol: {event.get('Symbol')}")
            time.sleep(SLEEP_INTERVAL)

        except Exception as e:
            logging.error(f"Failed to send event: {e}")

    producer.flush()
    logging.info("All events published successfully")

# ---------------------------
# Entry Point
# ---------------------------
if __name__ == "__main__":
    publish_stock_events()
