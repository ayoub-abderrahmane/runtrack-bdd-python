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
        for (id ,nom ,prenom ,salaire ,id_service) in cursor:
            print(f"ID :{id} ,NOM :{nom} ,PRENOM :{prenom} ,SALAIRE :{salaire}")

    def update(self , valeur ,id):
        cursor = mydb.cursor()
        cursor.execute("""
                UPDATE employe
                SET nom = %s
                WHERE id = %s     
            """ , (valeur ,id))
        mydb.commit()

    def delete(self , id):
        cursor = mydb.cursor()
        cursor.execute("""
                DELETE FROM employe
                WHERE id = %s 
                """ ,(id,))
        mydb.commit()

test = employe()
# test.create("Reus" ,"Marco" ,5400)
# test.update('boingz' ,4)
# test.read()
test.delete(6)


mydb.close()