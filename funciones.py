import csv
from passlib.hash import sha256_crypt
import pymysql
    
#'''
class Usuarios():
    def __init__(self,id,user,pasword):
        self.id = id
        self.user = user
        self.pasword = pasword

def conectarse()->None:
    return pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='2117',
                                db='prueba_bd')

def save_user(nombre:str, user_name:str, password:str, direccion:str, celular:int)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(nombre_completo, user_name, password, direccion, celular) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, user_name, password, direccion, celular))
    conexion.commit()
    conexion.close()