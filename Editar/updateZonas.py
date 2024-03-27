from tabulate import tabulate
import requests
import json

def BuscarIDdeZonas(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/zonas/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  


def updateZonas(id):
    data = BuscarIDdeZonas(id)
    if data is None:
            print(f"""

Id del Zonas no encontrado. """)
    
    while True:
        try:
            print(f"""
Datos para modificar: """)
            for i, (val, sev) in enumerate(data[0].items()):
                print(f"{i+1}. {val}")

            opcion = int(input(f"""
Seleccione una opción: """))
            datoModificar = list(data[0].keys())[opcion - 1]
            nuevoValor = input(f"""
Ingrese el nuevo valor para {datoModificar}: """)
            if datoModificar in data[0]:
                if datoModificar == "totalCapacidad":
                    data[0][datoModificar] = int(nuevoValor)
                    break
                else:
                    data[0][datoModificar] = nuevoValor
                    print(tabulate(data[0], headers="keys", tablefmt="rounded_grid"))
                    break
            else:
                 print(f"""
Seleccion incorrecta""")
                
        except ValueError as error:
            print(error)
    
    peticion = requests.put(f"http://154.38.171.54:5502/zonas/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Zona Modificada"
    return [res]
            
# def updateZonas(id):
#     data = BuscarIDdeZonas(id)
#     if not data:
#         print(f"ID del personal no encontrado para el ID {id}.")
#         return
    
#     for zona_index in range(len(data)):
#         zona = data[zona_index]
#         print(f"\nDatos de la zona {zona_index + 1}:")
#         print(tabulate(zona, headers="keys", tablefmt="rounded_grid"))
#         while True:
#             try:
#                 print("\nDatos para modificar:")
#                 for i, (val, sev) in enumerate(zona.items()):
#                     print(f"{i+1}. {val}")

#                 opcion = int(input("\nSeleccione una opción: "))
#                 if 1 <= opcion <= len(zona):
#                     datoModificar = list(zona.keys())[opcion - 1]
#                     nuevoValor = input(f"Ingrese el nuevo valor para {datoModificar}: ")
#                     if datoModificar == "NroItem" or "CodTransaccion" or "NroFormulario":
#                         zona[datoModificar] = int(nuevoValor)
#                     else:
#                         zona[datoModificar] = nuevoValor
#                     print(tabulate(zona, headers="keys", tablefmt="rounded_grid"))
#                     break
#                 else:
#                     print("Opción seleccionada fuera de rango.")
#             except ValueError:
#                 print("Error: Ingrese un número entero válido para la opción.")
    
#     try:
#         peticion = requests.put(f"http://154.38.171.54:5502/zonas/{id}", data=json.dumps(data, indent=4).encode("UTF-8"))
#         peticion.raise_for_status()
#         res = peticion.json()
#         res["Mensaje"] = "Personal Modificado"
#         return [res]
#     except requests.exceptions.RequestException as e:
#         print("Error al actualizar el personal:", e)
#         return []