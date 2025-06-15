import requests

# API Backend
API_BASE = "http://localhost:5000"

def obtener_usuario(usr):
    response = requests.get(f"{API_BASE}/usuarios/{usr}")
    if response.status_code == 200:
        return response.json()
    return None

def validar_usuario(usr):
    response = requests.get(f"{API_BASE}/usuarios/validar/{usr}")
    if response.status_code == 200:
        return response.json()
    return None

def modificar_juego(id_juego, precio, porcentaje_oferta, en_oferta):
    response = requests.post(
        f"{API_BASE}/admin/modificar_juego/{id_juego}",
        json={"precio": precio, "porcentaje_oferta": porcentaje_oferta, "en_oferta": en_oferta},
    )
    if response.status_code == 200:
        return True
    return None

def obtener_ofertas():
    response = requests.get(f"{API_BASE}/juegos/ofertas")
    if response.status_code == 200:
        return response.json()
    return None

def actualizar_usuario(usuario, email, contra, nombre, apellido, calle, direccion, codigo_postal, ciudad, pais, usuario_viejo):
    response = requests.post(
        f"{API_BASE}/usuarios/update/{usuario_viejo}",
        json = {
            "usuario": usuario,
            "email": email,
            "contraseña": contra,
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