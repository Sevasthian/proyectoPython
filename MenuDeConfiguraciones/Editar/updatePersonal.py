from tabulate import tabulate
import requests
import json

def BuscarIDdePersonal(id):
    peticion = requests.get(f"http://154.38.171.54:5502/personas/{id}")
    return peticion.json() if peticion.ok else []


# def updatePesonal(id):
#     data = BuscarIDdePersonal(id)
#     if data is None:
#             print(f"""

# Id del personal no encontrado. """)
    
#     while True:
#         try:
#             print(f"""
# Datos para modificar: """)
#             for i, (val, sev) in enumerate(data[0].items()):
#                 print(f"{i+1}. {val}")

#             opcion = int(input(f"""
# Seleccione una opción: """))
#             datoModificar = list(data[0].keys())[opcion - 1]
#             nuevoValor = input(f"""
# Ingrese el nuevo valor para {datoModificar}: """)
#             if datoModificar in data[0]:
#                 if datoModificar == "Telefonos":
#                     for i, (val, sev) in enumerate(datoModificar[0].items()):
#                         print(f"{i+1}. {val}")
                    
#                     break
#                 else:
#                     data[0][datoModificar] = nuevoValor
#                     print(tabulate(data[0], headers="keys", tablefmt="rounded_grid"))
#                     break
#             else:
#                  print(f"""
# Seleccion incorrecta""")
                
#         except ValueError as error:
#             print(error)
    
#     peticion = requests.put(f"http://154.38.171.54:5502/personas/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Personal Modificado"
#     return [res]
def updatePersonal(id):
    data = BuscarIDdePersonal(id)
    if data is None:
        print(f"ID del personal no encontrado.")
        return
    
    while True:
        try:
            print()
            print("\nDatos para modificar:")
            for i, (key, value) in enumerate(data.items()):
                print(f"{i+1}. {key}: {value}")

            opcion = int(input("\n Seleccione una opción: "))
            if opcion < 1 or opcion > len(data):
                print()
                print("Selección incorrecta")
                continue
            
            key_to_modify = list(data.keys())[opcion - 1]
            if key_to_modify == "id":
                print('''EL ID NO SE PUEDE MODIFICAR''')
                break
            
            if key_to_modify == "Telefonos":
                for i, (tipo_telefono, datos_telefono) in enumerate(data[key_to_modify][0].items(), start=1):
                    print()
                    print(f"{i}. Tipo de teléfono: {tipo_telefono}")
                    for telefono_key, telefono_value in datos_telefono.items():
                        print()
                        print(f"{telefono_key}: {telefono_value}")
                
                opcion_tel = int(input("Seleccione el tipo de teléfono a modificar: "))
                if opcion_tel < 1 or opcion_tel > len(data[key_to_modify][0]):
                    print()
                    print("Selección incorrecta")
                    continue
                
                tipo_seleccionado = list(data[key_to_modify][0].keys())[opcion_tel - 1]
                nuevo_numero = input(f"Ingrese el nuevo número de {tipo_seleccionado}: ")
                data[key_to_modify][0][tipo_seleccionado]["num"] = nuevo_numero
            else:
                new_value = input(f"Ingrese el nuevo valor para {key_to_modify}: ")
                data[key_to_modify] = new_value
            print()
            print("Datos actualizados:")
            for key, value in data.items():
                print()
            break

        except ValueError:
            print()
            print("Debe ingresar un número.")

    peticion = requests.put(f"http://154.38.171.54:5502/personas/{id}", data=json.dumps(data, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Personal Modificado"
    return [res]