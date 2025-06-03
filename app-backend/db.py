import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="ff",
        password="1234",
        database="ludoteca"
    )