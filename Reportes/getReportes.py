import requests
from tabulate import tabulate
import json
from colorama import init, Fore, Style
import time
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.YELLOW + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
def BuscarIDdeActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("Error al realizar la solicitud HTTP:", e)
        return []  
    

def getCategoria(categoria):
    categorias = []
    for val in getAllDataActivos():
        if val.get("idCategoria") == categoria:
            categorias.append(val)
    return categorias

def getEstado():
    categorias = []
    for val in getAllDataActivos():
        if val.get("idEstado") == "2":
            categorias.append(val)
    return categorias
def getAsignaciones():
    asignaciones_presentes = []
    for val in getAllDataActivos():
        asignaciones = val.get("asignaciones")
        if asignaciones: 
            asignaciones_presentes.append(val)
    return asignaciones_presentes
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

def getAllMarcas():
    allMarca = []
    for dia in getAllDataIdMarca():
            getAllMar = {
                    "ID de la marca": dia.get('id'),
                    "nombreDelProducto": dia.get('Nombre')
                      }
            allMarca.append(getAllMar)
    return allMarca

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


def getAllActivosAsignaciones():
        allActivos = []
        data = getAsignaciones()
        for sev in data:
          allActivos.append({
                "NroSerial": sev.get('NroSerial'),
                "Nombre": sev.get('Nombre'),
                "Asignacion": sev.get('asignaciones')
                                    })
          
        return allActivos
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
       
       


