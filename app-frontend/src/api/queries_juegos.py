import requests

API_BASE = "http://localhost:5000"

def obtener_juego(id):
    try:
        response = requests.get(f"{API_BASE}/juegos/{id}", timeout=4)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR EN OBTENER_JUEGO] {e}")
        return None
    return None

def obtener_juegos_rebajados():
    try:
        response = requests.get(f"{API_BASE}/juegos/ofertas")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] No se pudo conectar al backend: {e}")
    return None

def obtener_juegos_recientes():
    try:
        response = requests.get(f"{API_BASE}/juegos/recientes/{2024}")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] No se pudo conectar al backend: {e}")
    return None

def obtener_juegos_recomendados():
    try:
        response = requests.get(f"{API_BASE}/juegos/mas_valorados/{90}")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] No se pudo conectar al backend: {e}")
    return None

def modificar_juego(id_juego, precio, porcentaje_oferta, en_oferta):
    response = requests.put(
        f"{API_BASE}/admin/modificar_juego/{id_juego}",
        json={
            "precio": precio,
            "porcentaje_oferta": porcentaje_oferta,
            "en_oferta": en_oferta,
        },
    )
    if response.status_code == 200:
        return True
    return None

def buscar_juegos(query):
    response = requests.get(f"{API_BASE}/juegos/buscar?q={query}")
    if response.status_code == 200:
        return response.json()
    return None