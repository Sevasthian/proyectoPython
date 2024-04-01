import requests
from colorama import init, Fore, Style
import time
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.GREEN + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
def BuscarIDdeZonas(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/zonas/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("LA ZONA NO EXITE:")
        return []     
def BuscarZonas():
    idZonas = input("Ingrese el id de la zona : ")
    list = []
    for sev in BuscarIDdeZonas(idZonas):
        getAllAc={

                "Nombre de la Zona": sev.get('nombreZona'),
                "Coddigo Campus": sev.get('totalCapacidad'),
                "ID": sev.get('id')
          }
        list.append(getAllAc)
    return list

