import psycopg2

def insert_into_table(connection, data):
    cursor = connection.cursor()

    # Extract table_name from data
    table_name = data.get('table_name')

    if not table_name:
        print("Error: Missing table_name in data.")
        return

    # Remove the table_name from data
    del data['table_name']

    # Prepare the SQL query
    columns = ', '.join([f'"{column}"' if column.lower() == 'primary' else column for column in data.keys()])
    values = ', '.join([f"NULL" if value is None else f"'{value}'" if isinstance(value, str) else str(value) for value in data.values()])
    insert_query = f"insert into postgres.kafka.{table_name} ({columns}) values ({values});"
    print(insert_query)

    try:
        cursor.execute(insert_query)
        connection.commit()
    except psycopg2.Error as e:
        print(f"Error: {e}")
        