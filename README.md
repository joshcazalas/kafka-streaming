### Kafka-Streaming
-------------------
This project uses Python, Bash, Docker, and Apache Kafka to create a POC for a real-time streaming solution. 

## Overview
------------------
The project consists of a few different areas. 

# Flask App
The file flask_app.py contains an API which can be used to publish events to the Kafka topic.

# Producer and Consumer
The two main pieces are the python files producer.py and consumer.py. As their names suggest, producer publishes data to a Kafka topic using the flask app, and consumer consumes data from a Kafka topic and pushes it to the postgres database. consumer.py is a consumer function which is controlled by main.py, which tells it the location of the Kafka server and the desired topic. Both of these .py files use the helper functions directory, which contains miscellaneous python helper functions.

# SQL
The sql directory contains a few relevant .sql files used by the producer and consumer, mainly for creating tables and inserting data when needed.

# Sample Records
The sample_records directory contains a json file with sample records for multiple tables. These sample records are what is published to the Kafka topic when producer.py is run.

## Prerequisites
-------------------
1. Ubuntu 22.04 (or the latest LTS version) [link](https://releases.ubuntu.com/jammy/)
2. Docker Desktop with WSL integration enabled. [link](https://www.docker.com/products/docker-desktop/). WSL info [here](https://docs.docker.com/desktop/wsl/).
3. DBeaver Community (or other preferred DB tool) [link](https://dbeaver.io/download/)

## Setup
-------------------
1. Run `kafka_setup.sh` with the following command: `./kafka_setup.sh`

This will pull the Docker image, start a container using the image, install Apache Kafka, install the required Python libraries, start zookeeper, a requirement for running Kafka, start a Kafka server, create a Kafka topic, start the flask app containing the API, and start the consumer.

2. Run `producer.py` with the following command: `python3 producer.py`

This publish the sample data found in `sample_records.sample_data.json` to the Kafka topic using the flask app. The consumer will then load the data into the postgres instance.

## Errors
----------------------
If the error `bash: ./file_name.sh: Permission denied` is encountered, run `chmod +x file_name.sh` to grant execute permission on the file.