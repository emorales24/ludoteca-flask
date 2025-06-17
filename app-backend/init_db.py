import mysql.connector

with open("init_db.sql", encoding="utf-8") as f:
    sql = f.read()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    charset='utf8mb4',
)

cursor = conn.cursor()
cursor.execute("SET NAMES utf8mb4;")
for statement in sql.split(";"):
    if statement.strip():
        print(statement)
        cursor.execute(statement)
        conn.commit()
        print("Statement executed")

cursor.close()
conn.close()
