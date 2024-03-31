from tabulate import tabulate
from colorama import init, Fore, Style
import time
import requests
import json
def animateTextDeLosMenus(text):
    for char in text:
        print(Fore.YELLOW + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
    
def animateTextD(text):
    for char in text:
        print(Fore.RED + char, end="", flush=True)
        time.sleep(0.001) 
    print(Style.DIM) 
def BuscarIDdePersonal(id):
    peticion = requests.get(f"http://154.38.171.54:5502/personas/{id}")
    return peticion.json() if peticion.ok else []

def updatePersonal(id):
    data = BuscarIDdePersonal(id)
    if data is None:
        animateTextDeLosMenus(f"ID del personal no encontrado.")
        return
    
    while True:
        try:
            print()
            animateTextDeLosMenus("\nDatos para modificar:")
            for i, (key, value) in enumerate(data.items()):
                animateTextDeLosMenus(f"{i+1}. {key}: {value}")

            opcion = int(input("\n Seleccione una opción: "))
            if opcion < 1 or opcion > len(data):
                print()
                animateTextDeLosMenus("Selección incorrecta")
                continue
            
            key_to_modify = list(data.keys())[opcion - 1]
            if key_to_modify == "id":
                animateTextDeLosMenus('''EL ID NO SE PUEDE MODIFICAR''')
                break
            
            if key_to_modify == "Telefonos":
                for i, (tipo_telefono, datos_telefono) in enumerate(data[key_to_modify][0].items(), start=1):
                    animateTextDeLosMenus(f"{i}. Tipo de teléfono: {tipo_telefono}") #hacer cambio de color
                    for telefono_key, telefono_value in datos_telefono.items():
                        animateTextD(f"{telefono_key}: {telefono_value}")# hacer cambio de color
                
                opcion_tel = int(input("Seleccione el tipo de teléfono a modificar: "))
                if opcion_tel < 1 or opcion_tel > len(data[key_to_modify][0]):
                    print()
                    animateTextDeLosMenus("Selección incorrecta")
                    continue
                
                tipo_seleccionado = list(data[key_to_modify][0].keys())[opcion_tel - 1]
                nuevo_numero = input(f"Ingrese el nuevo número de {tipo_seleccionado}: ")
                data[key_to_modify][0][tipo_seleccionado]["num"] = nuevo_numero
            else:
                new_value = input(f"Ingrese el nuevo valor para {key_to_modify}: ")
                data[key_to_modify] = new_value
            print()
            animateTextDeLosMenus("Datos actualizados:")
            for key, value in data.items():
                print()
            break

        except ValueError:
            print()
            animateTextDeLosMenus("Debe ingresar un número.")

    peticion = requests.put(f"http://154.38.171.54:5502/personas/{id}", data=json.dumps(data, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Personal Modificado"
    return [res]