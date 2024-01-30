import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "entreprise"
)

cursor = mydb.cursor()

cursor.execute(
    "SELECT * FROM employe WHERE salaire > 3000")

result = cursor.fetchall()

print(result)

mydb.close()
cursor.close()