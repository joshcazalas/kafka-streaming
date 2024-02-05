# Kafka-Streaming
-------------------
This project uses Python, Bash, Docker, and Apache Kafka to create a POC for a real-time streaming solution. 

## Prerequisites
-------------------
1. Ubuntu 22.04 (or the latest LTS version) [link](https://releases.ubuntu.com/jammy/)
2. Docker Desktop with WSL integration enabled [link](https://www.docker.com/products/docker-desktop/). WSL info [here](https://docs.docker.com/desktop/wsl/).
3. DBeaver Community (or other preferred DB tool) [link](https://dbeaver.io/download/)

## Overview
------------------
The project consists of a few different components:

### Flask App
The file `flask_app.py` contains a CRUD RESTful API which can be used to publish events to the Kafka topic.

### Producer and Consumer
The main components of the kafka ingestion process are the python files `create.py`, `delete.py`, `update.py`, `get_total_arrests.py`, `get_complaints_by_officer.py`, and `get_arrests_by_crime_type.py`.

- Producer:
    - `create.py`: Posts a request to the flask app to create records in the postgres instance based on the data found in `sample_records.sample_data.txt`.

    - `update.py`: Posts a request to the flask app to create records in the postgres instance based on the edited data found in `sample_records.sample_data_edited.txt`. The records in this file are the same as those found in `sample_records.sample_data.txt`, except all timestamps are rolled back by one minute.

    - `delete.py`: Sends a request to the flask app to delete records of a given officer_id. The file is currently configured to delete records with an officer_id matching those found in `sample_records.sample_data.txt`.

- Aggregated Metrics:
    - `get_total_arrests.py`: Sends a GET request to the flask app to get the total number of arrests found in the `arrests` table. 

    - `get_complaints_by_officer.py`: Sends a GET request to the flask app to get a count of the total number of complaints per officer_id.

    - `get_arrests_by_crime_type.py`: Sends a GET request to the flask app to get a count of the total number of arrests by crime type.

### SQL
The `sql` directory contains a few relevant .sql files used by the producer and consumer, mainly for creating tables and inserting data when needed.

### Sample Records
The `sample_records` directory contains a json file with sample records for multiple tables. These sample records are what is published to the Kafka topic when `create.py` is run.

## Setup
-------------------
1. Run `kafka_setup.sh` with the following command: `./kafka_setup.sh`

This will pull the Docker image, start a container using the image, install Apache Kafka, install the required Python libraries, start zookeeper, a requirement for running Kafka, start a Kafka server, create a Kafka topic, start the flask app containing the API, and start the consumer.

2. Run one of the following three files: `python3 create.py` , `python3 delete.py` , `python3 update.py`

`create.py` will load the records found in `sample_records/sample_data.json` into the postgres instance, `delete.py` will delete records of a given arrest_id from the postgres database, and `update.py` will update all arrest records from `sample_records/sample_data.json` with slightly altered records found in `sample_records/sample_data_edited.json`

3. After loading data into the instance, run `python3 get_total_arrests.py`, `python3 get_complaints_by_officer.py`, or `python3 get_arrests_by_crime_type.py` to view aggregated metrics.

## Errors
----------------------
If the error `bash: ./file_name.sh: Permission denied` is encountered, run `chmod +x file_name.sh` to grant execute permission on the file.

## Alternate Methods
----------------------
For an alternate method to this POC that takes advantage of cloud services, see these AWS [Docs](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-dynamo-db.html).
Pairing a fleshed out version of this POC provided by AWS with Terraform for automating the deployments would create a more robust, time-efficient, and scalable version of this repository.