from colorama import init, Fore, Style
import time
from tabulate import tabulate
import requests
import json
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.YELLOW + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
def BuscarIDdeZonas(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/zonas/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", e)
        return []  


def updateZonas(id):
    data = BuscarIDdeZonas(id)
    if data is None:
            animateTextDeLosMenus(f"""

Id del Zonas no encontrado. """)
    
    while True:
        try:
            animateTextDeLosMenus(f"""
Datos para modificar: """)
            for i, (val, sev) in enumerate(data[0].items()):
                animateTextDeLosMenus(f"{i+1}. {val}")

            opcion = int(input(f"""
Seleccione una opción: """))
            datoModificar = list(data[0].keys())[opcion - 1]
            nuevoValor = input(f"""
Ingrese el nuevo valor para {datoModificar}: """)
            if datoModificar in data[0]:
                if datoModificar == "totalCapacidad":
                    data[0][datoModificar] = int(nuevoValor)
                    break
                else:
                    data[0][datoModificar] = nuevoValor
                    break
            else:
                 animateTextDeLosMenus(f"""
Seleccion incorrecta""")
                
        except ValueError as error:
            animateTextDeLosMenus(error)
    
    peticion = requests.put(f"http://154.38.171.54:5502/zonas/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Zona Modificada"
    return [res]
            