import psycopg2

def update_record(connection, data):
    cursor = connection.cursor()

    # Extract table_name from data
    table_name = data.get('table_name')

    if not table_name:
        print("Error: Missing table_name in data.")
        return

    # Remove the table_name from data
    del data['table_name']
    del data['event_type']

    # Prepare the SQL query
    set_values = ', '.join([f'"{column}" = ' + (f"NULL" if value is None else f"'{value}'" if isinstance(value, str) else str(value)) for column, value in data.items()])
    where_condition = f'id = {data["id"]}'

    update_query = f"UPDATE postgres.kafka.{table_name} SET {set_values} WHERE {where_condition};"
    print(update_query)

    try:
        cursor.execute(update_query)
        connection.commit()
    except psycopg2.Error as e:
        print(f"Error: {e}")
        