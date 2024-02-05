import psycopg2

def create_dimension(connection, dimension):
    cursor = connection.cursor()
    try:
        cursor.execute("create schema if not exists reporting")
        with open(f'sql/{dimension}_dimension_create.sql', 'r') as file:
            file_contents = file.read()
            cursor.execute(file_contents)
        with open(f'sql/{dimension}_dimension.sql', 'r') as file:
            file_contents = file.read()
            query = f"insert into postgres.reporting.{dimension}_dimension {file_contents}"
            cursor.execute(query)
    except psycopg2.Error as e:
            print(f"Error: {e}")
