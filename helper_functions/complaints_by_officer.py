import psycopg2

def complaints_by_officer(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("select officer_id, count(complaints.officer_id) as num_complaints from postgres.kafka.officer left join postgres.kafka.complaints on officer.id = complaints.officer_id group by officer_id;")
        result = cursor.fetchall()
        
        if result:
            return result
        else:
            return 0

    except psycopg2.Error as e:
        print(f"Error: {e}")
        return 0