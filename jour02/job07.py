import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "entreprise"
)





class employe():
    def __init__(self):
        pass

    def create(self ,nom ,prenom ,salaire):
        cursor = mydb.cursor()
        cursor.execute("""INSERT INTO employe (nom ,prenom ,salaire)
                       VALUES (%s ,%s ,%s)
                       """,(nom ,prenom ,salaire))
        mydb.commit()

    def read(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM employe")
        result = cursor.fetchall()
        print(result)

    def update(self ,colonne , valeur ,id):
        cursor = mydb.cursor()
        cursor.execute("""
                UPDATE employe
                SET """ colonne = valeur
                WHERE id = id     
                )
        mydb.commit()

    def delete(self , id):
        cursor = mydb.cursor()
        cursor.execute("""
                DELETE FROM employe
                WHERE id = """ ,(id))


test = employe()
# test.create("Reus" ,"Marco" ,5400)
test.delete(4)


mydb.close()