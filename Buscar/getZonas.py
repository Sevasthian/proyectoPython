import requests
def BuscarIDdeZonas(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/zonas/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  
    
def BuscarZonas(id):
    list = []
    for sev in BuscarIDdeZonas(id):
        getAllAc={

                "Nombre de la Zona": sev.get('nombreZona'),
                "Coddigo Campus": sev.get('totalCapacidad'),
                "ID": sev.get('id')
          }
        list.append(getAllAc)
    return list

