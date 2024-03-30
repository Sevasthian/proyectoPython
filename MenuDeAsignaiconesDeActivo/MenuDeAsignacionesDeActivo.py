import re
import requests
import json
import datetime
def DataZonas():
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/activos/")
        peticion.raise_for_status()  
        return peticion.json()
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  

def BuscarNombreZonas(Nombre):
    for val in DataZonas():
        if val.get("nombreZona")  == Nombre:
            return [val]



def CrearAsignacion():
    asignacion = DataZonas()
    if asignacion["idEstado"] == "0":
        while True:
            try:     
                if asignacion.get("asignaciones"):
                    datos = {}
                    if not datos.get("FechaAsignación"):
                        fecha_actual = datetime.datetime.now()
                        datos["FechaAsignación"] = fecha_actual
                    if not datos.get("TipoAsignacion"):
                        print('''               ELIJA EL TIPO DE ASIGNACIÓN
                                        1.) PERSONAL
                                        2.) ZONA


''')
                        opcion = int(input("Ingres el tipo de asignación: "))
                        if opcion == 1:
                            tipoPerso = "Personal"
                            datos["TipoAsignacion"] = tipoPerso
                        elif opcion == 2:
                            tipoZon = "Zona"
                            datos["TipoAsignacion"] = tipoZon
                    

















                if re.match(r'^[A-Z]', nombre) is not None:
                    if BuscarNombreZonas(nombre):
                        raise Exception("El nombre de la zona ingresado ya existe.")
                    else:
                        asignacion["nombreZona"] = nombre
                else:
                    raise Exception("Nombre no valido, recuerde que los nombres inician con mayuculas")
                
            if not asignacion.get("totalCapacidad"):
                capacidad = input("Ingrese la capacidad de la zona: ")
                if re.match(r'^\d+$', capacidad) is not None:
                    asignacion["totalCapacidad"] = capacidad
                    break
                else:
                    raise Exception("La capacidad de la zona solo se registran números")
                                   
        except Exception as error:
            print(error)
    peticion = requests.post("http://154.38.171.54:5502/zonas/", data=json.dumps(asignacion, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Zona Guardada"
    return [res]

# NroAsignacion
# • FechaAsignación
# • TipoAsignacion (Personal, Zona)
# • AsignadoA
# • Activos:
# o NroActivo
{
    "id": 556,
    "CodTransaccion": 327,
    "Nroserial": "Sin serial",
    "CodCampus": "JUA123",
    "NroFormulario": 966218327,
    "Nombre": "Teclado con luces ",
    "Proveedor": "Compumax Computer",
    "EmpresaResponsable": "Campuslands",
    "idMarca": "7",
    "idCategoria": "1",
    "idTipo": "1",
    "ValorUnitario": "70000",
    "idEstado": "0",
    "historialActivos": [],
    "asignaciones": []
  }