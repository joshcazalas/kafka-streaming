import psycopg2

def delete_from_table(connection, data):
    cursor = connection.cursor()

    # Extract table_name from data
    table_name = data.get('table_name')

    if not table_name:
        print("Error: Missing table_name in data.")
        return

    # Prepare the SQL query
    record_id = data.get('id')
    delete_query = f"delete from postgres.kafka.{table_name} where id = {record_id};"
    print(delete_query)

    try:
        cursor.execute(delete_query)
        connection.commit()
    except psycopg2.Error as e:
        print(f"Error: {e}")