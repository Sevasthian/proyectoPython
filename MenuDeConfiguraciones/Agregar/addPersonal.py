import re
import requests
import json
import uuid
def DataPersonal():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  

def BuscarNombreDeElPersonal(Nombre):
    for val in DataPersonal():
        if val.get("Nombre")  == Nombre:
            return [val]



def AddPersonal():
    Personal = {}
    while True:
        try:     
            if not Personal.get("id"):
                Personal["id"] = str(uuid.uuid4().hex[:4])
            if not Personal.get("nroId (CC, Nit)"):
                nroID = input("Ingrese el número de identificación: ")
                if re.match(r'^\d+$', nroID) is not None:
                        Personal["nroId (CC, Nit)"] = nroID
                else:
                    raise Exception("CC no valido, recuerde que solo se ingresan números")
                
            if not Personal.get("Nombre"):
                Nombre = input("Ingrese el nombre del personal a agregar: ")
                if re.match(r'^[A-Z][a-z\s]+$', Nombre) is not None:
                    if BuscarNombreDeElPersonal(Nombre):
                        raise Exception("El nombre de la zona ingresado ya existe.")
                    else:
                        Personal["Nombre"] = Nombre
                else:
                    raise Exception("Nombre no valido, recuerde que los nombres inician con mayuculas")
            if not Personal.get("Email"):
                email = input("Ingrese el email del personal:")
                if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None:
                    Personal["Email"] = email
                else:
                    raise Exception("Esto no es un email, aca te doy un ejemplo de como debe ser (sevasthian7777@gmail.com)")
            if not Personal.get("Telefonos"):
                telefonos = {}
                movil = input("Ingrese el número de teléfono móvil: ")
                if re.match(r'^\d{10}$', movil) is not None:
                    telefonos["movil"] = {
                        "id":Personal.get("id"),
                        "num": movil}
                else:
                    raise Exception("Número de teléfono móvil no válido, recuerde ingresar 10 dígitos")
                    
                casa = input("Ingrese el número de teléfono fijo (casa): ")
                if re.match(r'^\d{10}$', casa) is not None:
                    telefonos["casa"] = {
                        "id":Personal.get("id"),
                        "num": casa}
                else:
                    raise Exception("Número de teléfono fijo no válido, recuerde ingresar 10 dígitos")
                    
                Personal["Telefonos"] = [telefonos]
                break
                                   
        except Exception as error:
            print(error)
    peticion = requests.post("http://154.38.171.54:5502/personas/", data=json.dumps(Personal, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Personal Guardado"
    return [res]
{
    "id": "3",
    "nroId (CC, Nit)": "1003697856",
    "Nombre": "Miguel Castro",
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

