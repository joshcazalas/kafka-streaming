from flask import Flask, request, jsonify
from confluent_kafka import Producer
import json
import socket

app = Flask(__name__)

# Set up Kafka producer configuration
conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': socket.gethostname()
}

producer = Producer(conf)

@app.route('/arrests', methods=['POST'])
def create_arrest():
    data = request.json['arrests']

    # Publish each arrest event to Kafka with the table_name field
    topic = 'arrest'
    for arrest_event in data:
        arrest_event['table_name'] = 'arrests'  # Include the table_name field
        producer.produce(topic, key=str(arrest_event['id']), value=json.dumps(arrest_event))
        producer.flush()

    return jsonify({"message": "Arrest events sent to Kafka topic successfully"}), 201

@app.route('/officers', methods=['POST'])
def create_officer():
    data = request.json['officer']
    
    # Include the table_name field
    data['table_name'] = 'officer'

    # Publish the officer data to Kafka
    topic = 'officer'
    producer.produce(topic, key=str(data['id']), value=json.dumps(data))
    producer.flush()

    return jsonify({"message": "Officer data sent to Kafka topic successfully"}), 201

@app.route('/complaints', methods=['POST'])
def create_complaint():
    data = request.json['complaints']

    # Include the table_name field for each complaint event
    for complaint_event in data:
        complaint_event['table_name'] = 'complaint'

    # Publish each complaint event to Kafka
    topic = 'complaint'
    for complaint_event in data:
        producer.produce(topic, key=str(complaint_event['id']), value=json.dumps(complaint_event))
        producer.flush()

    return jsonify({"message": "Complaint events sent to Kafka topic successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)
