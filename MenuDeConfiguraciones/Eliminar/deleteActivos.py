import requests
import json
from colorama import init, Fore, Style
import time
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.YELLOW + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
def BuscarIDdeActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", e)
        return []
    
def deleteActivos(id):
    try:
        data = BuscarIDdeActivos(id)
        if data[0]["asignaciones"] == []:
            data[0]["idEstado"] = "2"
            if data is None:
                        animateTextDeLosMenus(f"""

                            
            Id del activo no encontrado. """)
            else:
                peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
                res = peticion.json()
                res["Mensaje"] = "Activo Modificado"
                return [res]
        else:
            animateTextDeLosMenus('''
                                ESTE ACTIVO NO SE PUEDE ELIMINAR PORQUE SE ENCUENTRA ASIGNADO
                ''')
    except Exception as error:
         animateTextDeLosMenus(error)
         
def DeletePersonal(id):
    data = BuscarIDdeActivos(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5502/activos/{id}")
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
    