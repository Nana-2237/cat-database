# database.py
import mysql.connector
from mysql.connector import Error

def get_connection():
    return mysql.connector.connect(
        host="db",  # 'db' refers to your Docker container name in docker-compose
        user="root",
        password="mariucaa",
        database="pisic"
    )

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        CREATE TABLE IF NOT EXISTS rase_pisici (
            CatID INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            Breed VARCHAR(255),
            Age INT,
            Gender ENUM('Male', 'Female')
        )
    """
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
