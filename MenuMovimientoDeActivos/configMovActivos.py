#import
import requests
import json
import datetime
import uuid
import time
#esto es diseño
from tabulate import tabulate
from colorama import init, Fore, Style
#*******************************************************************************************************************************************************************************************************************************************
#                                                               diseño
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
#*********************************************************************************************************************************************************************************************************************************************
#                                                                busquedas
def DataPersonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/personas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("No se encontraron datos de la persona")
        return []  
def DataZonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/activos/")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("No se encontro data en la zonas")
        return []  
def DataTipoDePersonal():
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/personas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Error al realizar la solicitud HTTP:")
        return []  
def DataTipoDeZona():
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/zonas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("Error al realizar la solicitud HTTP:")
        return []  
def BuscarIDdeActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/activos/{id}")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
            animateTextDeLosMenusGreen("No se encuentran activos")
            return []
#*************************************************************************************************************************************************************************************************************
#                                                                                filtros 
def VerificacionDeIdentidad(CC):
    try:
        for val in DataPersonas():
            if (val.get("nroId (CC, Nit)")  == CC and val.get("Nombre") == "Karen Celis") or (val.get("nroId (CC, Nit)") and  val.get("Nombre") == "Juan Jose Lizarazo"):
                return val
        return None
    except requests.exceptions.RequestException as e:
            animateTextDeLosMenusGreen("Su cc no es de tipo alministrador")
            return []
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
def BuscarNombreZonas(Nombre):
    try:
        for val in DataZonas():
            if val.get("nombreZona")  == Nombre:
                return [val]
        return None
    except requests.exceptions.RequestException as e:
            animateTextDeLosMenusGreen("No se encontro en nombre")
            return []
#*************************************************************************************************************************************************************************************************************
#                                                                               tablas   
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
#****************************************************************************************************************************************************************************************************************
#                                                                                eliminar activos                                                                             
def deleteActivos(id):
    while True:
        try:
            data = BuscarIDdeActivos(id)
            Acceso = input("Ingrese su numero de CC: ")
            if MostrarIdReposable(Acceso):
                data["idEstado"] = "0"
                data["asignaciones"] = []
                historial = {}
                if not historial.get("NroId"):
                    historial["NroId"] = str(uuid.uuid4().hex[:4])
                if not historial.get("Fecha"):
                    fecha_actual = datetime.datetime.now().strftime('%Y/%m/%d')
                    historial["Fecha"] = fecha_actual
                if not historial.get("tipoMov"):
                    tipo = "2"
                    historial["tipoMov"] = tipo
                if not historial.get("idRespMov"):
                    repo = MostrarIdReposable(Acceso)
                    letra = str(repo)
                    historial["idRespMov"] = letra   
                data.setdefault("historialActivos", []).append(historial)
                peticion = requests.put(f"http://154.38.171.54:5501/activos/{id}", data=json.dumps(data, indent=4).encode("UTF-8"))
                res = peticion.json()
                res["Mensaje"] = "Activo Modificado"
                return [res]
                    
        except requests.exceptions.RequestException as error:
                animateTextDeLosMenusGreen("ID no encontrado", str(error))
                return
                
        except ValueError as error:
                animateTextDeLosMenusGreen("ID no encontrado", str(error))
                return
#*********************************************************************************************************************************************************************************************************
#                                                                               dar activo de baja  
def darActivoPorDeBaja(id):
        while True:
            try:
                data = BuscarIDdeActivos(id)
                Acceso = input("Ingrese su numero de CC: ")
                if MostrarIdReposable(Acceso):
                    data["idEstado"] = "2"
                    data["asignaciones"] = []
                    historial = {}
                    if not historial.get("NroId"):
                        historial["NroId"] = str(uuid.uuid4().hex[:4]) 
                    if not historial.get("Fecha"):
                        fecha_actual = datetime.datetime.now().strftime('%Y/%m/%d')
                        historial["Fecha"] = fecha_actual
                    if not historial.get("tipoMov"):
                        tipo = "2"
                        historial["tipoMov"] = tipo
                    if not historial.get("idRespMov"):
                        repo = MostrarIdReposable(Acceso)
                        letra = str(repo)
                        historial["idRespMov"] = letra
                    data.setdefault("historialActivos", []).append(historial)
                    peticion = requests.put(f"http://154.38.171.54:5501/activos/{id}", data=json.dumps(data, indent=4).encode("UTF-8"))
                    res = peticion.json()
                    res["Mensaje"] = "Activo Modificado"
                    return [res]
                    
            except requests.exceptions.RequestException as error:
                 animateTextDeLosMenusGreen("ID no encontrado", str(error))
                 return
                 
            except ValueError as error:
                 animateTextDeLosMenusGreen("ID no encontrado", str(error))
                 return
#********************************************************************************************************************************************************************************************************************
#                                                                              dar activo en garantia
def darActivoPorGarantia(id):
    while True:
        try:
            data = BuscarIDdeActivos(id)
            Acceso = input("Ingrese su numero de CC: ")
            if MostrarIdReposable(Acceso):
                data["idEstado"] = "3"
                data["asignaciones"] = []
                historial = {}
                if not historial.get("NroId"):
                    historial["NroId"] = str(uuid.uuid4().hex[:4]) 
                if not historial.get("Fecha"):
                    fecha_actual = datetime.datetime.now().strftime('%Y/%m/%d')
                    historial["Fecha"] = fecha_actual
                if not historial.get("tipoMov"):
                    tipo = "3"
                    historial["tipoMov"] = tipo
                if not historial.get("idRespMov"):
                    repo = MostrarIdReposable(Acceso)
                    letra = str(repo)
                    historial["idRespMov"] = letra
                    
            data.setdefault("historialActivos", []).append(historial)
            peticion = requests.put(f"http://154.38.171.54:5501/activos/{id}", data=json.dumps(data, indent=4).encode("UTF-8"))
            res = peticion.json()
            res["Mensaje"] = "Activo Modificado"
            return [res]
                    
        except requests.exceptions.RequestException as error:
                animateTextDeLosMenusGreen("ID no encontrado", str(error))
                return
                
        except ValueError as error:
                animateTextDeLosMenusGreen("ID no encontrado", str(error))
                return
#*****************************************************************************************************************************************************************************************************************
#                                                                            reasignar activo
def reasignarActivo(id):
    dificil = BuscarIDdeActivos(id)
    Acceso = input("Ingrese su numero de CC: ")
    if VerificacionDeIdentidad(Acceso)is not None:
        if dificil["idEstado"] == "1":
            estado ="1"
            dificil["idEstado"] = estado
            dificil["asignaciones"] = []
            historial = {}
            if not historial.get("NroId"):
                historial["NroId"] = str(uuid.uuid4().hex[:4]) 
            if not historial.get("Fecha"):
                fecha_actual = datetime.datetime.now().strftime('%Y/%m/%d')
                historial["Fecha"] = fecha_actual
            if not historial.get("tipoMov"):
                tipo = "4"
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
                        opcion = int(input("Ingrese el tipo de reasignación: "))
                        if opcion == 1:
                            tipoPerso = "Personal"
                            datos["TipoAsignacion"] = tipoPerso
                        elif opcion == 2:
                            tipoZon = "Zona"
                            datos["TipoAsignacion"] = tipoZon
                    if not datos.get("AsignadoA"):
                        if datos["TipoAsignacion"] == "Personal":
                            animateTextDeLosMenusYellow(tabulate(TablaPersonal(), headers="keys", tablefmt="double_outline"))
                            Asig1 = input("INGRESE EL ID DE LA PERSONA QUE QUIERE REASIGNAR: ")
                            datos["AsignadoA"] = Asig1
                            break
                        elif datos["TipoAsignacion"] == "Zona":
                            animateTextDeLosMenusYellow(tabulate(TablaZona(), headers="keys", tablefmt="double_outline"))
                            Asig2 = input("  INGRESE EL ID DE LA ZONA QUE QUIERE REASIGNAR: ")
                            datos["AsignadoA"] = Asig2
                            break
                except Exception as error:
                    animateTextDeLosMenusGreen(str(error))
            dificil.setdefault("asignaciones", []).append(datos)
            peticion = requests.put(f"http://154.38.171.54:5501/activos/{id}", data=json.dumps(dificil, indent=4).encode("UTF-8"))
            res = peticion.json()
            res["Mensaje"] = "Activo Actualizado con Reasignación"
            return [res]
        else:
            animateTextDeLosMenusGreen('''NO SE PUEDE REASIGNAR PORQUE EL ACTIVO NO ESTA EN ESTADO ASIGNADO''')
    else:
        animateTextDeLosMenusGreen('''
                     USTED NO TIENE PERMISOS PARA ACEDER A LA REASIGNACIÓN DE ACTIVOS         ''')