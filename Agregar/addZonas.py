import re
import requests
import json
def DataZonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/zonas/")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  

def BuscarNombreZonas(Nombre):
    for val in DataZonas():
        if val.get("nombreZona")  == Nombre:
            return [val] 


        
# def AddZona():
#     producto = {}
#     while True:
#         try:
#             if not producto.get("nombreZona"):
#                 codigo = input("Ingrese el Nombre de la zona: ")
#                 if re.match(r'^[A-Z]', codigo)is not None:
#                     if BuscarNombreZonas(codigo):
#                         raise Exception("El nombre ingresado ya existe.")
#                     else:
#                         producto["nombreZona"] = codigo
#                 else:
#                     raise Exception(f"El nombre no cumple con el estandar establecido, recuerde que el nombre de las zonas empiezan con mayúsculas.")
                
#             if not producto.get("totalCapacidad"):
#                 nombre = input(f"Ingrese la capacidad de la zona: ")
#                 if re.match(r'^\d+$', nombre)is not None:
#                     producto["totalCapacidad"] = nombre
#                     break
#                 else:
#                     raise Exception("Capacidad no valido, recuerde que son numeros positivos lo que se ingresa.")
#         except Exception as error:
#             print(error)     
#     peticion = requests.post("http://154.38.171.54:5007/pedidos", data=json.dumps(producto, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Zona Guardada"
#     return [res]


# def AddZona():
#     producto = {}
#     while True:
#         try:
#             if not producto.get("nombreZona"):
#                 codigo = input("Ingrese el Nombre de la zona: ")
#                 if re.match(r'^[A-Z]', codigo) is not None:
#                     if BuscarNombreZonas(codigo):
#                         raise Exception("El nombre ingresado ya existe.")
#                     else:
#                         producto["nombreZona"] = codigo
#                 else:
#                     raise Exception(f"El nombre no cumple con el estandar establecido, recuerde que el nombre de las zonas empiezan con mayúsculas.")
                
#             if not producto.get("totalCapacidad"):
#                 nombre = input(f"Ingrese la capacidad de la zona: ")
#                 if re.match(r'^\d+$', nombre) is not None:
#                     producto["totalCapacidad"] = nombre
#                 else:
#                     raise Exception("Capacidad no valido, recuerde que son numeros positivos lo que se ingresa.")
            
#             guardar_zona(producto)
#             return {"Mensaje": "Zona Guardada"}
            
#         except Exception as error:
#             print(error)                     
        
    
# def guardar_zona(producto):
#     peticion = requests.post("http://154.38.171.54:5502/zonas/", data=json.dumps(producto, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     return res


def AddZona(nombre, capacidad):
    url = "http://154.38.171.54:5502/zonas/"
    datos_zona = {"nombreZona": nombre, "totalCapacidad": capacidad}
    try:
        respuesta = requests.post(url, data=json.dumps(datos_zona))
        return respuesta.json()
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return None
