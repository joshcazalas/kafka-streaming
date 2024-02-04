from confluent_kafka import Producer
from helper_functions.postgres_functions import create_kafka_staging_area
from datetime import date
import psycopg2
import socket
import json

def date_encoder(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")

# Kafka producer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': socket.gethostname()
}

# Create a Kafka producer instance
producer = Producer(conf)

connection = psycopg2.connect(host='localhost',
        database='postgres',
        user='postgres',
        password='admin',
        port='5520'
    )
connection.autocommit = True

# Message with sample data from postgres instance
with open('sample_records/sample_data.json', 'r') as file:
        json_data = json.load(file)

table_names = list(json_data.keys())
create_kafka_staging_area(connection, table_names,'public', 'kafka')
print(json_data)

# Serialize the JSON message
serialized_message = json.dumps(json_data, default=date_encoder)

# Publish the message to the Kafka topic
producer.produce('arrest', key='sample_key', value=serialized_message)

# Wait for any outstanding messages to be delivered and delivery reports received
producer.flush()

print("JSON data published.")
