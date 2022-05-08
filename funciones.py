from passlib.hash import sha256_crypt
import pyodbc
import os

#'''
class Usuarios():
    def __init__(self,id,user,pasword):
        self.id = id
        self.user = user
        self.pasword = pasword

def conectarse():
    DRIVER_NAME = "Microsoft Access Driver (*.mdb, *.accdb)"
    DB_PATH  = os.getcwd() + "/PFDBD/D.accdb"
    conn = pyodbc.connect("Driver={%s};DBQ=%s;" % (DRIVER_NAME, DB_PATH))
    cursor = conn.cursor()
    return cursor

def save_user(nombre:str, user_name:str, password:str, direccion:str, celular:str)->None:
    conexion = conectarse()
    escogertabla = "usuario"
    #'''
    myuser =( (nombre, user_name, password, direccion, celular), )
    conexion.executemany('INSERT INTO {} VALUES (?,?,?,?,?)'.format(escogertabla), myuser)
    #'''
    conexion.commit()

def save_t_user(nombre:str, user_name:str, password:str, roll:str)->None:
    conexion = conectarse()
    escogertabla = "t_usuario"
    myuser =( (id, nombre, user_name, password, roll,), )
    conexion.executemany('INSERT INTO {} VALUES (?,?,?,?)'.format(escogertabla), myuser)
    conexion.commit()

#Referencia de los get: https://parzibyte.me/blog/2021/03/29/flask-mysql-ejemplo-conexion-crud/
def get_password(user_name:str)->str:
    conexion = conectarse()
    conexion.execute('SELECT password FROM usuario WHERE user_name = ' + "'" + user_name + "';")
    for row in conexion.fetchone():
        password = row
    return password

def get_t_password(user_name:str)->str:
    conexion = conectarse()
    conexion.execute('SELECT password FROM usuarios WHERE user_name = ' + "'" + user_name + "';")
    for row in conexion.fetchone():
        password = row
    return password

def get_usuario(user_name:str)->str:
    conexion = conectarse()
    conexion.execute('SELECT user_name FROM usuario WHERE user_name = ' + "'" + user_name + "';")
    for row in conexion.fetchone():
        usuario = row
    return usuario

def get_t_usuario(user_name:str)->str:
    conexion = conectarse()
    conexion.execute('SELECT user_name FROM t_usuarios WHERE user_name = ' + "'" + user_name + "';")
    for row in conexion.fetchone():
        usuario = row
    return usuario

def get_roll(user_name:str)->str:
    conexion = conectarse()
    conexion.execute('SELECT roll FROM t_usuarios WHERE user_name = ' + "'" + user_name + "';")
    for row in conexion.fetchone():
        roll = row
    return roll

def get_historial(user_name)->dict:
    li = []
    l = []
    lis = {"user_name","doctor","diagnostico","receta","fecha"}
    i = 0
    conexion = conectarse()
    conexion.execute('SELECT * FROM citas_atendidas WHERE user_name = ' + "'" + user_name + "';")
    for row in conexion.fetchall():
        print(row)
        li.append(row)
        print("\Coño ",li.__getitem__(i))
        l = li.__getitem__(i)
        li = {"user_name":l.__getitem__(0),"doctor":l.__getitem__(1),"diagnostico":l.__getitem__(2),
        "receta":l.__getitem__(3),"fecha":l.__getitem__(4)}
        i += 1
    print(lis)
    return lis

def actualizar_password(user_name:str, password: str)->str:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    conexion = conexion.execute('UPDATE usuarios SET password =' + "'" + password_cryp + "'" + ' WHERE user_name = ' + "'" + user_name + "';")

def actualizar_t_password(user_name:str, password: str)->str:
    password_cryp = sha256_crypt.hash(password)
    conexion = conectarse()
    conexion.execute('UPDATE t_usuarios SET password =' + "'" + password_cryp + "'" + 'WHERE user_name = ' + "'" + user_name + "';")

def comprobar_usuario(usuario:str)->str:
    conexion = conectarse()
    conexion.execute('SELECT user_name FROM usuario WHERE user_name = ' + "'" + usuario + "';")
    for row in conexion.fetchone():
        u = row
        print("\n",u,"\n")
    return u

def comprobar_tusuario()->list:
    u = []
    conexion = conectarse()
    c_usuario = conexion.execute('SELECT user_name FROM usuarios;')
    for row in conexion.fetchone():
        u.append(row)
    return c_usuario

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

def save_cita(user_name:str, fecha:str, hora:str, motivo:str, c_mascotas:str)->None:
    conexion = conectarse()
    escogertabla = "citas"
    myuser =( (user_name, fecha, hora, motivo, c_mascotas), )
    conexion.executemany('INSERT INTO {} VALUES (?,?,?,?,?)'.format(escogertabla), myuser)
    conexion.commit()

def cambiar_cita(fecha:str, hora:str)->None:
    conexion = conectarse()
    conexion.execut('UPDATE citas SET fecha = {%s}, hora = {%s};'%(fecha, hora))
    conexion.commit()
'''
comprobar_usuario("P")
#'''