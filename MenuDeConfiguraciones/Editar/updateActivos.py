from colorama import init, Fore, Style
import time
from tabulate import tabulate
import requests
import json
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.YELLOW + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 

def BuscarIDdeActivos(id):
    peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    return [peticion.json()] if peticion.ok else []


def updateActivos(id):
    data = BuscarIDdeActivos(id)
    if data is None:
            animateTextDeLosMenus(f"""

Id del activo no encontrado. """)
    
    while True:
        try:
            print()
            animateTextDeLosMenus(f"""
Datos para modificar: """)
            for i, (val, sev) in enumerate(data[0].items()):
                animateTextDeLosMenus(f"{i+1}. {val}")

            opcion = int(input(f"""
Seleccione una opción: """))
            datoModificar = list(data[0].keys())[opcion - 1]
            if datoModificar in data[0]:
                if datoModificar == "historialActivos" or "asignaciones":
                    print()
                    animateTextDeLosMenus('''   
                                        ESTOS DATOS NO SE PUEDEN MODIFICAR''')
                    break
                else:
                    nuevoValor = input(f"""
        Ingrese el nuevo valor para {datoModificar}: """)
                    data[0][datoModificar] = nuevoValor
                    print(tabulate(data[0], headers="keys", tablefmt="rounded_grid"))
                    break
            else:
                 print()
                 animateTextDeLosMenus(f"""
Seleccion incorrecta""")
                
        except ValueError as error:
            animateTextDeLosMenus(error)
    
    peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Activo Modificado"
    return [res]
            
        


            
