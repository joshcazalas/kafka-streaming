#!/bin/bash

# Start kafka server
cd kafka-topic/kafka_2.13-3.6.1
./bin/kafka-server-start.sh config/server.properties
