import csv
from passlib.hash import sha256_crypt
from Levenshtein import distance
#'''
class Usuarios():
    def __init__(self,id,user,pasword):
        self.id = id
        self.user = user
        self.pasword = pasword
    
    #def __str__(self):
    #    return f'{self.user} - {self.pasword}'

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

def id_sum(archivo:str)->int:
    #Lee un archivo CSV y regresa un diccionario de diccionarios
    id_p = 0
    try:
        with open(archivo,'r',encoding='utf-8') as fh:
            csv_reader = csv.DictReader(fh)
            for renglon in csv_reader:
                llave = renglon['id']
                id_p=llave
            id_p += 1
    except IOError:
        print(f"No se pudo leer el archivo {archivo}")
    return id_p

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

def cambiar_clave(diccionario:dict,llave_dict:str,archivo:str)->None:
    #Configuralo para modificar la contraseña
    print()