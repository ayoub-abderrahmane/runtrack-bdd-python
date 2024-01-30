import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "LaPlateforme"
)

cursor = mydb.cursor()

cursor.execute(
    "SELECT capacite FROM salle")

result = cursor.fetchall()
total_capa = 0
for capa in result:
    total_capa += capa[0]

print ("La capacité totale de toutes les salles est de :" ,total_capa)

mydb.close()
cursor.close()