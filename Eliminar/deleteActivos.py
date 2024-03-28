import requests
import json
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
    data[0]["idEstado"] = "2"
    if data is None:
                print(f"""

                    
    Id del activo no encontrado. """)
    else:
        peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
        res = peticion.json()
        res["Mensaje"] = "Activo Modificado"
        return [res]




def DeletePersonal(id):
    data = BuscarIDdeActivos(id)
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
    