#import
import re
import requests
import json
#diseño
from colorama import init, Fore, Style
import time
#**************************************************************************************************************************************************************************************************************************
#                                                                                         colores
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
#*****************************************************************************************************************************************************************************************************************************
#                                                                                        busquedas 
def DataZonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/zonas/")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Error al realizar la solicitud HTTP:", str(e))
        return []  
#***************************************************************************************************************************************************************************************************************************************
#                                                                                         filtros
def BuscarNombreZonas(Nombre):
    try:
        for val in DataZonas():
            if val.get("nombreZona")  == Nombre:
                return [val]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("El nombre de la zona no se encuentra en la base de datos: ", str(e))
        return []
#****************************************************************************************************************************************************************************************************************************************
#                                                                                       añadir una zona
def AddZona():
    Zona = {}
    while True:
        try:     
            if not Zona.get("nombreZona"):
                animateTextDeLosMenusMagenta('''

  ______  __  __  _____   ______  _____  ______  __  __   ____    _____                                                        
 |  ____||  \/  ||  __ \ |  ____|/ ____||  ____||  \/  | / __ \  / ____|           /\                                          
 | |__   | \  / || |__) || |__  | |     | |__   | \  / || |  | || (___            /  \                                         
 |  __|  | |\/| ||  ___/ |  __| | |     |  __|  | |\/| || |  | | \___ \          / /\ \                                        
 | |____ | |  | || |     | |____| |____ | |____ | |  | || |__| | ____) |        / ____ \                                       
 |______||_|  |_||_|     |______|\_____||______||_|  |_| \____/ |_____/        /_/    \_\                                      
            _____  _____   ______  _____            _____           _    _  _   _                ______ ____   _   _           
     /\    / ____||  __ \ |  ____|/ ____|    /\    |  __ \         | |  | || \ | |    /\        |___  // __ \ | \ | |    /\    
    /  \  | |  __ | |__) || |__  | |  __    /  \   | |__) |        | |  | ||  \| |   /  \          / /| |  | ||  \| |   /  \   
   / /\ \ | | |_ ||  _  / |  __| | | |_ |  / /\ \  |  _  /         | |  | || . ` |  / /\ \        / / | |  | || . ` |  / /\ \  
  / ____ \| |__| || | \ \ | |____| |__| | / ____ \ | | \ \         | |__| || |\  | / ____ \      / /__| |__| || |\  | / ____ \ 
 /_/    \_\\_____||_|  \_\|______|\_____|/_/    \_\|_|  \_\         \____/ |_| \_|/_/    \_\    /_____|\____/ |_| \_|/_/    \_
                                                                                                                                                                                                                                                             
''')
                nombre = input("Ingrese el nombre de la zona: ")
                if re.match(r'^[A-Z]', nombre) is not None:
                    if BuscarNombreZonas(nombre):
                        raise Exception("El nombre de la zona ingresado ya existe.")
                    else:
                        Zona["nombreZona"] = nombre
                else:
                    raise Exception("Nombre no valido, recuerde que los nombres inician con mayuculas")
                
            if not Zona.get("totalCapacidad"):
                capacidad = input("Ingrese la capacidad de la zona: ")
                if re.match(r'^\d+$', capacidad) is not None:
                    Zona["totalCapacidad"] = capacidad
                    break
                else:
                    raise Exception("La capacidad de la zona solo se registran números")
                                   
        except Exception as error:
            animateTextDeLosMenusGreen(str(error))
    peticion = requests.post("http://154.38.171.54:5501/zonas/", data=json.dumps(Zona, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Zona Guardada"
    return [res]