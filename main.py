import subprocess
import psycopg2
from kafka import KafkaConsumer
from consumer import consume_kafka_message
from helper_functions.postgres_functions import create_kafka_staging_area

connection = psycopg2.connect(host='localhost',
        database='postgres',
        user='postgres',
        password='admin',
        port='5520'
    )
connection.autocommit = True

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                         group_id=None,
                         auto_offset_reset='latest'
                        )

# Create area in the postgres database to land data ingested by Kafka
create_kafka_staging_area(connection, ['arrests','complaints','officer'], 'public', 'kafka')

# Start Kafka consumer
consume_kafka_message(consumer, connection,['arrest'])
