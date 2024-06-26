#import
import requests
import json
import datetime
import time
import uuid
#diseño
from colorama import init, Fore, Style
from tabulate import tabulate
#****************************************************************************************************************************************************************************************************************************
#                                                                                       diseño colores
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
def BuscarIDActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/activos/{id}")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Data de activos no encontrado", str(e))
        return [] 
def BuscarActivos():
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/activos/")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Data de activos no encontrado", str(e))
        return [] 

def DataPersonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/personas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Data personas no encontrado", str(e))
        return []  
def DataZonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/activos/")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Error al realizar la solicitud HTTP:", str(e))
        return []  
def DataTipoDePersonal():
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/personas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Error al realizar la solicitud HTTP: ", str(e))
        return []  
def DataTipoDeZona():
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/zonas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Error al realizar la solicitud HTTP: ", str(e))
        return []  
def BusActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/activos/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("EL ACTIVO NO EXITE:", str(e))
        return []  
#***************************************************************************************************************************************************************************************************************************************************
#                                                                                       filtros
def VerificacionDeIdentidad(CC):
    try:
        for val in DataPersonas():
            if (val.get("nroId (CC, Nit)")  == CC and val.get("Nombre") == "Karen Celis") or (val.get("nroId (CC, Nit)") and  val.get("Nombre") == "Juan Jose Lizarazo"):
                return val
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Verificamos tu identidad y no perteneceses a los alministradores: ", str(e))
        return []
def MostrarIdReposable(cc):
    try:
        for persona in DataPersonas():
            if persona.get("nroId (CC, Nit)") == cc:
                return persona.get("id")
        return None
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Tu numero de CC no se encuentra en la base de datos: ", str(e))
        return []
def BuscarNombreZonas(Nombre):
    try:
        for val in DataZonas():
            if val.get("nombreZona")  == Nombre:
                return [val]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("El nombre de la zona no esta en la base de datos: ", str(e))
        return []
# def SoloMuestraDatosDeAsignaciones():
#     try:
#         historiales = []
#         # Iterar sobre los activos obtenidos de la función BuscarActivos()
#         for activo in BuscarActivos():
#             # Iterar sobre las asignaciones de cada activo
#             for asignacion in activo.get("asignaciones", []):
#                 # Verificar si la asignación es del tipo "Zona"
#                 if asignacion.get("TipoAsignacion") == "Zona" and asignacion.get("NroAsignacion") == :
#                     # Agregar la asignación a la lista de historiales
#                     historiales.append(asignacion)
#         # Devolver la lista de historiales
#         return historiales
#     except requests.exceptions.RequestException as e:
#         # Manejar excepción si ocurre un error al realizar la solicitud
#         animateTextDeLosMenusGreen("ERROR, No se encuentra data")
#***********************************************************************************************************************************************************************************************************************************************
#                                                                                          tablas de diseño 
def TablaPersonal():
    data = DataTipoDePersonal()
    list = []
    for sev in data:
        getAllAc={

                "ID de la persona": sev.get('id'),
                "Nombre de la persona": sev.get('Nombre'),
                
          }
        list.append(getAllAc)
    return list
def TablaZona():
    data = DataTipoDeZona()
    list = []
    for sev in data:
        getAllAc={

                "ID de la zona": sev.get('id'),
                "Nombre de la zona": sev.get('nombreZona'),
                
          }
        list.append(getAllAc)
    return list
#*************************************************************************************************************************************************************************************************************************************************************
#                                                                                          crear asignaciones
def CrearAsignacion(id):
    dificil = BuscarIDActivos(id)
    if dificil.get("asignaciones") == []:
        if not dificil:
            raise ValueError("El ID del activo no existe.")
        Acceso = input("Ingrese su numero de CC: ")
        if VerificacionDeIdentidad(Acceso)is not None:
            if dificil["idEstado"] == "0":
                estado ="1"
                dificil["idEstado"] = estado
                historial = {}
                if not historial.get("NroId"):
                    historial["NroId"] = str(uuid.uuid4().hex[:4])  
                if not historial.get("Fecha"):
                    fecha_actual = datetime.datetime.now().strftime('%Y/%m/%d')
                    historial["Fecha"] = fecha_actual
                if not historial.get("tipoMov"):
                    tipo = "1"
                    historial["tipoMov"] = tipo
                if not historial.get("idRespMov"):
                    repo = MostrarIdReposable(Acceso)
                    letra = str(repo)
                    historial["idRespMov"] = letra
                dificil.setdefault("historialActivos", []).append(historial)
                while True:
                    try:
                        datos = {}
                        if not datos.get("FechaAsignación"):
                            fecha_actual = datetime.datetime.now().strftime('%Y/%m/%d')
                            datos["FechaAsignación"] = fecha_actual
                        if not datos.get("TipoAsignacion"):
                            animateTextDeLosMenusYellow('''         
                                    ELIJA EL TIPO DE ASIGNACIÓN
                                                
                                        1.) PERSONAL
                                        2.) ZONA

            ''')
                            opcion = int(input("Ingrese el tipo de asignación: "))
                            if opcion == 1:
                                tipoPerso = "Personal"
                                datos["TipoAsignacion"] = tipoPerso
                            elif opcion == 2:
                                tipoZon = "Zona"
                                datos["TipoAsignacion"] = tipoZon
                        if not datos.get("AsignadoA"):
                            if datos["TipoAsignacion"] == "Personal":
                                animateTextDeLosMenusYellow(tabulate(TablaPersonal(), headers="keys", tablefmt="double_outline"))
                                Asig1 = input("Ingrese el ID de la persona que quiere asignar: ")
                                datos["AsignadoA"] = Asig1
                                break
                            elif datos["TipoAsignacion"] == "Zona":
                                animateTextDeLosMenusYellow(tabulate(TablaZona(), headers="keys", tablefmt="double_outline"))
                                Asig2 = input("Ingrese el ID de la zona que quiere asignar: ")
                                datos["AsignadoA"] = Asig2
                                break
                    except Exception as error:
                        animateTextDeLosMenusGreen(str(error))
                dificil.setdefault("asignaciones", []).append(datos)
                peticion = requests.patch(f"http://154.38.171.54:5501/activos/{id}", data=json.dumps(dificil, indent=4).encode("UTF-8"))
                res = peticion.json()
                res["Mensaje"] = "Activo Actualizado con Asignación"
                return [res]
            else:
                animateTextDeLosMenusGreen('''NO SE PUEDE ASIGNAR PORQUE EL ACTIVO NO ESTA EN ESTADO NO ASIGNADO''')
        else:
            animateTextDeLosMenusGreen('''
                        POR MOTIVOS DE SEGURIDAD SOLO PERSONAL AUTORIZADO PUEDE CREAR UNA ASIGNACIÓN        ''')
    else:
        animateTextDeLosMenusGreen(" ESTE ACTIVO NO SE PUEDE ASIGNAR PORQUE YA SE ENCUENTRA ASIGNADO")
#************************************************************************************************************************************************************************************************************************************************
#                                                                                          Buquedas de las asignaiones                                                              
def buscarAsignaciones(id):
    data = BusActivos(id)
    list = []
    for sev in data:
        asignacion = {
            "ID del activo": sev.get('id'),
            "Nombre del activo": sev.get('Nombre'),
            "asignaciones": {
                "Fecha de asignación": sev.get('FechaAsignación'),
                "Tipo de asignación": sev.get('TipoAsignacion'),
                "Id de la persona a la que se le asigno": sev.get('AsignadoA')
            }
        }
        list.append(asignacion)
    return list
