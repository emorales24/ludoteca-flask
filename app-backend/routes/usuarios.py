from flask import Blueprint, jsonify, request
from db import get_connection

usuarios_bp = Blueprint("usuarios",__name__)

@usuarios_bp.route("/")
def get_usuarios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(usuarios)



# Busca un usuario por su nombre de usuario en la tabla 'usuarios'.
# Retorna un diccionario con los datos del usuario (usuario, contraseña, rol)
# o None si no se encuentra.
@usuarios_bp.route("/login")
def login_usuario():
    conn = get_connection()
    if not conn:
        return None

    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT TOP 1 usuario, contraseña, rol FROM usuarios WHERE usuario = %s")
    usuario = cursor.fetchall()
    conn.close()
    cursor.close()
    return jsonify(usuario)