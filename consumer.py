from helper_functions.format_time import format_processing_time
from helper_functions.process_json_and_insert import insert_into_table
from helper_functions.create_dimension import create_dimension
import time
import psycopg2
import json

running = True
            
def consume_kafka_message(consumer, topics):
    consumer.subscribe(topics)

    connection = psycopg2.connect(host='localhost',
        database='postgres',
        user='postgres',
        password='admin',
        port='5520'
    )
    connection.autocommit = True
    
    try:
        while running:
            print("Polling...")
            for msg in consumer:
                if msg is None:
                    print("No message")
                    continue
                else:
                    # Load the message
                    decoded_msg = json.loads(msg.value.decode('utf-8'))
                    # Record start time
                    start_time = time.time()
                    # For each table present in the JSON, insert a record
                    for table_name, table_data in decoded_msg.items():
                        insert_into_table(connection, table_name, table_data)
                    # Record end time
                    end_time = time.time()
                    # Calculate elapsed time
                    elapsed_time = end_time - start_time
                    # Recreate the officer and arrest dimensions
                    create_dimension(connection, 'arrest')
                    create_dimension(connection, 'officer')
                    print("Dimensions Updated.")
                    print(f"Processing time: {format_processing_time(elapsed_time)}")
            consumer.commit()

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        connection.close()
