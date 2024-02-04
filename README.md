Prerequisites: Ubuntu, Docker Desktop, DBeaver Community (or preferred DB tool)

1. Create a new directory, pull the image, and install Apache Kafka
mkdir kafka-topic
cd kafka-topic
docker pull impulse101587/test-data:latest
docker run --restart always -p 5520:5432 --name test-data -d impulse101587/test-data
sudo apt update
sudo apt install -y default-jre
wget https://downloads.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz
tar -xzf kafka_2.13-3.6.1.tgz

2. Start zookeeper
cd kafka_2.13-3.6.1
./bin/zookeeper-server-start.sh config/zookeeper.properties
open new tab

3. Start a kafka server
cd kafka-topic/kafka_2.13-3.6.1
./bin/kafka-server-start.sh config/server.properties
open another new tab

4. Create a topic called arrest
cd kafka-topic/kafka_2.13-3.6.1
./bin/kafka-topics.sh --create --topic arrest --bootstrap-server localhost:9092


5. Create a landing area in the postgres database:
sudo apt install -y python3-pip
pip install confluent_kafka
pip install psycopg2-binary
touch postgres.py
code .
--set up tables in separate schema
create schema kafka;
create table kafka.arrests as
  select * from public.arrests
with no data;
create table kafka.arrest_type as
  select * from public.arrest_type
with no data;
create table kafka.officer as
  select * from public.arrest_type
with no data;

--python script to process events
sudo apt install python3-pip
pip3 install confluent_kafka
pip3 install kafka-python
pip3 install psycopg2-binary
touch consumer.py
touch producer.py

from confluent_kafka import Consumer, KafkaException, KafkaError
import psycopg2
import json

def process_message(message):
    print(f"Received message: {message.decode('utf-8')}")
    try:
        data = json.loads(message)

        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="admin"
        )

        cursor = conn.cursor()

        # Insert data into PostgreSQL tables (adjust queries and tables accordingly)
        for arrest in data.get("arrests", []):
            cursor.execute(
                sql.SQL("INSERT INTO kafka.arrests (id, officer_id, arrest_date, arrest_time, arrest_type_id, subject_race, crime_type_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"),
                (arrest["id"], arrest["officer_id"], arrest["arrest_date"], arrest["arrest_time"], arrest["arrest_type_id"], arrest["subject_race"], arrest["crime_type_id"])
            )

        for arrest_type in data.get("arrest_type", []):
            cursor.execute(
                sql.SQL("INSERT INTO kafka.arrest_type (id, name) VALUES (%s, %s)"),
                (arrest_type["id"], arrest_type["name"])
            )

        for officer in data.get("officer", []):
            cursor.execute(
                sql.SQL("INSERT INTO kafka.officer (id, employment_start_date, age, military_experience, race_id, gender_id, rank_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"),
                (officer["id"], officer["employment_start_date"], officer["age"], officer["military_experience"], officer["race_id"], officer["gender_id"], officer["rank_id"])
            )

        # Commit changes
        conn.commit()

    except Exception as e:
        print(f"Error processing message: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()
    

# Define Kafka consumer configuration
config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'arrest-event-consumer-group',
    'auto.offset.reset': 'earliest',
}

# Create Kafka consumer
consumer = Consumer(config)

# Subscribe to the Kafka topic
consumer.subscribe(['arrest'])

try:
    while True:
        # Poll for messages
        msg = consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        # Process the received message (implement your processing logic here)
        process_message(msg.value())

except KeyboardInterrupt:
    pass

except json.JSONDecodeError as e:
    print(f"Error parsing JSON message: {e}")

except Exception as e:
    print(f"Error processing message: {e}")

finally:
    # Close down consumer to commit final offsets.
    consumer.close()





from confluent_kafka import Producer
import json

# Kafka producer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

# Create a Kafka producer instance
producer = Producer(conf)

# Sample JSON message
json_message = {"arrests": [{"id":2017,"officer_id":223210,"arrest_date":"2017-11-04","arrest_time":"10:00:00","arrest_type_id":1,"subject_race":"Asian_Pacific Islander","crime_type_id":32}],"arrest_type": [{"id":1,"name":"Cited/Summoned"}],"officer": [{"id":239473,"employment_start_date":"2000-06-18","age":"41 to 50","military_experience":"","race_id":3,"gender_id":2,"rank_id":1}]}

# Serialize the JSON message
serialized_message = json.dumps(json_message)

# Produce the message to the Kafka topic
producer.produce('arrest', key='sample_key', value=serialized_message)

# Wait for any outstanding messages to be delivered and delivery reports received
producer.flush()











