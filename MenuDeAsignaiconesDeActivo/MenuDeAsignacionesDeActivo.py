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
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.YELLOW + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
#*****************************************************************************************************************************************************************************************************************************
#                                                                                        busquedas
def BuscarIDActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Data de activos no encontrado", str(e))
        return [] 
def DataPersonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Data personas no encontrado", str(e))
        return []  
def BuscarIDdeActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("EL ACTIVO NO EXITE:", str(e))
        return []  
def DataZonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", str(e))
        return []  
def DataTipoDePersonal():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP: ", str(e))
        return []  
def DataTipoDeZona():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/zonas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP: ", str(e))
        return []  
#***************************************************************************************************************************************************************************************************************************************************
#                                                                                       filtros
def VerificacionDeIdentidad(CC):
    try:
        for val in DataPersonas():
            if (val.get("nroId (CC, Nit)")  == CC and val.get("Nombre") == "Karen Celis") or (val.get("nroId (CC, Nit)") and  val.get("Nombre") == "Juan Jose Lizarazo"):
                return val
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Verificamos tu identidad y no perteneceses a los alministradores: ", str(e))
        return []
def MostrarIdReposable(cc):
    try:
        for persona in DataPersonas():
            if persona.get("nroId (CC, Nit)") == cc:
                return persona.get("id")
        return None
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Tu numero de CC no se encuentra en la base de datos: ", str(e))
        return []
def BuscarNombreZonas(Nombre):
    try:
        for val in DataZonas():
            if val.get("nombreZona")  == Nombre:
                return [val]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("El nombre de la zona no esta en la base de datos: ", str(e))
        return []
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
#                                                                                          creal asignaciones
def CrearAsignacion(id):
    dificil = BuscarIDdeActivos(id)
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
                        animateTextDeLosMenus('''         
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
                            animateTextDeLosMenus(tabulate(TablaPersonal(), headers="keys", tablefmt="double_outline"))
                            Asig1 = input("Ingrese el ID de la persona que quiere asignar: ")
                            datos["AsignadoA"] = Asig1
                            break
                        elif datos["TipoAsignacion"] == "Zona":
                            animateTextDeLosMenus(tabulate(TablaZona(), headers="keys", tablefmt="double_outline"))
                            Asig2 = input("Ingrese el ID de la zona que quiere asignar: ")
                            datos["AsignadoA"] = Asig2
                            break
                except Exception as error:
                    animateTextDeLosMenus(str(error))
            dificil.setdefault("asignaciones", []).append(datos)
            peticion = requests.patch(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(dificil, indent=4).encode("UTF-8"))
            res = peticion.json()
            res["Mensaje"] = "Activo Actualizado con Asignación"
            return [res]
        else:
            animateTextDeLosMenus('''NO SE PUEDE ASIGNAR PORQUE EL ACTIVO NO ESTA EN ESTADO NO ASIGNADO''')
    else:
        animateTextDeLosMenus('''
                     POR MOTIVOS DE SEGURIDAD SOLO PERSONAL AUTORIZADO PUEDE CREAR UNA ASIGNACIÓN        ''')
#************************************************************************************************************************************************************************************************************************************************
#                                                                                               

def BusActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("EL ACTIVO NO EXITE:", str(e))
        return []  
    
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
