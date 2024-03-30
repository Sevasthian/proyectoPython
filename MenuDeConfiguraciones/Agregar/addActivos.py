import json
import requests
from tabulate import tabulate
import uuid
import os
import re
from colorama import init, Fore, Style
import time
def DataMarcas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/marcas")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  
def DataCategoria():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/categoriaActivos")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  
def DataTipoDeActivo():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/tipoActivos")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  
    
def TablaTipoActivo():
    data = DataTipoDeActivo()
    list = []
    for sev in data:
        getAllAc={

                "ID del tipo de activo": sev.get('id'),
                "Nombre del tipo de activo": sev.get('Nombre'),
                
          }
        list.append(getAllAc)
    return list
def TablaCategoria():
    data = DataCategoria()
    list = []
    for sev in data:
        getAllAc={

                "ID de la Caregoria": sev.get('id'),
                "Nombre de la Categoria": sev.get('Nombre'),
                
          }
        list.append(getAllAc)
    return list
    
def TablaMarcas():
    data = DataMarcas()
    list = []
    for sev in data:
        getAllAc={

                "ID Marca": sev.get('id'),
                "Nombre de la Marca": sev.get('Nombre'),
                
          }
        list.append(getAllAc)
    return list

def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.RED + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
def DataActivos():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  

def BuscarNombreDelActivo(Nombre):
    for val in DataActivos():
        if val.get("Nombre")  == Nombre:
            return [val]
def BuscarNroID(Nro):
    for val in DataActivos():
        if val.get("NroItem") == Nro:
            return [val]


def AddActivo():
    Activo = {}
    while True:
        try:     
            if not Activo.get("NroItem"):
                nroID = input("Ingrese el número de de Item: ")
                if re.match(r'^\d+$', nroID) is not None:
                        if BuscarNroID(nroID):
                            raise Exception("El numero de Item ya existe")
                        else:
                            nroID = int(nroID)
                            Activo["NroItem"] = nroID
                else:
                    raise Exception("El numero de Item es incorrecto, recuerde que solo se ingresan números")
                
            if not Activo.get("CodTransaccion"):
                        Codtrasaccion = int(327)
                        Activo["CodTransaccion"] = Codtrasaccion
            if not Activo.get("NroSerial"):
                serial = input("Ingrese el numero del serial del activo:")
                if re.match(r'^[A-Z0-9]+$', serial) is not None:
                    Activo["NroSerial"] = serial
                else:
                    raise Exception("El número del serial esta incorrecto, recuerde que solo se aceptan número y letras en mayusculas ejemplo(400SN39189)")
            if not Activo.get("NroFormulario"):
                Formulario = input("Ingrese el número el número de formulario: ")
                if re.match(r'^\d+$', Formulario) is not None:
                    Formulario = int(Formulario)
                    Activo["NroFormulario"] = Formulario
                else:
                    raise Exception("Número de formulario incorrecto, recuerde ingresar solo se ingresan numeros")
            if not Activo.get("Nombre"):
                Nom = input("Ingrese el nombre del activo: ")
                Activo["Nombre"] = Nom
            if not Activo.get("Proveedor"):
                # Proverdor = str("Compumax Computer")
                Activo["Proveedor"] = "Compumax Computer "
            if not Activo.get("EmpresaResponsable"):
                Empresa = str("Campuslands")
                Activo["EmpresaResponsable"] = Empresa
            if not Activo.get("idMarca"):
                animateTextDeLosMenus(tabulate(TablaMarcas(), headers="keys", tablefmt="double_outline"))
                IdMarca = input("Ingrese el ID de la marca según la tabla: ")
                if re.match(r"[1-7]+", IdMarca) is not None:
                    Activo["IdMarca"] = IdMarca
                else:
                    raise Exception("Ingrese algun ID que estan en la tabla")
            if not Activo.get("idCategoria"):
                animateTextDeLosMenus(tabulate(TablaCategoria(), headers="keys", tablefmt="double_outline"))
                IdCategoria = input("Ingrese una el ID de una categoria que aparesca en la tabla:")
                if re.match(r"[1-3]+", IdCategoria) is not None:
                    Activo["idCategoria"]= IdCategoria
                else:
                    raise Exception("Ingrese algún ID que aparesca en la tabla")
            if not Activo.get("idTipo"):
                animateTextDeLosMenus(tabulate(TablaTipoActivo(), headers="keys", tablefmt="double_outline"))
                IdTipo = input("Ingrese el ID del tipo de activo que va a agregar:")
                if re.match(r"[1-8]+",IdTipo) is not None:
                    Activo["idTipo"] = IdTipo
                else:
                    raise Exception("Ingrese algún ID que aparesca en la tabla")
            if not Activo.get("ValorUnitario"):
                ValorUnita = input("Ingrese el valor unitario del activo :")
                if re.match(r"^[1-9][0-9]*$",ValorUnita) is not None:
                    Activo["ValorUnitario"] = ValorUnita
                else:
                    raise Exception("El valor unitario deben ser números ejemplo(10000)")
            if not Activo.get("idEstado"):
                IdEstado = str("0")
                Activo["idEstado"] = IdEstado
            if not Activo.get("id"):
                Activo["id"] = str(uuid.uuid4().hex[:4])
            if not Activo.get("historialActivos"):
                historialAc = []
                Activo["historialActivos"] = historialAc
            if not Activo.get("asignaciones"):
                asig = []
                Activo["asignaciones"] = asig
                break                                   
        except Exception as error:
            print(error)
    peticion = requests.post("http://154.38.171.54:5502/activos/", data=json.dumps(Activo, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Activo Guardado"
    return [res]

