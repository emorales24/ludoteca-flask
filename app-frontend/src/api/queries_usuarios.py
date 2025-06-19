import requests

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
    else:
        return response.status_code

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

def eliminar_usuario(usuario):
    response = requests.delete(f"{API_BASE}/usuarios/delete/{usuario}")
    if response.status_code == 200:
        return response.text
    return None

def registrar_usuario(usuario, nombre, apellido, email, contra, pais, ciudad):
    response = requests.post(
        f"{API_BASE}/registro",
        json = {
            "usuario": usuario,
            "contra": contra, 
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "pais": pais,
            "ciudad": ciudad    
        }
    )

    return response.status_code