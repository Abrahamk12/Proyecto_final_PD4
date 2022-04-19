from pprint import pprint
from datetime import datetime
import os

registro = {}

def incio(usuario:str)->None:
    now = datetime.now()
    registro[usuario] = {"fecha y hora de inicio de sesion": now}

def adios(usuario:str)->None:
    now = datetime.now()
    registro[usuario] = {"fecha y hora de fin de ls sesion": now}
