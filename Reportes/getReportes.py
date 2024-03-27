import requests
from tabulate import tabulate
import json
def getAllDataActivos():
    try:
            peticion =  requests.get("http://154.38.171.54:5502/activos")
            data = peticion.json()
            return data
    except requests.RequestException as e:
            print("Error en la solicitud HTTP:", e)
            return []
    except ValueError as e:
            print("Error al cargar JSON:", e)
            return []
def getAllDataIdMarca():
        try:
                peticion =  requests.get("http://154.38.171.54:5502/marcas")
                data = peticion.json()
                return data
        except requests.RequestException as e:
                print("Error en la solicitud HTTP:", e)
                return []
        except ValueError as e:
                print("Error al cargar JSON:", e)
        return []
def getAllDataCategoria():
    try:
                peticion =  requests.get("http://154.38.171.54:5502/categoriaActivos")
                data = peticion.json()
                return data
    except requests.RequestException as e:
                print("Error en la solicitud HTTP:", e)
                return []
    except ValueError as e:
                print("Error al cargar JSON:", e)
    return []
      
      


def getAllActivos():
    allActivos = []
    for sev in getAllDataActivos():
          getAllAc={
                "NroSerial": sev.get('NroSerial'),
                "CodCampus": sev.get('CodCampus'),
                "Nombre": sev.get('Nombre'),
                "ID Marca": sev.get('idMarca'),
          }
          allActivos.append(getAllAc)
    return allActivos

def getAllMarcas():
    allMarca = []
    for dia in getAllDataIdMarca():
            getAllMar = {
                    "ID de la marca": dia.get('id'),
                    "nombreDelProducto": dia.get('Nombre')
                    
            }
            allMarca.append(getAllMar)
    return allMarca

# def getAllCategoria():
#       datosDeActivo = getAllDataActivos()
#       datosDeCategoria = getAllDataCategoria()
#       while True:
#         try:
#             print(tabulate(datosDeCategoria, headers="keys", tablefmt="rounded_grid"))
#             print(f"""
# Lista de las categorias a selecionar """)
#             for val in datosDeCategoria:
#                 print(f"{val['id']}.) {val['Nombre']}")
         
#             opcion = int(input('''
# Seleccione una opción que desea visualisar: '''))
#             if opcion == 1:
#                    getAllÑ = []
#                    if 
#                    }
#                    for val in datosDeActivo:
#                           getAll1 = {
#                                  "NumeroSerial" : val.get('NroSerial'),
#                                  "Nombre" : val.get('Nombre'),
#                                  "Proveedor" : val.get('Proveedor'),
#                                  "IDcategoria" : val.get('idCategoria')
#                           }
#                           getAllÑ.append(getAllÑ)
#                           return(getAll1)
#                    print(tabulate(getAllÑ, headers="keys", tablefmt="rounded_grid"))
#             elif opcion == 2:
#                    getAllD = []
#                    for val in datosDeActivo:
#                           getAll2 = {

#                           }



