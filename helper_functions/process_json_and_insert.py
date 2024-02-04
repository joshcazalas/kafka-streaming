import psycopg2

def insert_into_table(connection, table_name, data):
    cursor = connection.cursor()
    for entry in data:
        columns = ', '.join([f'"{column}"' if column.lower() == 'primary' else column for column in entry.keys()])
        values = ', '.join([f"NULL" if value is None else f"'{value}'" if isinstance(value, str) else str(value) for value in entry.values()])
        insert_query = f"insert into postgres.kafka.{table_name} ({columns}) values ({values});"
        print(insert_query)
        try:
            cursor.execute(insert_query)
            connection.commit()
        except psycopg2.Error as e:
            print(f"Error: {e}")