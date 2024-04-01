import requests
from colorama import init, Fore, Style
import time
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.GREEN + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
def BuscarIDdePersonal(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("EL PERSONAL NO EXITE")
        return []     
def BuscarPersonal():
    idPersonal = input("Ingrese el id del activo : ")
    data = BuscarIDdePersonal(idPersonal)
    list = []
    for sev in data:
        getAllAc={

                "Numero de IDENTIDAD": sev.get('nroId (CC, Nit)'),
                "Nombre": sev.get('Nombre'),
                "Email": sev.get('Email'),
                "Telefonos": sev.get('Telefonos')
          }
        list.append(getAllAc)
    return list
