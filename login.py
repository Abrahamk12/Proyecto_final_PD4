from datetime import datetime
import pyodbc
import os

registro = {}

def conectarse():
    DRIVER_NAME = "Microsoft Access Driver (*.mdb, *.accdb)"
    DB_PATH  = os.getcwd() + "/PFDBD/D.accdb"
    conn = pyodbc.connect("Driver={%s};DBQ=%s;" % (DRIVER_NAME, DB_PATH))
    cursor = conn.cursor()
    return cursor

def incio(usuario:str)->None:
    now = datetime.now()
    registro[usuario] = {"fecha y hora de inicio de sesion": now}
