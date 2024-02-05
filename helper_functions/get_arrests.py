import psycopg2

def get_arrests_count(connection):
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT COUNT(*) AS count FROM postgres.kafka.arrests;")
        result = cursor.fetchone()
        
        if result:
            total_arrests = result[0]
            return total_arrests
        else:
            return 0

    except psycopg2.Error as e:
        print(f"Error: {e}")
        return 0