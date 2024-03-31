#esto es diseño
from tabulate import tabulate
from colorama import init, Fore, Style
#import
import requests
import json
import datetime
import uuid
import time
#*******************************************************************************************************************************************************************************************************************************************
#                                                               diseño
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.YELLOW + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 


def VerificacionDeIdentidad(CC):
    for val in DataPersonas():
        if (val.get("nroId (CC, Nit)")  == CC and val.get("Nombre") == "Karen Celis") or (val.get("nroId (CC, Nit)") and  val.get("Nombre") == "Juan Jose Lizarazo"):
            return val
def MostrarIdReposable(cc):
        data = DataPersonas()
        for persona in data:
            if persona.get("nroId (CC, Nit)") == cc:
                return persona.get("id")
        return None 

def DataPersonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", str(e))
        return []  


def BuscarIDdeActivos(id):
    peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
    return peticion.json() if peticion.ok else []

def DataZonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", str(e))
        return []  

def BuscarNombreZonas(Nombre):
    for val in DataZonas():
        if val.get("nombreZona")  == Nombre:
            return [val]


def DataTipoDePersonal():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", str(e))
        return []  
    
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


def DataTipoDeZona():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/zonas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", str(e))
        return []  
    
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
def BuscarIDdeActivos(id):
        peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        peticion.raise_for_status()  
        return peticion.json()

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
                    historial["NroId"] = str(uuid.uuid4().hex[:4])  # Utilizamos el mismo ID del activo para el historial
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
                    break
                data.setdefault("historialActivos", []).append(historial)
            peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data, indent=4).encode("UTF-8"))
            res = peticion.json()
            res["Mensaje"] = "Activo Modificado"
            return [res]
                    
        except requests.exceptions.RequestException as error:
                animateTextDeLosMenus("ID no encontrado", str(error))
                return
                
        except ValueError as error:
                animateTextDeLosMenus("ID no encontrado", str(error))
                return
    
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
                    peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data, indent=4).encode("UTF-8"))
                    res = peticion.json()
                    res["Mensaje"] = "Activo Modificado"
                    return [res]
                    
            except requests.exceptions.RequestException as error:
                 animateTextDeLosMenus("ID no encontrado", str(error))
                 return
                 
            except ValueError as error:
                 animateTextDeLosMenus("ID no encontrado", str(error))
                 return
        

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
                    historial["NroId"] = str(uuid.uuid4().hex[:4])  # Utilizamos el mismo ID del activo para el historial
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
            peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(data, indent=4).encode("UTF-8"))
            res = peticion.json()
            res["Mensaje"] = "Activo Modificado"
            return [res]
                    
        except requests.exceptions.RequestException as error:
                animateTextDeLosMenus("ID no encontrado", str(error))
                return
                
        except ValueError as error:
                animateTextDeLosMenus("ID no encontrado", str(error))
                return

def reasignarActivo(id):
    dificil = BuscarIDdeActivos(id)
    Acceso = input("Ingrese su numero de CC: ")
    if VerificacionDeIdentidad(Acceso)is not None:
        if dificil["idEstado"] == "1":
            estado ="1"
            dificil["idEstado"] = estado
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
                        animateTextDeLosMenus('''         
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
                            animateTextDeLosMenus(tabulate(TablaPersonal(), headers="keys", tablefmt="double_outline"))
                            Asig1 = input("INGRESE EL ID DE LA PERSONA QUE QUIERE REASIGNAR: ")
                            datos["AsignadoA"] = Asig1
                            break
                        elif datos["TipoAsignacion"] == "Zona":
                            animateTextDeLosMenus(tabulate(TablaZona(), headers="keys", tablefmt="double_outline"))
                            Asig2 = input("  INGRESE EL ID DE LA ZONA QUE QUIERE REASIGNAR: ")
                            datos["AsignadoA"] = Asig2
                            break
                except Exception as error:
                    animateTextDeLosMenus(str(error))
            dificil.setdefault("asignaciones", []).append(datos)
            peticion = requests.put(f"http://154.38.171.54:5502/activos/{id}", data=json.dumps(dificil, indent=4).encode("UTF-8"))
            res = peticion.json()
            res["Mensaje"] = "Activo Actualizado con Reasignación"
            return [res]
        else:
            animateTextDeLosMenus('''NO SE PUEDE REASIGNAR PORQUE EL ACTIVO NO ESTA EN ESTADO ASIGNADO''')
    else:
        animateTextDeLosMenus('''
                     USTED NO TIENE PERMISOS PARA ACEDER A LA REASIGNACIÓN DE ACTIVOS         ''')