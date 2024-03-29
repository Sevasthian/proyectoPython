import re
import requests
import json
def DataZonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/zonas/")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  

def BuscarNombreZonas(Nombre):
    for val in DataZonas():
        if val.get("nombreZona")  == Nombre:
            return [val]



def AddZona():
    Personal = {}
    while True:
        try:     
            if not Personal.get("nroId (CC, Nit)"):
                nombre = input("Ingrese el nombre de la zona: ")
                if re.match(r'^[A-Z]', nombre) is not None:
                    if BuscarNombreZonas(nombre):
                        raise Exception("El nombre de la zona ingresado ya existe.")
                    else:
                        Personal["nombreZona"] = nombre
                else:
                    raise Exception("Nombre no valido, recuerde que los nombres inician con mayuculas")
                
            if not Personal.get("totalCapacidad"):
                capacidad = input("Ingrese la capacidad de la zona: ")
                if re.match(r'^\d+$', capacidad) is not None:
                    Personal["totalCapacidad"] = capacidad
                    break
                else:
                    raise Exception("La capacidad de la zona solo se registran números")
                                   
        except Exception as error:
            print(error)
    peticion = requests.post("http://154.38.171.54:5502/zonas/", data=json.dumps(Personal, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Zona Guardada"
    return [res]

{
    "id": "3",
    "nroId (CC, Nit)": "1003697856",
    "nroId (CC, Nit)": "Miguel Castro",
    "Email": "miguelcastro@example.com",
    "Telefonos": [
      {
        "movil": {
          "id": "3",
          "num": "3002014592"
        },
        "casa": {
          "id": "3",
          "num": "3002014593"
        }
      }
    ]
  }