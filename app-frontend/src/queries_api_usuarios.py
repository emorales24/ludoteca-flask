import requests

# API Backend
API_BASE = "http://localhost:5000"


def obtener_usuario(usr):
    response = requests.get(f"{API_BASE}/usuarios/{usr}")
    if response.status_code == 200:
        return response.json()
    return None

def validar_usuario(usr, contra_evaluar):
    response = requests.post(
        f"{API_BASE}/usuarios/validar/{usr}",
        json = {
            "contra_evaluar": contra_evaluar
        },
    )
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return "no_encontrado"
    elif response.status_code == 401:
        return "contra_incorrecta"

def actualizar_usuario(usuario, email, contra, nombre, apellido, calle, direccion, codigo_postal, ciudad, pais, usuario_viejo):
    response = requests.put(
        f"{API_BASE}/usuarios/update/{usuario_viejo}",
        json = {
            "usuario": usuario,
            "email": email,
            "contra": contra,
            "nombre": nombre,
            "apellido": apellido,
            "calle": calle,
            "direccion": direccion,
            "codigo_postal": codigo_postal,
            "ciudad": ciudad,
            "pais": pais,
        },
    )
    if response.status_code == 200:
        return True
    return None

def obtener_metodos_pago(usuario_id):
    response = requests.get(f"{API_BASE}/metodos_pago/{usuario_id}")
    if response.status_code == 200:
        return response.json()
    return None

def eliminar_usuario(usuario):
    response = requests.delete(f"{API_BASE}/usuarios/delete/{usuario}")
    if response.status_code == 200:
        return response.text
    return None
      
def loguear_usuario(usuario):
    response = requests.post(f"{API_BASE}/usuarios/login/{usuario}")
    if response.status_code == 204:
        return response.text
    return None

def desloguear_usuario():
    response = requests.delete(f"{API_BASE}/usuarios/logout")
    if response.status_code == 204:
        return response.text
    return None

def buscar_usuario_online():
    response = requests.get(f"{API_BASE}/usuarios/check")
    if response.status_code == 200:
        return response.json()
    return None

def actualizar_usuario_online():
    response = requests.put(f"{API_BASE}/usuarios/update_online")
    if response.status_code == 200:
        return True
    return None