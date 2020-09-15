import mysql.connector

mydb = mysql.connector.connect(
    host="Siddharths-MacBook-Air.local",
    user="root",
    password="misraa123",
    database="sid"
)
mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
