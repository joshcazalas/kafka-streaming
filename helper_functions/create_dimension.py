import psycopg2

def create_dimension(connection, dimension):
    cursor = connection.cursor()
    with open('sql/{dimension}_dimension.sql', 'r') as file:
        query = f"create table postgres.kafka.{dimension}_dimension as {file}"
        cursor.execute(file)
