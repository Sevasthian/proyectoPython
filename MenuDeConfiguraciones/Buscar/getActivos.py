import requests
from colorama import init, Fore, Style
import time
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.GREEN + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
def BuscarIDdeActivos(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        animateTextDeLosMenus("EL ACTIVO NO EXITE")
        return [] 
    except AttributeError:
        animateTextDeLosMenus("Ingrese algún dato") 
def BuscarActivos():
    try:
        idActivo = input("Ingrese el id del activo : ")
        data = BuscarIDdeActivos(idActivo)
        list = []
        for sev in data:
            getAllAc={
    
                    "Numero Item": sev.get('NroItem'),
                    "Codigo Transaccion": sev.get('CodTransaccion'),
                    "Numero de Serial": sev.get('NroSerial'),
                    "Codigo Campus": sev.get('CodCampus'),
                    "Numero de Formulario": sev.get('NroFormulario'),
                    "Nombre": sev.get('Nombre'),
                    "Proveedor": sev.get('Proveedor'),
                    "Empresa Responsable": sev.get('EmpresaResponsable'),
                    "ID Marca": sev.get('idMarca'),
                    "ID Categoria": sev.get('idCategoria'),
                    "ID Tipo": sev.get('idTipo'),
                    "ID": sev.get('id')
            }
            list.append(getAllAc)
        return list
    except AttributeError:
        animateTextDeLosMenus("Debe ingresar algún dato")
