import re
import requests
import json
def DataZonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/zonas/")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  

def BuscarNombreZonas(Nombre):
    for val in DataZonas():
        if val.get("nombreZona")  != Nombre:
            return [val] 


        
# def AddZona():
#     producto = {}
#     while True:
#         try:
#             if not producto.get("nombreZona"):
#                 codigo = input("Ingrese el Nombre de la zona: ")
#                 if re.match(r'^[A-Z]', codigo)is not None:
#                     if BuscarNombreZonas(codigo):
#                         raise Exception("El nombre ingresado ya existe.")
#                     else:
#                         producto["nombreZona"] = codigo
#                 else:
#                     raise Exception(f"El nombre no cumple con el estandar establecido, recuerde que el nombre de las zonas empiezan con mayúsculas.")
                
#             if not producto.get("totalCapacidad"):
#                 nombre = input(f"Ingrese la capacidad de la zona: ")
#                 if re.match(r'^\d+$', nombre)is not None:
#                     producto["totalCapacidad"] = nombre
#                     break
#                 else:
#                     raise Exception("Capacidad no valido, recuerde que son numeros positivos lo que se ingresa.")
#         except Exception as error:
#             print(error)     
#     peticion = requests.post("http://154.38.171.54:5007/pedidos", data=json.dumps(producto, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Zona Guardada"
#     return [res]


# def AddZona():
#     producto = {}
#     while True:
#         try:
#             if not producto.get("nombreZona"):
#                 codigo = input("Ingrese el Nombre de la zona: ")
#                 if re.match(r'^[A-Z]', codigo) is not None:
#                     if BuscarNombreZonas(codigo):
#                         raise Exception("El nombre ingresado ya existe.")
#                     else:
#                         producto["nombreZona"] = codigo
#                 else:
#                     raise Exception(f"El nombre no cumple con el estandar establecido, recuerde que el nombre de las zonas empiezan con mayúsculas.")
                
#             if not producto.get("totalCapacidad"):
#                 nombre = input(f"Ingrese la capacidad de la zona: ")
#                 if re.match(r'^\d+$', nombre) is not None:
#                     producto["totalCapacidad"] = nombre
#                 else:
#                     raise Exception("Capacidad no valido, recuerde que son numeros positivos lo que se ingresa.")
            
#             guardar_zona(producto)
#             return {"Mensaje": "Zona Guardada"}
            
#         except Exception as error:
#             print(error)                     
        
    
# def guardar_zona(producto):
#     peticion = requests.post("http://154.38.171.54:5502/zonas/", data=json.dumps(producto, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     return res


def AddZona(nombre, capacidad):
    while True:
        url = "http://154.38.171.54:5502/zonas/"   
        try:
                if re.match(r'^[A-Z]', nombre) and re.match(r'^\d+$', capacidad):
                    datos_zona = {"nombreZona": nombre, "totalCapacidad": capacidad}
                    try:
                        respuesta = requests.post(url, data=json.dumps(datos_zona))
                        respuesta.raise_for_status()
                        return respuesta.json()
                    
                    
                    except requests.exceptions.RequestException as e:
                        print("Error al realizar la solicitud HTTP:", e)
                        return None
                else:
                    if not re.match(r'^[A-Z]', nombre):
                        print("El nombre de la zona debe comenzar con mayúscula.")
                    if not re.match(r'^\d+$', capacidad):
                        print("La capacidad de la zona debe contener solo números.")
                    return None
        except Exception as error:
            print(error) 
        break
    

    # def agregar_zona(nombre, capacidad):
    # url = "http://154.38.171.54:5502/zonas/"

                
    # # Verificar si el nombre comienza con mayúscula y si la capacidad contiene solo números
    # if re.match(r'^[A-Z].*$', nombre) and re.match(r'^\d+$', capacidad):
    #     datos_zona = {"nombreZona": nombre, "totalCapacidad": capacidad}
    #     try:
    #         respuesta = requests.post(url, data=json.dumps(datos_zona))
    #         respuesta.raise_for_status()
    #         return respuesta.json()
    #     except requests.exceptions.RequestException as e:
    #         print("Error al realizar la solicitud HTTP:", e)
    #         return None
    # else:
    #     if not re.match(r'^[A-Z].*$', nombre):
    #         print("El nombre de la zona debe comenzar con mayúscula.")
    #     if not re.match(r'^\d+$', capacidad):
    #         print("La capacidad de la zona debe contener solo números.")
    #     return None
def GuardarClientes():
    cliente = dict()
    while True:
        try:
            if not cliente.get("codigo_cliente"):
                codigo = input(f"Escriba el codigo del cliente: ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    if GC.getOneClienteCodigo(codigo):
                        raise Exception("El codigo del cliente ya existe.")
                    else:
                        cliente["codigo_cliente"] = codigo
                else:
                    raise Exception("Codigo ingresado no valido, asegurese de ingresar solo dígitos numéricos")
                
            if not cliente.get("nombre_cliente"):
                nombre = input(f"Ingrese el nombre del cliente: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre) is not None:
                    cliente["nombre_cliente"] = nombre
                else:
                    raise Exception("Nombre no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not cliente.get("nombre_contacto"):
                nombreContacto = input(f"Ingrese el nombre contacto del cliente: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombreContacto) is not None:
                    cliente["nombre_contacto"] = nombreContacto
                else:
                    raise Exception("Nombre del contacto no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")

            if not cliente.get("apellido_contacto"):
                ApellidoContacto = input(f"Ingrese el apellido contacto del cliente: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', ApellidoContacto) is not None:
                    cliente["apellido_contacto"] = ApellidoContacto
                else:
                    raise Exception("Apellido del contacto no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not cliente.get("telefono"):
                telefono = input("Ingrese el número de telefono: ")
                if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$', telefono) is not None:
                    if GC.getAllTelefono(telefono):
                        raise Exception("El telefono ingresado ya existe.")
                    else:
                        cliente["telefono"] = telefono
                else:
                    raise Exception("Telefono no valido ( ejm: 654352981 o 2 8005-7162 )")
                
            if not cliente.get("fax"):
                fax = input("Ingrese el Fax: ")
                if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$', fax) is not None:
                    cliente["fax"] = fax
                else:
                    raise Exception("Fax no valido ( ejm: 654352981 o 2 8005-7162 )")
                
            if not cliente.get("linea_direccion1"):
                linea_direccion1 = input(f"Ingrese la linea de direccion 1: ")
                cliente["linea_direccion1"] = linea_direccion1

            if not cliente.get("linea_direccion2"):
                linea_direccion2 = input(f"Ingrese la linea de direccion 2: ")
                cliente["linea_direccion2"] = linea_direccion2

            if not cliente.get("ciudad"):
                ciudad = input(f"Ingrese la ciudad: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', ciudad) is not None:
                    cliente["ciudad"] = ciudad
                else:
                    raise Exception("Ciudad no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not cliente.get("region"):
                region = input(f"Ingrese la Region: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', region) is not None:
                    cliente["region"] = region
                else:
                    raise Exception("Region no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not cliente.get("pais"):
                pais = input(f"Ingrese el pais: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', pais) is not None:
                    cliente["pais"] = pais
                else:
                    raise Exception("Pais no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not cliente.get("codigo_postal"):
                codigo_postal = input("Ingrese el Codigo postal: ")
                if re.match(r'^\d{4,5}$', codigo_postal) is not None:
                    cliente["codigo_postal"] = codigo_postal
                else:
                    raise Exception("Codigo postal no valido, asegurese de ingresar 4 o 5 dígitos numéricos")
                
            if not cliente.get("codigo_empleado_rep_ventas"):
                codigo_empleado_rep_ventas = input(f"Escriba el codigo del representante de ventas: ")
                if re.match(r'^[0-9]+$', codigo_empleado_rep_ventas) is not None:
                    codigo_empleado_rep_ventas = int(codigo_empleado_rep_ventas)
                    cliente["codigo_empleado_rep_ventas"] = codigo_empleado_rep_ventas
                else:
                    raise Exception("Codigo ingresado no valido, asegurese de ingresar solo dígitos numéricos")
                
            if not cliente.get("limite_credito"):
                limite_credito = input(f"Escriba el limite de credito: ")
                if re.match(r'^[0-9]+$', limite_credito) is not None:
                    limite_credito = float(limite_credito)
                    cliente["limite_credito"] = limite_credito
                    break
                else:
                    raise Exception("Limite de credito ingresado no valido, asegurese de ingresar solo dígitos numéricos")
                                   
        except Exception as error:
            print(error)