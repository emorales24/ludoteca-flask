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
def get_usuario(usr):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s", (usr,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(usuario)

@usuarios_bp.route("/validar/<usr>")
def get_rol_usuario_clave(usr):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT rol, usuario, contraseña FROM usuarios WHERE usuario = %s", (usr,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(usuario)


@usuarios_bp.route("login/<usr>")
def post_usuario_online(usr):

    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("""
        INSERT INTO usuario_online (id, usuario_id, rol, nombre, apellido)
        SELECT 1, id, rol, nombre, apellido
        FROM usuarios
        WHERE usuario = %s
    """, (usr,))  # Podriamos usar Replace que hace que si no encuentra uno, lo agrega, y si existe uno,
                  # lo reescribe. Pero ahi perdemos el error. Borrar este comentario al entregar el TP
    conn.commit()

    
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(usuario)


# este es borrable pero lo dejo para no modificar el del perfil
# este  nos sirve para 
# OBJETIVO: TRAEMOS EL USUARIO ONLINE 
# CONSECUENCIA EN EL FRONT 1: Si existe, lo mostramos trayendolo con get_usuario
# CONSECUENTA EN EL FRONT 2: Si no hay dato, lo redirigimos al login
# (este comentario es mejor moverlo al app.py de front)
@usuarios_bp.route("check/<usr>")  
def get_usuario_online(usr):     
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT usuario FROM usuario_online WHERE id = 1")
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(usuario)

@usuarios_bp.route("logout/<usr>")
def delete_usuario_online():
