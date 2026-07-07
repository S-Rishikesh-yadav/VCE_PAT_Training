import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rishi@9347",
        database="pythoncompanydb"
    )
    return connection