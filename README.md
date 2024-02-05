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
2. Docker Desktop with WSL integration enabled [link](https://www.docker.com/products/docker-desktop/). WSL info [here](https://docs.docker.com/desktop/wsl/).
3. DBeaver Community (or other preferred DB tool) [link](https://dbeaver.io/download/)

## Setup
-------------------
1. Run `kafka_setup.sh` with the following command: `./kafka_setup.sh`

This will pull the Docker image, start a container using the image, install Apache Kafka, install the required Python libraries, start zookeeper, a requirement for running Kafka, start a Kafka server, create a Kafka topic, start the flask app containing the API, and start the consumer.

2. Run one of the following three files: `python3 create.py` , `python3 delete.py` , `python3 update.py`

create.py will load the records found in sample_records/sample_data.json into the postgres instance, delete.py will delete records of a given arrest_id from the postgres database, and update.py will update all arrest records from sample_records/sample_data.json with slightly altered records found in sample_records/sample_data_edited.json

## Errors
----------------------
If the error `bash: ./file_name.sh: Permission denied` is encountered, run `chmod +x file_name.sh` to grant execute permission on the file.

## Alternate Methods
----------------------
For an alternate method to this POC that takes advantage of cloud services, see these AWS [Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html)
Pairing a fleshed out version of this POC with Terraform would create the most seamless version of this product.