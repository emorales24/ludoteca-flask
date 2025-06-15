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

@usuarios_bp.route("login/<usr>",  methods = ["POST"])
def post_usuario_online(usr):

    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("""
        INSERT INTO usuario_online (id, usuario_id, rol, usuario, email)
        SELECT 1, id, rol, usuario, email
        FROM usuarios
        WHERE usuario = %s
    """, (usr,)) 
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify("Se inició sesión correctamente", 204)


# este es borrable pero lo dejo para no modificar el del perfil
# este  nos sirve para 
# OBJETIVO: TRAEMOS EL USUARIO ONLINE 
# CONSECUENCIA EN EL FRONT 1: Si existe, lo mostramos trayendolo con get_usuario
# CONSECUENTA EN EL FRONT 2: Si no hay dato, lo redirigimos al login
# (este comentario es mejor moverlo al app.py de front)
@usuarios_bp.route("check")  
def get_usuario_online():     
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT usuario FROM usuario_online WHERE id = 1")
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    if usuario:
        return jsonify(usuario,200)
    return jsonify(usuario) 

@usuarios_bp.route("logout",  methods = ["DELETE"])
def delete_usuario_online():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("DELETE FROM usuario_online WHERE id = 1")
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify("Cerraste sesion correctamente",204)