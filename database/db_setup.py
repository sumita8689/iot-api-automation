from database.db_connection import create_connection

def setup_database():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, title TEXT, price INTEGER)')
    cursor.execute('INSERT OR REPLACE INTO products (id,title,price) VALUES (1, "Essence Mascara Lash Princess", 9.99)')
    connection.commit()
    connection.close()

if __name__ == "__main__":
    setup_database()