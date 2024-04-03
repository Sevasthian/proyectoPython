#import
import time
import requests
import json
#diseño
from tabulate import tabulate
from colorama import init, Fore, Style
#**************************************************************************************************************************************************************************************************
#                                                                        colores
def animateTextDeLosMenusCyan(text):
        try:
            for char in text:
                print(Fore.CYAN + char, end="", flush=True)
                time.sleep(0.001)
            print(Style.RESET_ALL)
        except TypeError:
            animateTextDeLosMenusGreen("Por favor ingrese los datos pedidos")
            input("Presione alguna tecla para continuar con el programa...")
        except KeyboardInterrupt:
            animateTextDeLosMenusGreen("El programa se va a cerrar porque el usuario no lo dejo correr   ")
            input( "   Presione alguna tecla para continuar con la cancelación del programa")
            raise KeyboardInterrupt("Por favor utiliza bien el programa")
        except Exception as error:
            animateTextDeLosMenusGreen(str(error))
def animateTextDeLosMenusGreen(text):
        try: 
            for char in text:
                print(Fore.GREEN + char, end="", flush=True)
            print(Style.RESET_ALL)
            time.sleep(0.001)
        except TypeError:
            animateTextDeLosMenusGreen("Por favor ingrese los datos pedidos")
            input("Presione alguna tecla para continuar con el programa...")
        except KeyboardInterrupt:
            animateTextDeLosMenusGreen("El programa se va a cerrar porque el usuario no lo dejo correr   ")
            input( "   Presione alguna tecla para continuar con la cancelación del programa")
            raise KeyboardInterrupt("Por favor utiliza bien el programa")
        except Exception as error:
            animateTextDeLosMenusGreen(str(error))
def animateTextDeLosMenusMagenta(text): 
        try: 
            for char in text:
                print(Fore.MAGENTA + char, end="", flush=True)
            print(Style.RESET_ALL)
        except TypeError:
            animateTextDeLosMenusGreen("Por favor ingrese los datos pedidos")
            input("Presione alguna tecla para continuar con el programa...")
        except KeyboardInterrupt:
            animateTextDeLosMenusGreen("El programa se va a cerrar porque el usuario no lo dejo correr   ")
            input( "   Presione alguna tecla para continuar con la cancelación del programa")
            raise KeyboardInterrupt("Por favor utiliza bien el programa")
        except Exception as error:
            animateTextDeLosMenusGreen(str(error))
def animateTextDeLosMenusRed(text):
        try: 
            for char in text:
                print(Fore.RED + char, end="", flush=True)
                time.sleep(0.001)
            print(Style.RESET_ALL)
        except TypeError:
            animateTextDeLosMenusGreen("Por favor ingrese los datos pedidos")
            input("Presione alguna tecla para continuar con el programa...")
        except KeyboardInterrupt:
            animateTextDeLosMenusGreen("El programa se va a cerrar porque el usuario no lo dejo correr   ")
            input( "   Presione alguna tecla para continuar con la cancelación del programa")
            raise KeyboardInterrupt("Por favor utiliza bien el programa")
        except Exception as error:
            animateTextDeLosMenusGreen(str(error))
def animateTextDeLosMenusYellow(text):
        try: 
            for char in text:
                print(Fore.YELLOW + char, end="", flush=True)
            print(Style.RESET_ALL)
        except TypeError:
            animateTextDeLosMenusGreen("Por favor ingrese los datos pedidos")
            input("Presione alguna tecla para continuar con el programa...")
        except KeyboardInterrupt:
            animateTextDeLosMenusGreen("El programa se va a cerrar porque el usuario no lo dejo correr   ")
            input( "   Presione alguna tecla para continuar con la cancelación del programa")
            raise KeyboardInterrupt("Por favor utiliza bien el programa")
        except Exception as error:
            animateTextDeLosMenusGreen(str(error))
#**************************************************************************************************************************************************************************************************
#                                                                         busquedas
def BuscarIDdePersonal(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas/{id}")
        peticion.raise_for_status()
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Los datos en la base de datos: ", str(e))
        return []
#***************************************************************************************************************************************************************************************************
#                                                                        editar personal
def updatePersonal(id):
    data = BuscarIDdePersonal(id)
    if data is None:
        animateTextDeLosMenusGreen(f"Dato del personal no encontrado.")
        return
    
    while True:
        try:
            print()
            animateTextDeLosMenusYellow("\nDatos para modificar:")
            for i, (key, value) in enumerate(data.items()):
                animateTextDeLosMenusYellow(f"{i+1}. {key}: {value}")

            opcion = int(input("\n Seleccione una opción: "))
            if opcion < 1 or opcion > len(data):
                print()
                animateTextDeLosMenusGreen("Selección incorrecta")
                continue
            
            key_to_modify = list(data.keys())[opcion - 1]
            if key_to_modify == "id":
                animateTextDeLosMenusGreen('''EL ID NO SE PUEDE MODIFICAR''')
                break
            
            if key_to_modify == "Telefonos":
                for i, (tipo_telefono, datos_telefono) in enumerate(data[key_to_modify][0].items(), start=1):
                    animateTextDeLosMenusYellow(f"{i}. Tipo de teléfono: {tipo_telefono}") #hacer cambio de color
                    for telefono_key, telefono_value in datos_telefono.items():
                        animateTextDeLosMenusMagenta(f"{telefono_key}: {telefono_value}")# hacer cambio de color
                
                opcion_tel = int(input("Seleccione el tipo de teléfono a modificar: "))
                if opcion_tel < 1 or opcion_tel > len(data[key_to_modify][0]):
                    print()
                    animateTextDeLosMenusGreen("Selección incorrecta")
                    continue
                
                tipo_seleccionado = list(data[key_to_modify][0].keys())[opcion_tel - 1]
                nuevo_numero = input(f"Ingrese el nuevo número de {tipo_seleccionado}: ")
                data[key_to_modify][0][tipo_seleccionado]["num"] = nuevo_numero
            else:
                new_value = input(f"Ingrese el nuevo valor para {key_to_modify}: ")
                data[key_to_modify] = new_value
            print()
            animateTextDeLosMenusMagenta("Datos actualizados:")
            for key, value in data.items():
                print()
            break

        except ValueError as error:
            print()
            animateTextDeLosMenusGreen("Debe ingresar un número.", str(error) )

    peticion = requests.put(f"http://154.38.171.54:5502/personas/{id}", data=json.dumps(data, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Personal Modificado"
    return [res]