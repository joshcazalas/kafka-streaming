import psycopg2

# Move the fact tables over into the Kafka ingestion schema for use later
def copy_fact_tables(connection, source_schema, target_schema):
    cursor = connection.cursor()
    fact_tables = ['arrest_type','complaint_action','crime_type','gender','incident_type','race','rank']
    for table in fact_tables:
        cursor.execute(f"create table {target_schema}.{table} as select * from {source_schema}.{table};")

# Wipe the kafka ingestion schema when needed
def reset_kafka_staging_area(connection, schema):
    cursor = connection.cursor()
    cursor.execute(f"drop schema if exists {schema} cascade;")

# Create or recreate the schema and provided list of tables
def create_schema_and_tables(connection, tables, source_schema, target_schema):
    cursor = connection.cursor()
    print(f"Creating new schema {target_schema}...")
    cursor.execute(f"create schema {target_schema};")
    print(f"{target_schema} successfully created.")

    for table in tables:
        print(f"Cloning table {source_schema}.{table} to {target_schema}.{table}...")
        cursor.execute(f"create table {target_schema}.{table} as select * from {source_schema}.{table} with no data;")
        print(f"{target_schema}.{table} successfuly created.")

# Drop and recreate the entire kafka staging area for testing
def create_kafka_staging_area(connection, tables, source_schema, target_schema):
    try:
        print("Resetting Kafka staging area...")
        reset_kafka_staging_area(connection, target_schema)
        print("Kafka staging area successfully reset.")

        print("Creating Kafka staging area...")
        create_schema_and_tables(connection, tables, source_schema, target_schema)
        copy_fact_tables(connection, source_schema, target_schema)
        print('Kafka staging area successfully created.')


    except psycopg2.Error as e:
        print(f"Error: {e}")
