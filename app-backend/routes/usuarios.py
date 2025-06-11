from flask import Blueprint, jsonify, request
from db import get_connection

usuarios_bp = Blueprint("usuarios",__name__)

@usuarios_bp.route("/")
def get_usuarios():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(usuarios)

@usuarios_bp.route("/<usr>")
def login(usr):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usr,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    if not usuario:
        return ("Usuario no encontrado", 404)
    return jsonify(usuario)


@usuarios_bp.route("/<usr>")
def get_usuario(usr):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usr,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    if not usuario:
        return ("Usuario no encontrado", 404)
    return jsonify(usuario)