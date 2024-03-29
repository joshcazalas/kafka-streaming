#!/bin/bash

# Pull and run the docker image
docker pull impulse101587/test-data:latest
docker run --restart always -p 5520:5432 --name postgres-container -d impulse101587/test-data

# Install dependencies
sudo apt update
sudo apt install -y default-jre
sudo apt install -y python3-pip
pip3 install -r requirements.txt
wget https://downloads.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz
tar -xzf kafka_2.13-3.6.1.tgz
rm -f kafka_2.13-3.6.1.tgz

# Start zookeeper
cd kafka_2.13-3.6.1
nohup ./bin/zookeeper-server-start.sh config/zookeeper.properties &

sleep 15

# Start Kafka server
nohup ./bin/kafka-server-start.sh config/server.properties &

sleep 15

# Delete Kafka topic if exists
./bin/kafka-topics.sh --delete --topic arrest-topic --bootstrap-server localhost:9092

sleep 10

# Create Kafka topic
./bin/kafka-topics.sh --create --topic arrest-topic --bootstrap-server localhost:9092

# Start Flask App
cd ..
nohup python3 flask_app.py &

# Start the consumer
python3 main.py
