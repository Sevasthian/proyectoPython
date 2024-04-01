#import
import re
import requests
import json
import uuid
import time
#diseño
from colorama import init, Fore, Style
#**********************************************************************************************************************************************************************************************************************************
#                                                                                                     colores
def animateTextDeLosMenusCyan(text):
        try:
            for char in text:
                print(Fore.CYAN + char, end="", flush=True)
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
#******************************************************************************************************************************************************************************************************************************************
#                                                                                                 buscar
def DataPersonal():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("No se encontro el ID buscado:",str(e))
        return []  
#************************************************************************************************************************************************************************************************************************************************************
#                                                                                                 filtros
def BuscarNombreDeElPersonal(Nombre):
    try:
        for val in DataPersonal():
            if val.get("Nombre")  == Nombre:
                return [val]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("El nombre del personal no se encuentra en la base de datos: ", str(e))
        return []
#*********************************************************************************************************************************************************************************************************************************************************
#                                                                                                añadir personas
def AddPersonal():
    Personal = {}
    while True:
        try:     
            if not Personal.get("id"):
                Personal["id"] = str(uuid.uuid4().hex[:4])
            if not Personal.get("nroId (CC, Nit)"):
                animateTextDeLosMenusMagenta('''
  ______  __  __  _____   ______  _____  ______  __  __   ____    _____                                                                                   
 |  ____||  \/  ||  __ \ |  ____|/ ____||  ____||  \/  | / __ \  / ____|           /\                                                                     
 | |__   | \  / || |__) || |__  | |     | |__   | \  / || |  | || (___            /  \                                                                    
 |  __|  | |\/| ||  ___/ |  __| | |     |  __|  | |\/| || |  | | \___ \          / /\ \                                                                   
 | |____ | |  | || |     | |____| |____ | |____ | |  | || |__| | ____) |        / ____ \                                                                  
 |______||_|  |_||_|     |______|\_____||______||_|  |_| \____/ |_____/        /_/    \_\                                                                 
            _____  _____   ______  _____            _____           _    _  _   _         _____   ______  _____    _____   ____   _   _            _      
     /\    / ____||  __ \ |  ____|/ ____|    /\    |  __ \         | |  | || \ | |       |  __ \ |  ____||  __ \  / ____| / __ \ | \ | |    /\    | |     
    /  \  | |  __ | |__) || |__  | |  __    /  \   | |__) |        | |  | ||  \| |       | |__) || |__   | |__) || (___  | |  | ||  \| |   /  \   | |     
   / /\ \ | | |_ ||  _  / |  __| | | |_ |  / /\ \  |  _  /         | |  | || . ` |       |  ___/ |  __|  |  _  /  \___ \ | |  | || . ` |  / /\ \  | |     
  / ____ \| |__| || | \ \ | |____| |__| | / ____ \ | | \ \         | |__| || |\  |       | |     | |____ | | \ \  ____) || |__| || |\  | / ____ \ | |____ 
 /_/    \_\\_____||_|  \_\|______|\_____|/_/    \_\|_|  \_\         \____/ |_| \_|       |_|     |______||_|  \_\|_____/  \____/ |_| \_|/_/    \_\|______|
                                                                                                                                                          
                                                                                                                                                          
''')
                nroID = input("Ingrese el número de identificación: ")
                if re.match(r'^\d+$', nroID) is not None:
                        Personal["nroId (CC, Nit)"] = nroID
                else:
                    raise Exception("CC no valido, recuerde que solo se ingresan números")
                
            if not Personal.get("Nombre"):
                Nombre = input("Ingrese el nombre del personal a agregar: ")
                if re.match(r'^[A-Z][a-z]+(?:\s[A-Z][a-z]+){0,3}$', Nombre) is not None:
                    if BuscarNombreDeElPersonal(Nombre):
                        raise Exception("El nombre de la zona ingresado ya existe.")
                    else:
                        Personal["Nombre"] = Nombre
                else:
                    raise Exception("Nombre no valido, recuerde que los nombres inician con mayuculas")
            if not Personal.get("Email"):
                email = input("Ingrese el email del personal: ")
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
            animateTextDeLosMenusGreen(str(error))
    peticion = requests.post("http://154.38.171.54:5502/personas/", data=json.dumps(Personal, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Personal Guardado"
    return [res]


