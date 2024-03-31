import requests
from colorama import init, Fore, Style
import time
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.YELLOW + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
def BuscarIDdePersonal(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", e)
        return []  
def dataPersonal():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", e)
        return []  
    



def condiccionDePersonal(id):
    condicion = []
    for val in dataPersonal():
        if val.get("asignaciones"):
            buscar = val['asignaciones'][0]
            if buscar.get("TipoAsignacion") == "Personal" and buscar.get("AsignadoA") == id:
                condicion.append(buscar)
    return condicion



def DeletePersonal(id):
    if not condiccionDePersonal(id):
        data = BuscarIDdePersonal(id)
        if len(data):
            peticion = requests.delete(f"http://154.38.171.54:5502/personas/{id}")
            if peticion.status_code == 204:
                data.append({"message":  "Personal eliminado correctamente"})
                return {
                    "body": data,
                    "status": peticion.status_code,
                }     
        else:
            return {
                    "body":[{
                        "Mensaje": "Personal no encontrado.",
                        "id": id,
                }],
                "status": 400,
                }
    else:
        animateTextDeLosMenus('''

            NO SE PUEDE ELIMINAR PERSONAL PORQUE YA TIENE ACTIVO ASIGNADO'''
              )
