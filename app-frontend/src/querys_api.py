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

def actualizar_usuario(username, )