import requests
from colorama import init, Fore, Style
import time

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



def DeletePersonal(id):
    data = BuscarIDdeZonas(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5502/zonas/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Zona eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Zona no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }
    