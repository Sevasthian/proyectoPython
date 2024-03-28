import json
import requests
from tabulate import tabulate
import os
import re


def GuardarProducto():
    producto = {}
    while True:
        try:
            if not producto.get("codigo_producto"):
                codigo = input("Ingrese el codigo del producto: ")
                if re.match(r'^[A-Z]{2}-\d{3}$', codigo) is not None:
                    if getProductoCodigo(codigo):
                        raise Exception("El codigo ingresado ya existe.")
                    else:
                        producto["codigo_producto"] = codigo
                else:
                    raise Exception(f"El codigo no cumple con el estandar establecido ( ejm: XX-111 ).")
                
            if not producto.get("nombre"):
                nombre = input(f"Ingrese el nombre del producto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre) is not None:
                    producto["nombre"] = nombre
                else:
                    raise Exception("Nombre no valido, recuerde que todas las palabras deben iniciar con mayúsculas.")
                
            if not producto.get("gama"):
                gama = input("Ingrese la gama del producto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s.]*$', nombre) is not None:
                    asd = GG.getAllNombre(gama)
                    if asd:
                        producto["gama"] = gama
                    else:
                        raise Exception("Gamas validas: ( Herbaceas, Herramientas, Aromáticas, Frutales, Ornamentales )")
                else:
                    raise Exception("Gamas validas: ( Herbaceas, Herramientas, Aromáticas, Frutales, Ornamentales )")
                
            if not producto.get("dimensiones"):
                dimensiones = input("Ingrese las dimensiones del producto: ")
                if re.match(r'^\d+-\d+$', dimensiones) is not None:
                    producto["dimensiones"] = dimensiones
                else:
                    raise Exception("Dimensiones no válidas, la forma correcta es ( numero-numero ).")
                
            if not producto.get("proveedor"): 
                proveedor = input("Ingrese el proveedor: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s.]*$', proveedor) is not None:
                    producto["proveedor"] = proveedor
                else:
                    raise Exception("Proveedor no valido, recuerde que la primera palabra debe iniciar con mayúsculas.")
                
            if not producto.get("descripcion"):
                descripcion = input("Ingrese una descripción: ")
                producto["descripcion"] = descripcion
            
            if not producto.get("cantidadEnStock"):
                cantidad = input("Ingrese el precio de venta: ")
                if re.match(r'^[0-9]+$', cantidad) is not None:
                    cantidad = int(cantidad)
                    producto["cantidadEnStock"] = cantidad
                else:
                    raise Exception("Cantidad no valida, asegurese de ingresar solo dígitos numéricos.")
                
            if not producto.get("precio_venta"):
                PrecioVenta = input("Ingrese el precio de venta: ")
                if re.match(r'^[0-9]+$', PrecioVenta) is not None:
                    PrecioVenta = int(PrecioVenta)
                    producto["precio_venta"] = PrecioVenta
                else:
                    raise Exception("Precio de venta no valido, asegurese de ingresar solo dígitos numéricos.")
                
            if not producto.get("precio_proveedor"):
                PrecioProveedor = input("Ingrese el precio del proveedor: ")
                if re.match(r'^[0-9]+$', PrecioProveedor) is not None:
                    PrecioProveedor = int(PrecioProveedor)
                    producto["precio_proveedor"] = PrecioProveedor
                    break
                else:
                    raise Exception("Precio de proveedor no valido, asegurese de ingresar solo dígitos numéricos.")
        
        except Exception as error:
            print(error)                     
    
    peticion = requests.post("http://154.38.171.54:5008/actvos", data=json.dumps(producto, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]