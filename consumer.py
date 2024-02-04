from helper_functions.format_time import format_processing_time
from helper_functions.process_json_and_insert import insert_into_table
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
                    decoded_msg = json.loads(msg.value.decode('utf-8'))
                    start_time = time.time()  # Record start time
                    for table_name, table_data in decoded_msg.items():
                        insert_into_table(connection, table_name, table_data)
                    end_time = time.time()  # Record end time
                    elapsed_time = end_time - start_time
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
