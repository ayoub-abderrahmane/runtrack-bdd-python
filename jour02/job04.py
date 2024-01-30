import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "LaPlateforme"
)

cursor = mydb.cursor()

cursor.execute(
    "SELECT nom ,capacite FROM salle")

result = cursor.fetchall()

print(result)

mydb.close()
cursor.close()