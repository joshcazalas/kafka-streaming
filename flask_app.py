from flask import Flask, request, jsonify
from confluent_kafka import Producer
from helper_functions.get_arrests import get_arrests_count
from helper_functions.arrests_by_crime_type import arrests_by_crime_type
from helper_functions.complaints_by_officer import complaints_by_officer
import json
import socket
import psycopg2

app = Flask(__name__)

# Set up Kafka producer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': socket.gethostname()
}

producer = Producer(conf)

@app.route('/arrests/create', methods=['POST'])
def create_arrest():
    data = request.json['arrests']

    # Publish each arrest event to Kafka with the table_name field
    topic = 'arrest-topic'
    for arrest_event in data:
        arrest_event['table_name'] = 'arrests'  # Include the table_name field
        arrest_event['event_type'] = 'create'
        producer.produce(topic, key=str(arrest_event['id']), value=json.dumps(arrest_event))
        producer.flush()

    return jsonify({"message": "Arrest create event sent to Kafka topic successfully"}), 201

@app.route('/arrests/delete', methods=['DELETE'])
def delete_arrest():
    data = request.json['arrests']

    topic = 'arrest-topic'
    for arrest_event in data:
        arrest_event['event_type'] = 'delete'
        arrest_event['table_name'] = 'arrests'
        producer.produce(topic, key=str(arrest_event['id']), value=json.dumps(arrest_event))
        producer.flush()

    return jsonify({"message": f"Arrest event scheduled for deletion"}), 200

@app.route('/arrests/update', methods=['PUT'])
def update_arrest():
    data = request.json['arrests']

    topic = 'arrest-topic'
    for arrest_event in data:
        arrest_event['event_type'] = 'update'
        arrest_event['table_name'] = 'arrests'
        producer.produce(topic, key=str(arrest_event['id']), value=json.dumps(arrest_event))
        producer.flush()

    return jsonify({"message": f"Arrest event scheduled for update"}), 200


@app.route('/officers', methods=['POST'])
def create_officer():
    data = request.json['officer']

    topic = 'arrest-topic'
    for officer_event in data:
        officer_event['table_name'] = 'officer'
        officer_event['event_type'] = 'create'
        producer.produce(topic, key=str(officer_event['id']), value=json.dumps(officer_event))
        producer.flush()

    return jsonify({"message": "Officer create event sent to Kafka topic successfully"}), 201

@app.route('/complaints', methods=['POST'])
def create_complaint():
    data = request.json['complaints']

    topic = 'arrest-topic'
    for complaints_event in data:
        complaints_event['table_name'] = 'complaints'
        complaints_event['event_type'] = 'create'
        producer.produce(topic, key=str(complaints_event['id']), value=json.dumps(complaints_event))
        producer.flush()

    return jsonify({"message": "Complaints create event sent to Kafka topic successfully"}), 201

@app.route('/aggregated_metrics/total_arrests', methods=['GET'])
def get_total_arrests():
    connection = psycopg2.connect(host='localhost',
        database='postgres',
        user='postgres',
        password='admin',
        port='5520'
    )
    connection.autocommit = True
    total_arrests = get_arrests_count(connection)
    return jsonify({"total_arrests": total_arrests})

@app.route('/aggregated_metrics/arrests_by_crime_type', methods=['GET'])
def get_arrests_by_crime_type():
    connection = psycopg2.connect(host='localhost',
        database='postgres',
        user='postgres',
        password='admin',
        port='5520'
    )
    connection.autocommit = True
    num_arrests_by_crime_type = arrests_by_crime_type(connection)
    return jsonify({"arrests_by_crime_type": num_arrests_by_crime_type})

@app.route('/aggregated_metrics/complaints_by_officer', methods=['GET'])
def get_complaints_by_officer():
    connection = psycopg2.connect(host='localhost',
        database='postgres',
        user='postgres',
        password='admin',
        port='5520'
    )
    connection.autocommit = True
    num_complaints_by_officer = complaints_by_officer(connection)
    return jsonify({"complaints_by_officer": num_complaints_by_officer})

if __name__ == '__main__':
    app.run(debug=True)
