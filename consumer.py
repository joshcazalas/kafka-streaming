import time
import json
from helper_functions.insert import insert_into_table
from helper_functions.delete import delete_from_table
from helper_functions.update import update_record
from helper_functions.create_dimension import create_dimension

running = True

def consume_kafka_message(consumer, postgres_connection ,topics):
    consumer.subscribe(topics)

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
                    print(f"Decoded Message: {decoded_msg}")

                    # Record start time
                    start_time = time.time()

                    table_data = decoded_msg.copy()
                    event_type = table_data.get('event_type', 'unknown')

                    # Check the event type and perform actions accordingly
                    if event_type == 'create':
                        print("Performing create operation...")
                        if 'table_name' in decoded_msg:
                            insert_into_table(postgres_connection, table_data)
                        else:
                            print(f"Missing 'table_name' in message: {decoded_msg}")
                    elif event_type == 'delete':
                        print("Performing delete operation...")
                        if 'table_name' in decoded_msg:
                            delete_from_table(postgres_connection, table_data)
                        else:
                            print(f"Missing 'table_name' in message: {decoded_msg}")
                    elif event_type == 'update':
                        print("Performing delete operation...")
                        if 'table_name' in decoded_msg:
                            update_record(postgres_connection, table_data)
                        else:
                            print(f"Missing 'table_name' in message: {decoded_msg}")
                    else:
                        print(f"Unknown event type: {event_type}")

                    # Record end time
                    end_time = time.time()

                    # Calculate elapsed time
                    elapsed_time = end_time - start_time

                    # Recreate the officer and arrest dimensions
                    create_dimension(postgres_connection, 'arrest')
                    create_dimension(postgres_connection, 'officer')
                    print("Dimensions Updated.")
                    print(f"Processing time: {elapsed_time} seconds")
                    
            consumer.commit()

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        postgres_connection.close()