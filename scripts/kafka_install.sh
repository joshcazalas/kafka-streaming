#!/bin/bash

cd .. 

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
./bin/zookeeper-server-start.sh config/zookeeper.properties
