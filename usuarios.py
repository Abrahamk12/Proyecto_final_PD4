from passlib.hash import sha256_crypt
from login import *

def conectarse():
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                 r'DBQ=C:\Users\super\Documents\Sexto_Semestre\Proyecto_final_PD4\BD\bd.accdb;'
    conn = pyodbc.connect(con_string)
    cursor = conn.cursor()
    return cursor

def save_user(nombre:str, user_name:str, password:str, direccion:str, celular:int)->None:
    conexion = conectarse()
    escogertabla = "usuario"
    #'''
    myuser =( (nombre, user_name, password, direccion, celular), )
    conexion.executemany('INSERT INTO {} VALUES (?,?,?,?,?)'.format(escogertabla), myuser)
    #'''
    conexion.commit()
    conexion.close()

def save_t_user(nombre:str, user_name:str, password:str, roll:str)->None:
    conexion = conectarse()
    escogertabla = "t_usuario"
    myuser =( (id, nombre, user_name, password, roll,), )
    conexion.executemany('INSERT INTO {} VALUES (?,?,?,?)'.format(escogertabla), myuser)
    conexion.commit()
    conexion.close()

#Referencia de los get: https://parzibyte.me/blog/2021/03/29/flask-mysql-ejemplo-conexion-crud/
def get_password(user_name:str)->str:
    conexion = conectarse()
    pas = conexion.execute('SELECT passwrod FROM usuario WHERE usuario = ' + "'" + user_name + "';")
    conexion.close()
    return pas

def get_t_password(user_name:str)->str:
    conexion = conectarse()
    password = conexion.execute('SELECT password FROM usuarios WHERE user_name = ' + "'" + user_name + "';")
    conexion.close()
    return password 

def get_usuario(user_name:str)->str:
    conexion = conectarse()
    usuario = conexion.execute('SELECT user_name FROM usuarios WHERE user_name = ' + "'" + user_name + "';")
    conexion.close()
    return usuario

def get_t_usuario(user_name:str)->str:
    conexion = conectarse()
    usuario = conexion.execute('SELECT user_name FROM t_usuarios WHERE user_name = ' + "'" + user_name + "';")
    conexion.close()
    return usuario

def get_roll(user_name:str)->str:
    conexion = conectarse()
    roll = conexion.execute('SELECT roll FROM t_usuarios WHERE user_name = ' + "'" + user_name + "';")
    conexion.close()
    return roll

def actualizar_password(user_name:str, password: str)->str:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    conexion = conexion.execute('UPDATE usuarios SET password =' + "'" + password_cryp + "'" + ' WHERE user_name = ' + "'" + user_name + "';")
    conexion.close()

def actualizar_t_password(user_name:str, password: str)->str:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    conexion.execute('UPDATE t_usuarios SET password =' + "'" + password_cryp + "'" + 'WHERE user_name = ' + "'" + user_name + "';")
    conexion.close()

def comprobar_usuario(user_name)->list:
    conexion = conectarse()
    us = conexion.execute('SELECT * FROM usuario;')
    return us

def comprobar_tusuario()->list:
    conexion = conectarse()
    c_usuario = conexion.execute('SELECT user_name FROM usuarios;')
    conexion.close()
    return c_usuario
