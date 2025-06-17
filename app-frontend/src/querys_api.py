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


def obtener_ofertas():
    try:
        response = requests.get(f"{API_BASE}/juegos/ofertas")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] No se pudo conectar al backend: {e}")
    return None


def obtener_juegos_rescientes():
    try:
        response = requests.get(f"{API_BASE}/juegos/recientes/{2024}")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] No se pudo conectar al backend: {e}")
    return None


def obtener_recomendados():
    try:
        response = requests.get(f"{API_BASE}/juegos/mas_valorados/{90}")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] No se pudo conectar al backend: {e}")
    return None


def obtener_rebajados():
    try:
        response = requests.get(f"{API_BASE}/juegos/ofertas")
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] No se pudo conectar al backend: {e}")
    return None


def obtener_juego(id):
    try:
        response = requests.get(f"{API_BASE}/juegos/{id}", timeout=4)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"[ERROR EN OBTENER_JUEGO] {e}")
        return None
    return None

      
def actualizar_usuario(usuario, email, contra, nombre, apellido, calle, direccion, codigo_postal, ciudad, pais, usuario_viejo):
    response = requests.put(
        f"{API_BASE}/usuarios/update/{usuario_viejo}",
        json={
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

def buscar_juegos(query):
    response = requests.get(f"{API_BASE}/juegos/buscar?q={query}")
    if response.status_code == 200:
        return response.json()
    return None

def obtener_historial_compras():
    response = requests.get(f"{API_BASE}/carrito/items/historial")
    if response.status_code == 200:
        return response.json()
    return None

def obtener_metodos_pago(usuario_id):
    response = requests.get(f"{API_BASE}/metodos_pago/{usuario_id}")
    if response.status_code == 200:
        return response.json()
    return None