def generate_random_json_data(connection, source_schema):
    cursor = connection.cursor()
    cursor.execute(f"select table_name from information_schema.tables where table_schema = '{source_schema}' and (select count(*) from information_schema.columns where table_schema = '{source_schema}' and table_name = information_schema.tables.table_name) > 2;")
    tables = [row[0] for row in cursor.fetchall()]
    
    json_data = {}

    cursor.execute(f"select id from {source_schema}.officer limit 1;")
    officer_id = cursor.fetchone()[0]
    print("officer_id")
    print(officer_id)

    for table in tables:
        
        cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = '{table}' AND column_name = 'officer_id');")
        column_result = cursor.fetchone()[0]
        print(f"{table} has column")
        print(column_result)

        random_record = None

        if officer_id and column_result:
            print(f"this is a table with officer_id column. officer id is {officer_id}")
            cursor.execute(f"select * from {source_schema}.{table} where officer_id = '246137';")
            record = cursor.fetchone()
            if record:
                random_record = record[0]
                print("random record")
                print(random_record)
        else:
            cursor.execute(f"select * from {source_schema}.{table} tablesample system(80) limit 1;")
            random_record = cursor.fetchone()[0]
        

        if random_record:
            columns = [desc[0] for desc in cursor.description]
            if table not in json_data:
                json_data[table] = []
            try: 
                # Explicitly specify the order of keys to ensure correct mapping
                record_dict = {col: random_record[columns.index(col)] for col in columns}
                json_data[table].append(record_dict)
            except IndexError as e:
                print(f"Error: {e}")
                print(f"Table: {table}")
                print(f"Columns: {columns}")
                print(f"Record: {random_record}")
                print("---")

    return json_data
