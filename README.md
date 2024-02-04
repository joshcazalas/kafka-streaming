### Kafka-Streaming
-------------------
This project uses python, bash, and Docker to create a POC for a real-time streaming solution with Apache Kafka

## Prerequisites
-------------------
1. Ubuntu 22.04 (or the latest LTS version)
2. Docker Desktop with WSL integration enabled
3. DBeaver Community (or other preferred DB tool)

## Setup
-------------------
1. Run `kafka_install.sh` with the following command: `./kafka_install.sh`
This will pull the Docker image, start a container using the image, install Apache Kafka, install the required Python libraries, and start zookeeper, a requirement for running Kafka. After this script is complete, leave the current tab open in Ubuntu to allow Zookeeper to run in the background and open a new Ubuntu tab to continue.
2. Run `start_kafka_server.sh` with the following command: `./start_kafka_server.sh`
This will open the directory that Kafka was installed in and start a locally hosted Kafka server. After the script is complete, leave the current open as well to allow the Kafka server to run in the background. Open a new Ubuntu tab to continue.
3. Run `create_kafka_topic.sh` with the following command: `./create_kafka_topic.sh`
This will create a Kafka topic called `arrest` which will be used in the following steps for real time data streaming.