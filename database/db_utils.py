from database.db_connection import create_connection

def fetch_all(query):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    connection.close()
    return data
