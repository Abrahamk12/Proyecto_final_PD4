import pymysql
from passlib.hash import sha256_crypt
from login import *

def save_user(nombre:str, user_name:str, password:str, direccion:str, celular:int)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(nombre_completo, user_name, password, direccion, celular) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, user_name, password, direccion, celular))
    conexion.commit()
    conexion.close()

def save_t_user(nombre:str, user_name:str, password:str, roll:str)->None:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO t_usuarios(nombre_completo, user_name, password, roll) VALUES (%s, %s, %s, %s)",
                       (nombre, user_name, password_cryp, roll))
    conexion.commit()
    conexion.close()

#Referencia de los get: https://parzibyte.me/blog/2021/03/29/flask-mysql-ejemplo-conexion-crud/
def get_password(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        password = cursor.execute("SELECT password FROM usuarios WHERE user_name = " + '"' + user_name + '"')
        password = cursor.fetchone()
    conexion.close() 
    for i in range(len(password)):
        pas = password.__getitem__(i)
    return pas 

def get_t_password(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        password = cursor.execute("SELECT password FROM usuarios WHERE user_name = " + '"' + user_name + '"')
    conexion.close()
    for i in range(len(password)):
        pas = password.__getitem__(i)
    return pas 

def get_usuario(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute("SELECT user_name FROM usuarios WHERE user_name = " + '"' + user_name + '"')
        usuario = cursor.fetchone()
    conexion.close()
    us = usuario.__getitem__(0)
    return us

def get_t_usuario(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute("SELECT user_name FROM t_usuarios WHERE user_name = " + '"' + user_name + '"')
    conexion.close()
    for i in range(len(usuario)):
        us = usuario.__getitem__(i)
    return us

def get_roll(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        roll = cursor.execute("SELECT roll FROM t_usuarios WHERE user_name = " + '"' + user_name + '"')
    conexion.close()
    for i in range(len(roll)):
        rol = roll.__getitem__(i)
    return rol

def actualizar_password(user_name:str, password: str)->str:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor = cursor.execute("UPDATE usuarios SET password =" + '"' + password_cryp + '"' + " WHERE user_name = " + '"' + user_name + '"')
    conexion.commit()
    conexion.close()

def actualizar_t_password(user_name:str, password: str)->str:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor = cursor.execute("UPDATE t_usuarios SET password =" + '"' + password_cryp + '"' + " WHERE user_name = " + '"' + user_name + '"')
    conexion.commit()
    conexion.close()

def comprobar_usuario()->list:
    c_us = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT user_name FROM usuarios")
        c_usuario = cursor.fetchall()
    conexion.close()
    for i in range(len(c_usuario)):
        us = c_usuario.__getitem__(i)
        c_us.append(us.__getitem__(0))
    return c_us

