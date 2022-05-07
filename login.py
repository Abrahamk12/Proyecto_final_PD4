from datetime import datetime
import pyodbc
import os

registro = {}

def conectarse():
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                 r'DBQ=C:\Users\josel\Desktop\Database2.accdb;'
    conn = pyodbc.connect(con_string)
    cursor = conn.cursor()
    return cursor

def incio(usuario:str)->None:
    now = datetime.now()
    registro[usuario] = {"fecha y hora de inicio de sesion": now}
