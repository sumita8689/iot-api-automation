from database.db_connection import create_connection

def fetch_all(query):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    data_dict =[]
    for rows in data:
        row_dict ={'id':rows[0],'title':rows[1],'price':rows[2]}
        data_dict.append(row_dict)
    connection.close()
    return data_dict
