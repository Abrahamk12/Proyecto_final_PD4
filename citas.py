import pymysql
from login import conectarse

def save_cita(user_name:str, fecha:str, motivo:str, c_mascotas:int)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(user_name, fecha, motivo, c_mascotas) VALUES (%s, %s, %s, %i)",
                       (user_name, fecha, motivo, c_mascotas))
    conexion.commit()
    conexion.close()