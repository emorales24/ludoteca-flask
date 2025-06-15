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

@usuarios_bp.route("/update/<usr>", methods = ["POST"])
def update_usuario(usr):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    data = request.json
    usuario = data.get("usuario")
    email = data.get("email")
    contraseña = data.get("contraseña")
    nombre = data.get("nombre")
    apellido = data.get("apellido")
    calle = data.get("calle")
    direccion = data.get("numero")
    codigo_postal = data.get("codigo_postal")
    ciudad = data.get("ciudad")
    pais = data.get("pais")

    cursor.execute(
        """
            UPDATE usuarios
            SET 
                usuario = %s,
                contraseña = %s,
                email = %s,
                nombre = %s,
                apellido = %s,
                pais = %s,
                ciudad = %s,
                calle = %s,
                direccion = %s,
                codigo_postal = %s
            WHERE usuario = %s
        """, (usuario, contraseña, email, nombre, apellido, pais, ciudad, calle, direccion, codigo_postal, usr,)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return ("Valores Modificados", 200)

@usuarios_bp.route("/delete/<usr>", methods = ["DELETE"])
def eliminar_perfil(usr):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    
    cursor.execute(
        """
            DELETE
            FROM usuarios
            WHERE usuario = %s
        """, (usr,)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return ("Valores Modificados", 200)