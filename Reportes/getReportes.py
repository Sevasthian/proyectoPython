#import
import requests
import json
import time
#diseño
from tabulate import tabulate
from colorama import init, Fore, Style
#***********************************************************************************************************************************************************************************************
#                                                                                           colores
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
#***********************************************************************************************************************************************************************************************
#                                                                                          busquedas
def BuscarIDdeActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/activos/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("No se encuentra en la data")
        return [] 
def BuscarIDdeActivosDehistoria(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5501/activos/{id}")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("No se encuentra en la data")
        return []  
def getAllDataActivos():
    try:
            peticion =  requests.get("http://154.38.171.54:5501/activos")
            data = peticion.json()
            return data
    except requests.RequestException as e:
            animateTextDeLosMenusGreen("Error en la solicitud HTTP:")
            return []
    except ValueError as e:
            animateTextDeLosMenusGreen("Error al cargar JSON:")
            return []
def getAllDataIdMarca():
        try:
                peticion =  requests.get("http://154.38.171.54:5501/marcas")
                data = peticion.json()
                return data
        except requests.RequestException as e:
                animateTextDeLosMenusGreen("Error en la solicitud HTTP:")
                return []
        except ValueError as e:
                animateTextDeLosMenusGreen("Error al cargar JSON:")
        return []
def getAllDataCategoria():
    try:
                peticion =  requests.get("http://154.38.171.54:5501/categoriaActivos/")
                data = peticion.json()
                return data
    except requests.RequestException as e:
                animateTextDeLosMenusGreen("Error en la solicitud HTTP:")
                return []
    except ValueError as e:
                animateTextDeLosMenusGreen("Error al cargar JSON:")
    return []
#*********************************************************************************************************************************************************************************************
#                                                                                       filtros
def getCategoria(categoria):
    try:
        categorias = []
        for val in getAllDataActivos():
            if val.get("idCategoria") == categoria:
                categorias.append(val)
        return categorias
    except requests.exceptions.RequestException as e:
            animateTextDeLosMenusGreen("ERROR")
            return []
def getAllValidosdeAsignaciones():
    try:
        asignaciones_presentes = []
        for val in getAllDataActivos():
            asignaciones = val.get("asignaciones")
            if asignaciones: 
                asignaciones_presentes.append(val)
        return asignaciones_presentes
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("ERROR")
        return []
def getEstado():
    try:
        categorias = []
        for val in getAllDataActivos():
            if val.get("idEstado") == "2":
                categorias.append(val)
        return categorias
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("ERROR")
        return []
    
def SoloMuestraDatosDeAsignaciones():
    try:
        asignaciones_presentes = []
        for activo in getAllDataActivos():
            asignaciones = activo.get("asignaciones")
            if asignaciones:
                asignaciones_presentes.append(asignaciones)
        return asignaciones_presentes
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("ERROR")
        return []
def SoloMuestraDatosDeHIstorial(id):
    try:
        historiales = []
        for activo in BuscarIDdeActivos(id):
            for his in activo.get("historialActivos", []):
                historiales.append(his)
        return historiales
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenusGreen("ERROR, No se encuentra data")
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
                               animateTextDeLosMenusGreen(''' 
                                                NO HAY ACTIVOS CON ESTA CATEGORIA''')
                        return activos
                except Exception as error:
                       animateTextDeLosMenusGreen(str(error))
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
        data = getAllValidosdeAsignaciones()
        for sev in data:
          allActivos.append({
                "NroSerial": sev.get('NroSerial'),
                "Nombre": sev.get('Nombre'),
                           })
        return allActivos
def pendejo():
    try:
        locuras = []
        ñao = SoloMuestraDatosDeAsignaciones()
        for pen in ñao:
               locuras.append({
                      "NroAsignacion": pen[0].get('NroAsignacion'),
                      "FechaAsignacion": pen[0].get('FechaAsignacion'),
                      "TipoAsignacion" : pen[0].get('TipoAsignacion'),
                      "AsignadoA": pen[0].get('AsignadoA')
               })
        return locuras
    except KeyError:
        animateTextDeLosMenusGreen("algun pedejo daño json")
        # Manejar la excepción si 'NroAsignacion' no está presente en el primer elemento de 'pen'
        return None
#****************************************************************************************************************************************************************************************************
#                                                                          listar historial de movimiento de activo
def getActivo(id):
        allActivos = []
        for sev in BuscarIDdeActivos(id):
          getAllAc={
                "NroSerial": sev.get('NroSerial'),
                "Nombre": sev.get('Nombre')
                                    }
          allActivos.append(getAllAc)
        return allActivos
def getAllHistoriaDeMov(id):
    histori = []
    data = SoloMuestraDatosDeHIstorial(id)
    for sev in data:
            histori.append({
                  "NroId": sev.get('NroId'),
                  "Fecha" : sev.get('Fecha'),
                  "tipoMov" : sev.get('tipoMov'),
                  "idRespMov": sev.get('idRespMov')
            })
    return  histori