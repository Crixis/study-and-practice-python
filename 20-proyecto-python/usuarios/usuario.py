from colorama import Cursor
import mysql.connector
import datetime

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="proyecto_python",
    port=3306
)

cursor=database.cursor(buffered=True)

class Usuario:

    def __init__(self, nombre, apellidos, email, contra):
        self.nombre=nombre
        self.apellidos=apellidos
        self.email=email
        self.contra=contra
    
    def registrar(self):
        fecha=datetime.datetime.now

        sql="INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario=(self.nombre, self.apellidos, self.email, self.contra, fecha)

        cursor.execute(sql, usuario)
        database.commit()

        return[cursor.rowcount, self]

    def identificar(self):
        return self.nombre
