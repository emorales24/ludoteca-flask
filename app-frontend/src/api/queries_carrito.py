import requests

API_BASE = "http://localhost:5000"

def obtener_carrito():
    response = requests.get(f"{API_BASE}/carrito/items")
    if response.status_code == 200:
        return response.json()
    return None


def comprar_carrito():
    response = requests.put(f"{API_BASE}/carrito/comprar_carrito")
    if response.status_code == 200:
        return response.json()
    return None


def colocar_item_carrito(id_juego,tipo_envio,precio):
    response = requests.post(f"{API_BASE}/carrito/{id_juego}/{tipo_envio}/{precio}")
    if response.status_code == 200:
        return response.json()
    return None


def sacar_item_carrito(id_item):
    response = requests.delete(f"{API_BASE}/carrito/items/{id_item}")
    if response.status_code == 200:
        return response.json()
    return None


def obtener_historial_compras():
    response = requests.get(f"{API_BASE}/carrito/items/historial")
    if response.status_code == 200:
        return response.json()
    return None