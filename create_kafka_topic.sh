#!/bin/bash

cd kafka-topic/kafka_2.13-3.6.1
./bin/kafka-topics.sh --create --topic arrest --bootstrap-server localhost:9092
