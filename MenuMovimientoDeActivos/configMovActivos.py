import requests
import json
from tabulate import tabulate


def BuscarIDdeActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  

    
def deleteActivos(id):
    data = BuscarIDdeActivos(id)
    data[0]["idEstado"] = "0"
    data[0]["asignaciones"] = []
    if data is None:
                print(f"""

                    
    Id del activo no encontrado. """)
    else:
        peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
        res = peticion.json()
        res["Mensaje"] = "Activo Modificado"
        return [res]
    
def darActivoPorDeBaja(id):
    data = BuscarIDdeActivos(id)
    data[0]["idEstado"] = "2"
    data[0]["asignaciones"] = []
    if data is None:
                print(f"""

                    
    Id del activo no encontrado. """)
    else:
        peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
        res = peticion.json()
        res["Mensaje"] = "Activo Modificado"
        return [res]
    


def darActivoPorGarantia(id):
    data = BuscarIDdeActivos(id)
    data[0]["idEstado"] = "3"
    data[0]["asignaciones"] = []
    if data is None:
                print(f"""

                    
    Id del activo no encontrado. """)
    else:
        peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
        res = peticion.json()
        res["Mensaje"] = "Activo Modificado"
        return [res]
    
