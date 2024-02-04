import psycopg2

def create_dimension(connection, dimension):
    cursor = connection.cursor()
    try:
        with open(f'sql/{dimension}_dimension.sql', 'r') as file:
            file_contents = file.read()
            query = f"create table postgres.kafka.{dimension}_dimension as {file_contents}"
            cursor.execute(query)
    except psycopg2.Error as e:
            print(f"Error: {e}")
