### Kafka-Streaming
-------------------
This project uses Python, Bash, Docker, and Apache Kafka to create a POC for a real-time streaming solution. 

## Overview
------------------
The project consists of a few different areas. 

# Scripts
The scripts directory contains shell scripts used to install dependencies. See the Setup section below for install steps.

# Producer and Consumer
The two main pieces are the python files producer.py and consumer.py. As their names suggest, producer publishes data to a Kafka topic, and consumer consumes data from a Kafka topic and pushes it to the postgres database. consumer.py is a consumer function which is controlled by main.py, which tells it the location of the Kafka server and the desired topic. Both of these .py files use the helper functions directory, which is full of other python helper functions.

# SQL
The sql directory contains a few relevant .sql files used by the producer and consumer, mainly for creating tables and inserting data when needed.

# Sample Records
The sample_records directory contains a json file with sample records for multiple tables. These sample records are what is published to the Kafka topic when producer.py is run.

## Prerequisites
-------------------
1. Ubuntu 22.04 (or the latest LTS version)
2. Docker Desktop with WSL integration enabled. More info [here](https://docs.docker.com/desktop/wsl/).
3. DBeaver Community (or other preferred DB tool)

## Setup
-------------------
1. Navigate to the scripts directory: `cd scripts/`

This directory contains shell scripts which will assist with installing all of the required dependencies for this project.

1. Run `kafka_install.sh` with the following command: `./kafka_install.sh`

This will pull the Docker image, start a container using the image, install Apache Kafka, install the required Python libraries, and start zookeeper, a requirement for running Kafka. After this script is complete, leave the current tab open in Ubuntu to allow Zookeeper to run in the background. Open a new Ubuntu tab and navigate back to the scripts directory to continue.

2. Run `start_kafka_server.sh` with the following command: `./start_kafka_server.sh`

This will open the directory that Kafka was installed in and start a locally hosted Kafka server. After the script is complete, leave the current open as well to allow the Kafka server to run in the background. Open a new Ubuntu tab and navigate back to the scripts directory to continue.

3. Run `create_kafka_topic.sh` with the following command: `./create_kafka_topic.sh`

This will create a Kafka topic called `arrest` which will be used in the following steps for real time data streaming.

## Real-Time Data Streaming
----------------------
Once Kafka is set up, use the following steps to execute real-time streaming:

1. In one tab, execute main.py and leave it running: `python3 main.py`
main.py polls the Kafka topic for new records in an infinite loop, grabbing and processing records as they come.

2. In another tab, execute producer.py to publish the data found in the sample_records directory to the Kafka topic. The instance of consumer.py still running in the previous tab will automatically publish the records to postgres. Switch back to the consumer tab to see insert info and runtimes for each published message.

## Errors
----------------------
If the error `bash: ./file_name.sh: Permission denied` is encountered, run `chmod +x file_name.sh` to grant execute permission on the file.