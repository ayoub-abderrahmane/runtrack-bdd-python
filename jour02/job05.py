import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "LaPlateforme"
)

cursor = mydb.cursor()

cursor.execute(
    "SELECT superficie FROM etage"
    )


result = cursor.fetchall()
print(result)
total_result = 0
for superficie in result:
    total_result += superficie[0]
print("La superficie de LaPlateforme est de" ,total_result ,"m2")

mydb.close()
cursor.close()