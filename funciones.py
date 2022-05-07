from passlib.hash import sha256_crypt
import pyodbc
    
#'''
class Usuarios():
    def __init__(self,id,user,pasword):
        self.id = id
        self.user = user
        self.pasword = pasword

def conectarse():
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};' \
                 r'DBQ=C:\Users\super\Documents\Sexto_Semestre\Proyecto_final_PD4\BD\bd.accdb;'
    conn = pyodbc.connect(con_string)
    cursor = conn.cursor()
    return cursor

def save_user(nombre:str, user_name:str, password:str, direccion:str, celular:int)->None:
    conexion = conectarse()
    conexion.executemany("INSERT INTO usuario (nombre_completo, user_name, password, direccion, celular)"
    + "VALUES (" + "'" + nombre + "', '" + user_name + "', '" + password + "', '" + direccion + "', '" + celular +"');")
    conexion.commit()
    conexion.close()

def save_t_user(nombre:str, user_name:str, password:str, roll:str)->None:
    conexion = conectarse()
    conexion.executemany('INSERT INTO t_usuario VALUES (' + nombre + "', '" + user_name + "', '" + password + "', '" + roll + "');")
    conexion.commit()
    conexion.close()

#Referencia de los get: https://parzibyte.me/blog/2021/03/29/flask-mysql-ejemplo-conexion-crud/
def get_password(user_name:str)->str:
    conexion = conectarse()
    pas = conexion.execute('SELECT passwrod FROM usuario WHERE usuario = ' + "'" + user_name + "';")
    return pas

def get_t_password(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        password = cursor.execute('SELECT password FROM usuarios WHERE user_name = ' + "'" + user_name + "';")
    conexion.close()
    for i in range(len(password)):
        pas = password.__getitem__(i)
    return pas 

def get_usuario(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute('SELECT user_name FROM usuarios WHERE user_name = ' + "'" + user_name + "';")
        usuario = cursor.fetchone()
    conexion.close()
    us = usuario.__getitem__(0)
    return us

def get_t_usuario(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        usuario = cursor.execute('SELECT user_name FROM t_usuarios WHERE user_name = ' + "'" + user_name + "';")
    conexion.close()
    for i in range(len(usuario)):
        us = usuario.__getitem__(i)
    return us

def get_roll(user_name:str)->str:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        roll = cursor.execute('SELECT roll FROM t_usuarios WHERE user_name = ' + "'" + user_name + "';")
    conexion.close()
    rol = roll.__getitem__(0)
    return rol

def actualizar_password(user_name:str, password: str)->str:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor = cursor.execute('UPDATE usuarios SET password =' + "'" + password_cryp + "'" + ' WHERE user_name = ' + "'" + user_name + "';")
    conexion.commit()
    conexion.close()

def actualizar_t_password(user_name:str, password: str)->str:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor = cursor.execute('UPDATE t_usuarios SET password =' + "'" + password_cryp + "'" + 'WHERE user_name = ' + "'" + user_name + "';")
    conexion.commit()
    conexion.close()

def comprobar_usuario(user_name)->list:
    conexion = conectarse()
    us = conexion.execute('SELECT user_name FROM usuario WHERE usuario = ' + "'" + user_name + "';")
    return us

def comprobar_tusuario()->list:
    c_us = []
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute('SELECT user_name FROM usuarios;')
        c_usuario = cursor.fetchall()
    conexion.close()
    for i in range(len(c_usuario)):
        us = c_usuario.__getitem__(i)
        c_us.append(us.__getitem__(0))
    return c_us

def set_roll()->list:
    lr = ["administrador","trabajador","doctor"]

def l_menu(usuario:str, rol:str)->list:
    #d = diccionario, m = menu, t = trabajador, a = admin, u = usuario
    dma = {"Registrar trabajador":"/a_opciones/add_new_user_t/",
    "Registrar usuario":"/a_opciones/new_user",
    "Cambiar contraseña usuario":'/restart_password/', 
    "Cambiar contraseña trabajador":"/a_opciones/contraseña_trabajador",
    "Ver Base de Datos":"/a_opciones/bd/",
    "Perfil usuario":"/a_opciones/perfil_usuario/", 
    "Cambiar contraseña":"/restart_password/"}
    
    dmt = {"Agendar cita":"/agendar_cita/", 
    "Cambiar cita":"/cambiar_cita/", 
    "Ver sig cita":"/sig_cita/", 
    "Pagos":"/t_opciones/pago/", 
    "Perfil usuario":"/t_opciones/",
    "Cancelar cita":"/t_opciones/", 
    "Cambiar contraseña":"/t_opciones/"}
     
    dmd = {"Sig cita":"/sig_cita/", 
        "Cita actual":"/cita_actual/",
        "Perfil paciente":"/perfil_paciente/",
        "Cambiar contraseña":"contraseña_trabajador"}

    roll = get_roll(usuario)
        
    #'''
    if roll == "trabajador":
        return dmt
    if roll == "administrador":
        return dma
    if roll == "doctor":
        return dmd
    #'''

def save_cita(user_name:str, fecha:str, motivo:str, c_mascotas:int)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(user_name, fecha, motivo, c_mascotas) VALUES (%s, %s, %s, %i)",
                       (user_name, fecha, motivo, c_mascotas))
    conexion.commit()
    conexion.close()

