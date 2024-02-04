import psycopg2

def reset_kafka_staging_area(connection, schema):
    cursor = connection.cursor()
    cursor.execute(f"drop schema if exists {schema} cascade;")

def create_schema_and_tables(connection, tables, source_schema, target_schema):
    cursor = connection.cursor()
    print(f"Creating new schema {target_schema}...")
    cursor.execute(f"create schema {target_schema};")
    print(f"{target_schema} successfully created.")

    for table in tables:
        print(f"Cloning table {source_schema}.{table} to {target_schema}.{table}...")
        cursor.execute(f"create table {target_schema}.{table} as select * from {source_schema}.{table} with no data;")
        print(f"{target_schema}.{table} successfuly created.")

def create_kafka_staging_area(connection, tables, source_schema, target_schema):
    try:
        print("Resetting Kafka staging area...")
        reset_kafka_staging_area(connection, target_schema)
        print("Kafka staging area successfully reset.")

        print("Creating Kafka staging area...")
        create_schema_and_tables(connection, tables, source_schema, target_schema)
        print('Kafka staging area successfully created.')

    except psycopg2.Error as e:
        print(f"Error: {e}")
