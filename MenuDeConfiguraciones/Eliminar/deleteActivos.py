#import
import requests
import json
import datetime
import uuid
#diseño
from colorama import init, Fore, Style
#*********************************************************************************************************************************************************************************
#                                                                          colores
def animateTextDeLosMenusCyan(text):
        try:
            for char in text:
                print(Fore.CYAN + char, end="", flush=True)
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
        except TypeError:
            animateTextDeLosMenusGreen("Por favor ingrese los datos pedidos")
            input("Presione alguna tecla para continuar con el programa...")
        except KeyboardInterrupt:
            animateTextDeLosMenusGreen("El programa se va a cerrar porque el usuario no lo dejo correr   ")
            input( "   Presione alguna tecla para continuar con la cancelación del programa")
            raise KeyboardInterrupt("Por favor utiliza bien el programa")
        except Exception as error:
            animateTextDeLosMenusGreen(str(error))
#**********************************************************************************************************************************************************************************
#                                                                          busquedas
def BuscarIDdeActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException:
        animateTextDeLosMenusGreen("Data no encontrada:")
        return []
def DataPersonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("No se encuentra en la data")
        return []  
#*************************************************************************************************************************************************************************************
#                                                                               filtro
def MostrarIdReposable(cc):
        try:
            data = DataPersonas()
            for persona in data:
                if persona.get("nroId (CC, Nit)") == cc:
                    return persona.get("id")
            return None 
        except requests.exceptions.RequestException as e:
            animateTextDeLosMenusGreen("Su cc no se encuentra en la base de datos ")
            return []
#*********************************************************************************************************************************************************************************************
#                                                                                eliminar activos
def deleteActivos(id):
    try:
        data = BuscarIDdeActivos(id)
        Acceso = input("Ingrese su numero de CC: ")
        if MostrarIdReposable(Acceso):
            if data["asignaciones"] == []:
                data["idEstado"] = "2"
                historial = {}
                if not historial.get("NroId"):
                    historial["NroId"] = str(uuid.uuid4().hex[:4]) 
                if not historial.get("Fecha"):
                    fecha_actual = datetime.datetime.now().strftime('%Y/%m/%d')
                    historial["Fecha"] = fecha_actual
                if not historial.get("tipoMov"):
                    historial["tipoMov"] = "2"
                if not historial.get("idRespMov"):
                    historial["idRespMov"] = str(MostrarIdReposable(Acceso))
                data.setdefault("historialActivos", []).append(historial)
                url = f"http://154.38.171.54:5502/activos/{id}"
                peticion = requests.put(url, data=json.dumps(data, indent=4).encode("UTF-8"))
                res = peticion.json()
                res["Mensaje"] = "Activo Modificado"
                return [res]
            else:
                animateTextDeLosMenusGreen('''
                                ESTE ACTIVO NO SE PUEDE ELIMINAR PORQUE SE ENCUENTRA ASIGNADO
                ''')
        else:
            animateTextDeLosMenusGreen('''
                                ACCESO DENEGADO
                ''')
    except Exception as error:
        animateTextDeLosMenusGreen(str(error))
#**************************************************************************************************************************************************************************************************
#                                                                         opcion secreta para eliminar activo 
def DeleteActivoSecreto(id):
    data = BuscarIDdeActivos(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5502/activos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Zona eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Zona no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }
    