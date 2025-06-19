import os
import requests
from dotenv import load_dotenv
load_dotenv()

API_BASE = os.getenv("API_BASE")

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