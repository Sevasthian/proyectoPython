import requests
def BuscarIDdePersonal(id):
    try:
        peticion = requests.get(f"http://154.38.171.54:5502/personas/{id}")
        peticion.raise_for_status()  
        return [peticion.json()]
    except requests.exceptions.RequestException as e:
        print("Error al realizar la solicitud HTTP:", e)
        return []  
    
def BuscarPersonal(id):
    data = BuscarIDdePersonal(id)
    list = []
    for sev in data:
        getAllAc={

                "Numero de IDENTIDAD": sev.get('nroId (CC, Nit)'),
                "Nombre": sev.get('Nombre'),
                "Email": sev.get('Email'),
                "Telefonos": sev.get('Telefonos')
          }
        list.append(getAllAc)
    return list
