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

def save_t_user(nombre:str, user_name:str, password:str, roll:str)->None:
    conexion = conectarse()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO t_usuarios(nombre_completo, user_name, password, roll) VALUES (%s, %s, %s, %s)",
                       (nombre, user_name, password, roll))
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
    rol = roll.__getitem__(0)
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

def comprobar_tusuario()->list:
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

def set_roll()->list:
    lr = ["administrador","trabajador","doctor"]

def l_menu(usuario:str, rol:str)->list:
    #d = diccionario, m = menu, t = trabajador, a = admin, u = usuario
    dma = {"Registrar trabajador":"/a_opciones/add_new_user_t.html",
    "Registrar usuario":"/a_opciones/usuario",
    "Cambiar contraseña usuario":'/restart_password/', 
    "Cambiar contraseña trabajador":"/a_opciones/contraseña-trabajador",
    "Ver Base de Datos":"/a_opciones/usuario/a_opciones/bd",
    "Perfil usuario":"/a_opciones/perfil_usuario.html", 
    "Cambiar contraseña":"/restart_password/"}
    
    dmt = {"Agendar cita":"/agendar_cita.", 
    "Cambiar cita":"/cambiar_cita", 
    "Ver sig cita":"/t_opciones/", 
    "Pagos":"/t_opciones/pago.html", 
    "Perfil usuario":"/t_opciones/",
    "Cancelar cita":"/t_opciones/", 
    "Cambiar contraseña":"/t_opciones/"}
     
    dmd = {"Sig cita":"", 
        "Cita actual":"",
        "Perfil paciente":"",
        "Cambiar contraseña":""}

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

