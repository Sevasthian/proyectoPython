import json
import requests
from tabulate import tabulate
import os
import re
# def GuardarClientes():
#     cliente = dict()
#     while True:
#         try:
#             if not cliente.get("codigo_cliente"):
#                 codigo = input(f"Escriba el codigo del cliente: ")
#                 if re.match(r'^[0-9]+$', codigo) is not None:
#                     codigo = int(codigo)
#                     if getOneClienteCodigo(codigo):
#                         raise Exception("El codigo del cliente ya existe.")
#                     else:
#                         cliente["codigo_cliente"] = codigo
#                 else:
#                     raise Exception("Codigo ingresado no valido, asegurese de ingresar solo dígitos numéricos")
                
#             if not cliente.get("nombre_cliente"):
#                 nombre = input(f"Ingrese el nombre del cliente: ")
#                 if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre) is not None:
#                     cliente["nombre_cliente"] = nombre
#                 else:
#                     raise Exception("Nombre no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
#             if not cliente.get("nombre_contacto"):
#                 nombreContacto = input(f"Ingrese el nombre contacto del cliente: ")
#                 if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombreContacto) is not None:
#                     cliente["nombre_contacto"] = nombreContacto
#                 else:
#                     raise Exception("Nombre del contacto no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")

#             if not cliente.get("apellido_contacto"):
#                 ApellidoContacto = input(f"Ingrese el apellido contacto del cliente: ")
#                 if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', ApellidoContacto) is not None:
#                     cliente["apellido_contacto"] = ApellidoContacto
#                 else:
#                     raise Exception("Apellido del contacto no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
#             if not cliente.get("telefono"):
#                 telefono = input("Ingrese el número de telefono: ")
#                 if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$', telefono) is not None:
#                     if getAllTelefono(telefono):
#                         raise Exception("El telefono ingresado ya existe.")
#                     else:
#                         cliente["telefono"] = telefono
#                 else:
#                     raise Exception("Telefono no valido ( ejm: 654352981 o 2 8005-7162 )")
                
#             if not cliente.get("fax"):
#                 fax = input("Ingrese el Fax: ")
#                 if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$', fax) is not None:
#                     cliente["fax"] = fax
#                 else:
#                     raise Exception("Fax no valido ( ejm: 654352981 o 2 8005-7162 )")
                
#             if not cliente.get("linea_direccion1"):
#                 linea_direccion1 = input(f"Ingrese la linea de direccion 1: ")
#                 cliente["linea_direccion1"] = linea_direccion1

#             if not cliente.get("linea_direccion2"):
#                 linea_direccion2 = input(f"Ingrese la linea de direccion 2: ")
#                 cliente["linea_direccion2"] = linea_direccion2

#             if not cliente.get("ciudad"):
#                 ciudad = input(f"Ingrese la ciudad: ")
#                 if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', ciudad) is not None:
#                     cliente["ciudad"] = ciudad
#                 else:
#                     raise Exception("Ciudad no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
#             if not cliente.get("region"):
#                 region = input(f"Ingrese la Region: ")
#                 if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', region) is not None:
#                     cliente["region"] = region
#                 else:
#                     raise Exception("Region no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
#             if not cliente.get("pais"):
#                 pais = input(f"Ingrese el pais: ")
#                 if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', pais) is not None:
#                     cliente["pais"] = pais
#                 else:
#                     raise Exception("Pais no valida, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
#             if not cliente.get("codigo_postal"):
#                 codigo_postal = input("Ingrese el Codigo postal: ")
#                 if re.match(r'^\d{4,5}$', codigo_postal) is not None:
#                     cliente["codigo_postal"] = codigo_postal
#                 else:
#                     raise Exception("Codigo postal no valido, asegurese de ingresar 4 o 5 dígitos numéricos")
                
#             if not cliente.get("codigo_empleado_rep_ventas"):
#                 codigo_empleado_rep_ventas = input(f"Escriba el codigo del representante de ventas: ")
#                 if re.match(r'^[0-9]+$', codigo_empleado_rep_ventas) is not None:
#                     codigo_empleado_rep_ventas = int(codigo_empleado_rep_ventas)
#                     cliente["codigo_empleado_rep_ventas"] = codigo_empleado_rep_ventas
#                 else:
#                     raise Exception("Codigo ingresado no valido, asegurese de ingresar solo dígitos numéricos")
                
#             if not cliente.get("limite_credito"):
#                 limite_credito = input(f"Escriba el limite de credito: ")
#                 if re.match(r'^[0-9]+$', limite_credito) is not None:
#                     limite_credito = float(limite_credito)
#                     cliente["limite_credito"] = limite_credito
#                     break
#                 else:
#                     raise Exception("Limite de credito ingresado no valido, asegurese de ingresar solo dígitos numéricos")
                                   
#         except Exception as error:
#             print(error)

#     peticion = requests.post("http://154.38.171.54:5001/cliente", data=json.dumps(cliente, indent=4).encode("UTF-8"))
#     res = peticion.json()
#     res["Mensaje"] = "Cliente Guardado"
#     return [res]