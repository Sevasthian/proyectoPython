import requests
def BuscarIDdePersonal(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  



def DeletePersonal(id):
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
    