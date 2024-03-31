import re
import requests
import json
from colorama import init, Fore, Style
import time
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.YELLOW + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
def DataZonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/zonas/")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", str(e))
        return []  

def BuscarNombreZonas(Nombre):
    for val in DataZonas():
        if val.get("nombreZona")  == Nombre:
            return [val]



def AddZona():
    Zona = {}
    while True:
        try:     
            if not Zona.get("nombreZona"):
                nombre = input("Ingrese el nombre de la zona: ")
                if re.match(r'^[A-Z]', nombre) is not None:
                    if BuscarNombreZonas(nombre):
                        raise Exception("El nombre de la zona ingresado ya existe.")
                    else:
                        Zona["nombreZona"] = nombre
                else:
                    raise Exception("Nombre no valido, recuerde que los nombres inician con mayuculas")
                
            if not Zona.get("totalCapacidad"):
                capacidad = input("Ingrese la capacidad de la zona: ")
                if re.match(r'^\d+$', capacidad) is not None:
                    Zona["totalCapacidad"] = capacidad
                    break
                else:
                    raise Exception("La capacidad de la zona solo se registran números")
                                   
        except Exception as error:
            animateTextDeLosMenus(str(error))
    peticion = requests.post("http://154.38.171.54:5502/zonas/", data=json.dumps(Zona, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Zona Guardada"
    return [res]