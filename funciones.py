import csv
from passlib.hash import sha256_crypt
import csv
    
#'''
class Usuarios():
    def __init__(self,id,user,pasword):
        self.id = id
        self.user = user
        self.pasword = pasword

def lee_diccionario_csv(archivo:str)->list:
    #Lee un archivo CSV y regresa un diccionario de diccionarios
    diccionario = {}
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                llave = renglon['usuario']
                diccionario[llave]=renglon
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    return diccionario

def lee_archivo_csv(archivo:str)->list:
    #Lee un archivo CSV y regresa una lista de registros
    lista = []
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.reader(fh)
            for renglon in csv_reader:
                lista.append(renglon)
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    return lista

def obten_campos(diccionario:dict,llave_d:str)->list:
    lista = [llave_d]
    llaves = list(diccionario.keys())
    k = llaves[0]
    nuevo_diccionario = diccionario[k]
    lista_campos = list(nuevo_diccionario.keys())
    lista.extend(lista_campos)
    return lista

def graba_diccionario(diccionario:dict,llave_dict:str,archivo:str):
    with open(archivo,'w') as fh: #fh = file handle
        lista_campos = obten_campos(diccionario, llave_dict)
        dw = csv.DictWriter(fh,lista_campos)
        dw.writeheader()
        renglones = []
        for llave, valor_d in diccionario.items():
            d = { 'usuario':llave}
            for key, value  in valor_d.items():
                d[key] = value
            renglones.append(d)
        dw.writerows(renglones)
#'''

def cambiar_clave(usuario:str,password,archivo:str)->None:
    #Configuralo para modificar la contraseña
    diccionario = lee_diccionario_csv(archivo)
    print(diccionario)

    llave_dict_cryp = sha256_crypt.hash(password)
    diccionario.update({usuario: llave_dict_cryp})
    print("\n",diccionario)
    '''
    with open(archivo,'w') as fh: #fh = file handle
        lista_campos = obten_campos(diccionario, llave_dict)
        dw = csv.DictWriter(fh,lista_campos)
        dw.writeheader()
        renglones = []
        for llave, valor_d in diccionario.items():
            d = { 'usuario':llave}
            for key, value  in valor_d.items():
                d[key] = value
            renglones.append(d)
        dw.writerows(renglones)
    '''
    #https://code.tutsplus.com/es/tutorials/how-to-read-and-write-csv-files-in-python--cms-29907 enlace del ejemplo
    with open(archivo, 'w') as csvfile:
        fieldnames = ['usuario','password','n_competo','direccion','celular']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(diccionario)
