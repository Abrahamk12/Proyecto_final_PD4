import csv
from passlib.hash import sha256_crypt
from __future__ import print_function
from datetime import date, datetime, timedelta
from mysql.connector import errorcode
    
#'''
class Usuarios():
    def __init__(self,id,user,pasword):
        self.id = id
        self.user = user
        self.pasword = pasword

def conectarse()->None:
    try:
        cnx = mysql.connector.connect(user='root',
                                        database='prueba_bd')
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            cnx.close()

def save_user(nombre:str, user_name:str, password:str, direccion:str, celular:int)->None:
    cnx = mysql.connector.connect(user='root', database='prueba_bd')
    cursor = cnx.cursor()
    add_user = ("INSERT INTO usuarios "
               "(nombre_completo, user_name, password, direccion, celular) "
               "VALUES (%s, %s, %s, %s, %i)")
    
    data_user = (nombre, user_name, password, direccion, celular)

    cursor.execute(add_user, data_user)
    emp_no = cursor.lastrowid