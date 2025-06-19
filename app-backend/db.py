import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ludoteca",
        charset='utf8mb4',
        collation='utf8mb4_unicode_ci'
    )
