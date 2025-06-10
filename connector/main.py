import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="mariucaa",
        database="pisic",
        port=3306
    )

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rase_pisici (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            Breed VARCHAR(100),
            Age INT,
            Gender VARCHAR(10)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
