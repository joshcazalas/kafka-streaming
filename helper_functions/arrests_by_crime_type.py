import psycopg2

def arrests_by_crime_type(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("select crime_type.name as crime, count(*) from postgres.kafka.arrests inner join postgres.kafka.crime_type on arrests.crime_type_id = crime_type.id group by crime;")
        result = cursor.fetchall()
        
        if result:
            return result
        else:
            return 0

    except psycopg2.Error as e:
        print(f"Error: {e}")
        return 0