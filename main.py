from kafka import KafkaConsumer
from consumer import consume_kafka_message

consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                group_id=None,
                auto_offset_reset='latest'
              )

consume_kafka_message(consumer, ['arrest'])
