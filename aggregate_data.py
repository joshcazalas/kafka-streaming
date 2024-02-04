import psycopg2

def aggregate_officer_data(connection, source_schema, target_schema):
    cursor = connection.cursor()
    cursor.execute(f"create schema if not exists {schema};")