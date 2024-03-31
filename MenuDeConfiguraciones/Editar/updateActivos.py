#import
import time
from tabulate import tabulate
import requests
import json
#diseño
from colorama import init, Fore, Style
#******************************************************************************************************************************************************************************************************************************************************
#                                                                                      colores
def animateTextDeLosMenusCyan(text):
    try: 
        for char in text:
            print(Fore.CYAN + char, end="", flush=True)
    except Exception as error:
        animateTextDeLosMenusGreen(str(error))
    except KeyboardInterrupt as error:
              animateTextDeLosMenusGreen("Por favor cierra el programa correctamente  ", str(error))
              input("Presione alguna tecla para continuar con el programa")
def animateTextDeLosMenusGreen(text):
    try: 
        for char in text:
            print(Fore.GREEN + char, end="", flush=True)
    except Exception as error:
        animateTextDeLosMenusGreen(str(error))
    except KeyboardInterrupt as error:
              animateTextDeLosMenusGreen("Por favor cierra el programa correctamente  ", str(error))
              input("Presione alguna tecla para continuar con el programa")
def animateTextDeLosMenusMagenta(text):
    try: 
        for char in text:
            print(Fore.MAGENTA + char, end="", flush=True)
    except Exception as error:
        animateTextDeLosMenusGreen(str(error))
    except KeyboardInterrupt as error:
              animateTextDeLosMenusGreen("Por favor cierra el programa correctamente  ", str(error))
              input("Presione alguna tecla para continuar con el programa")
def animateTextDeLosMenusRed(text):
    try: 
        for char in text:
            print(Fore.RED + char, end="", flush=True)
    except Exception as error:
        animateTextDeLosMenusGreen(str(error))
    except KeyboardInterrupt as error:
              animateTextDeLosMenusGreen("Por favor cierra el programa correctamente  ", str(error))
              input("Presione alguna tecla para continuar con el programa")
def animateTextDeLosMenusYellow(text):
    try: 
        for char in text:
            print(Fore.YELLOW + char, end="", flush=True)
    except Exception as error:
        animateTextDeLosMenusGreen(str(error))
    except KeyboardInterrupt as error:
              animateTextDeLosMenusGreen("Por favor cierra el programa correctamente  ", str(error))
              input("Presione alguna tecla para continuar con el programa")
#******************************************************************************************************************************************************************************************************************************************************
#                                                                                      busquedas
def BuscarIDdeActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("No se encontro la data activos:", str(e))
        return [] 
#******************************************************************************************************************************************************************************************************************************************************
#                                                                                  actualizar activos
def updateActivos(id):
    data = BuscarIDdeActivos(id)
    if data is None:
            animateTextDeLosMenusGreen(f"""

Id del activo no encontrado. """)
    
    while True:
        try:
            print()
            animateTextDeLosMenusYellow(f"""
Datos para modificar: """)
            for i, (val, sev) in enumerate(data[0].items()):
                animateTextDeLosMenusYellow(f"{i+1}. {val}")

            opcion = int(input(f"""
Seleccione una opción: """))
            datoModificar = list(data[0].keys())[opcion - 1]
            if datoModificar in data[0]:
                if datoModificar == "historialActivos" or "asignaciones":
                    print()
                    animateTextDeLosMenusGreen('''   
                                        ESTOS DATOS NO SE PUEDEN MODIFICAR''')
                    break
                else:
                    nuevoValor = input(f"""
        Ingrese el nuevo valor para {datoModificar}: """)
                    data[0][datoModificar] = nuevoValor
                    animateTextDeLosMenusYellow(tabulate(data[0], headers="keys", tablefmt="rounded_grid"))
                    break
            else:
                 print()
                 animateTextDeLosMenusGreen(f"""
Seleccion incorrecta""")
                
        except ValueError as error:
            animateTextDeLosMenusGreen(str(error))
    
    peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data[0], indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Activo Modificado"
    return [res]
            
        


            
