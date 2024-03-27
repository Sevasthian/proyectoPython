import requests
import json
def BuscarIDdeActivos(id):
    try:
        peticion = requests.get(f"http://192.168.18.7:5007/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  
    
# def deleteActivos(id):
#     data = BuscarIDdePersonal(id)
#     if len(data):
#         peticion = requests.put(f"http://192.168.18.7:5007/{id}")
#         for val in data:
#             if peticion.status_code == 204:
#                 data.append({"message":  "Activo eliminado correctamente",
#                          "idEstado": val.put('idEstado') })
#             return data
#     else:
#         return {
#                 "body":[{
#                     "Mensaje": "Activo no encontrado.",
#                     "id": id,
#             }],
#             "status": 400,
#             }
    
def deleteActivos(id):
    data = BuscarIDdeActivos(id)
    data[0]["idEstado"] = "2"
    if data is None:
                print(f"""

                    
    Id del activo no encontrado. """)
    else:
        peticion = requests.put(f"http://192.168.18.7:5007/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
        res = peticion.json()
        res["Mensaje"] = "Activo Modificado"
        return [res]

    