#import
import requests
import json
import time
#diseño
from tabulate import tabulate
from colorama import init, Fore, Style
#***********************************************************************************************************************************************************************************************
#                                                                                           colores
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.YELLOW + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
#***********************************************************************************************************************************************************************************************
#                                                                                          busquedas
def BuscarIDdeActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", e)
        return []  
def getAllDataActivos():
    try:
            peticion =  requests.get("http://154.38.171.54:5502/activos")
            data = peticion.json()
            return data
    except requests.RequestException as e:
            animateTextDeLosMenus("Error en la solicitud HTTP:", e)
            return []
    except ValueError as e:
            animateTextDeLosMenus("Error al cargar JSON:", e)
            return []
def getAllDataIdMarca():
        try:
                peticion =  requests.get("http://154.38.171.54:5502/marcas")
                data = peticion.json()
                return data
        except requests.RequestException as e:
                animateTextDeLosMenus("Error en la solicitud HTTP:", e)
                return []
        except ValueError as e:
                animateTextDeLosMenus("Error al cargar JSON:", e)
        return []
def getAllDataCategoria():
    try:
                peticion =  requests.get("http://154.38.171.54:5502/categoriaActivos/")
                data = peticion.json()
                return data
    except requests.RequestException as e:
                animateTextDeLosMenus("Error en la solicitud HTTP:", e)
                return []
    except ValueError as e:
                animateTextDeLosMenus("Error al cargar JSON:", e)
    return []
#*********************************************************************************************************************************************************************************************
#                                                                                       filtros
def getCategoria(categoria):
    categorias = []
    for val in getAllDataActivos():
        if val.get("idCategoria") == categoria:
            categorias.append(val)
    return categorias
def getAllValidosdeAsignaciones():
    try:
        asignaciones = []
        data = getAllDataActivos()  # Corregir llamada de función
        for sev in data:
            # Suponiendo que 'asignaciones' es un campo en sev
            if sev.get('asignaciones') is not None:  # Comprobar si 'asignaciones' existe y no es None
                asignaciones.append(sev.get('asignaciones'))  # Agregar 'asignaciones' a la lista
        return asignaciones
    except Exception as e:  # Manejar cualquier excepción, no solo requests.exceptions.RequestException
        print("Ha ocurrido un error:", e)
        return []
        
def getEstado():
    categorias = []
    for val in getAllDataActivos():
        if val.get("idEstado") == "2":
            categorias.append(val)
    return categorias
def SoloMuestraDatosDeAsignaciones():
    try:
        asignaciones_presentes = []
        for activo in getAllDataActivos():
            asignaciones = activo.get("asignaciones")
            if asignaciones:
                for asignacion in asignaciones:
                    asignaciones_presentes.append(asignacion)
        return asignaciones_presentes
    except requests.exceptions.RequestException as e:
        print("Tu número de CC no se encuentra en la base de datos: ")
        return []
#**************************************************************************************************************************************************************************************************
#                                                                                    tablas
def getAllMarcas():
    allMarca = []
    for dia in getAllDataIdMarca():
            getAllMar = {
                    "ID de la marca": dia.get('id'),
                    "nombreDelProducto": dia.get('Nombre')
                      }
            allMarca.append(getAllMar)
    return allMarca

#**************************************************************************************************************************************************************************************************
#                                                                                    listar todos los activos  
def getAllActivos():
    allActivos = []
    for sev in getAllDataActivos():
          getAllAc={
                 "ID": sev.get('id'),
                "NroSerial": sev.get('NroSerial'),
                "CodCampus": sev.get('CodCampus'),
                "Nombre": sev.get('Nombre'),
                "ID Marca": sev.get('idMarca'),
          }
          allActivos.append(getAllAc)
    return allActivos
#***************************************************************************************************************************************************************************************************
#                                                                                    listar activos por categoria
def getAllCategoria(categoria):
        while True:
                try:
                        activos = []
                        data = getCategoria(categoria)
                        for sev in data:
                                                activos.append({
                                                "NroItem": sev.get('NroItem'),
                                                "CodTransaccion": sev.get('CodTransaccion'),
                                                "NroSerial": sev.get('NroSerial'),
                                                "CodCampus": sev.get('CodCampus'),
                                                "NroFormulario": sev.get('NroFormulario'),
                                                "Nombre": sev.get('Nombre'),
                                                "Proveedor": sev.get('Proveedor'),
                                                "EmpresaResponsable": sev.get('EmpresaResponsable'),
                                                "idMarca": sev.get('idMarca'),
                                                "idCategoria": sev.get('idCategoria'),
                                                "idTipo": sev.get('idTipo'),
                                                "ValorUnitario": sev.get('ValorUnitario'),
                                                "idEstado": sev.get('idEstado'),
                                                "id": sev.get('id'),
                                        })
                                                
                        if not activos:
                               animateTextDeLosMenus(''' 
                                                NO HAY ACTIVOS CON ESTA CATEGORIA''')
                        return activos
                except Exception as error:
                       animateTextDeLosMenus(error)
#***************************************************************************************************************************************************************************************************
#                                                                          listar activos dados de baja por daños
def getAllDadosDeBajaPorDaño():
        activos = []
        data = getEstado()
        for sev in data:
                        activos.append({
                        "NroItem": sev.get('NroItem'),
                        "CodTransaccion": sev.get('CodTransaccion'),
                        "NroSerial": sev.get('NroSerial'),
                        "CodCampus": sev.get('CodCampus'),
                        "NroFormulario": sev.get('NroFormulario'),
                        "Nombre": sev.get('Nombre'),
                        "Proveedor": sev.get('Proveedor'),
                        "EmpresaResponsable": sev.get('EmpresaResponsable'),
                        "idMarca": sev.get('idMarca'),
                        "idCategoria": sev.get('idCategoria'),
                        "idTipo": sev.get('idTipo'),
                        "ValorUnitario": sev.get('ValorUnitario'),
                        "idEstado": sev.get('idEstado'),
                        "id": sev.get('id'),
                })
        return activos
#****************************************************************************************************************************************************************************************************
#                                                                         listar activos y asignaciones      
def getAllActivosAsignaciones():
        allActivos = []
        locuras = []
        data = getAllValidosdeAsignaciones()
        ñao = SoloMuestraDatosDeAsignaciones()
        for sev in data:
          allActivos.append({
                "NroSerial": sev.get('NroSerial'),
                "Nombre": sev.get('Nombre'),
                                    })
        for pen in ñao:
               locuras.append({
                      "NroAsignacion": pen.get('NroAsignacion'),
                      "FechaAsignacion": pen.get('FechaAsignacion'),
                      "TipoAsignacion" : pen.get('TipoAsignacion'),
                      "AsignadoA": pen.get('AsignadoA')
               })
        return(allActivos,locuras)
def convinacionesDeLaTablaAnteriorDeAsignaciones():
    allActivos, locuras = getAllActivosAsignaciones()
    
    # Indexar las asignaciones por NroSerial si está presente
    asignaciones_por_serial = {}
    for asignacion in locuras:
        serial = asignacion.get("NroSerial")
        if serial not in asignaciones_por_serial:
            asignaciones_por_serial[serial] = []
        asignaciones_por_serial[serial].append(asignacion)
    
    # Combinar datos de activos y asignaciones
    combined_data = []
    for activo in allActivos:
        serial = activo["NroSerial"]
        if serial in asignaciones_por_serial:
            for asignacion in asignaciones_por_serial[serial]:
                combined_data.append({
                    "NroSerial": serial,
                    "Nombre": activo.get("Nombre", ""),
                    "NroAsignacion": asignacion.get("NroAsignacion", ""),
                    "FechaAsignacion": asignacion.get("FechaAsignacion", ""),
                    "TipoAsignacion": asignacion.get("TipoAsignacion", ""),
                    "AsignadoA": asignacion.get("AsignadoA", "")
                })
        else:
            combined_data.append({
                "NroSerial": serial,
                "Nombre": activo.get("Nombre", ""),
                "NroAsignacion": "",
                "FechaAsignacion": "",
                "TipoAsignacion": "",
                "AsignadoA": ""
            })

    # Imprimir la tabla combinada
    print(tabulate(combined_data, headers="keys"))
#****************************************************************************************************************************************************************************************************
#                                                                          listar historial de movimiento de activo

       



def getAllHistorialDeMovDeActivo(id):
        allActivos = []

        for sev in BuscarIDdeActivos(id):
          getAllAc={
                "NroSerial": sev.get('NroSerial'),
                "Nombre": sev.get('Nombre'),
                "Historial de movimiento de activo": sev.get('historialActivos')
                                    }
          allActivos.append(getAllAc)
        return allActivos