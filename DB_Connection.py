import mysql.connector

def db_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password@123",
        database="my_python_db"
    )
