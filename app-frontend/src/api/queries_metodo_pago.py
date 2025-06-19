import os
import requests
from dotenv import load_dotenv
load_dotenv

API_BASE = os.getenv("API_BASE")

def obtener_metodos_pago(usuario_id):
    response = requests.get(f"{API_BASE}/metodos_pago/{usuario_id}")
    if response.status_code == 200:
        return response.json()
    return None

def agregar_metodo_pago(usuario_id, tipo, marca, numero_tarjeta, vencimineto, codigo_cvv):
    response = requests.post(
        f"{API_BASE}/metodos_pago/add/{usuario_id}",
        json = {
            "tipo": tipo,
            "marca": marca,
            "numero_tarjeta": numero_tarjeta,
            "fecha_vencimiento": vencimineto,
            "numero_cvv": codigo_cvv,
        }    
    )

    return response.status_code

def eliminar_metodo_pago(usuario_id, codigo_cvv):
    response = requests.delete(
        f"{API_BASE}/metodos_pago/delete/{usuario_id}",
        json = {
            "codigo_cvv": codigo_cvv
        },
    )
    if response.status_code == 201:
        return True