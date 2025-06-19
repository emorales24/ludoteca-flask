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
    cursor.execute(
        """
            SELECT * FROM usuarios 
            INNER JOIN usuario_online
            ON usuario_online.usuario = usuarios.usuario
            WHERE usuarios.usuario = %s
        """, (usr,)
    )
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(usuario)

@usuarios_bp.route("/validar/<usr>", methods = ["POST"])
def validate_usuario(usr):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    data = request.json
    contra_evaluar = data.get("contra_evaluar")
    cursor.execute(
        """
            SELECT rol, usuario, contra FROM usuarios WHERE usuario = %s
        """, (usr,)
    )
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()

    if not usuario:
        return jsonify("Usuario no encontrado."), 404
    elif usuario["contra"] == contra_evaluar:
        return jsonify(usuario), 200
    else:
        return jsonify("Error, contraseña incorrecta"), 401

@usuarios_bp.route("/update/<usr>", methods = ["PUT"])
def update_usuario(usr):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    data = request.json
    usuario = data.get("usuario")
    email = data.get("email")
    contra = data.get("contra")
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
                contra = %s,
                email = %s,
                nombre = %s,
                apellido = %s,
                pais = %s,
                ciudad = %s,
                calle = %s,
                direccion = %s,
                codigo_postal = %s
            WHERE usuario = %s
        """, (usuario, contra, email, nombre, apellido, pais, ciudad, calle, direccion, codigo_postal, usr,)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return ("Valores Modificados", 200)

@usuarios_bp.route("/delete/<usr>", methods = ["DELETE"])
def delete_usuario(usr):
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

@usuarios_bp.route("check")  
def get_usuario_online():     
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("SELECT id, usuario_id, usuario, rol FROM usuario_online WHERE id = 1")
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    if usuario:
        return jsonify(usuario), 200
    return jsonify(usuario) , 404

@usuarios_bp.route("logout",  methods = ["DELETE"])
def delete_usuario_online():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("DELETE FROM usuario_online WHERE id = 1")
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify("Cerraste sesion correctamente",204)

@usuarios_bp.route("update_online", methods = ["PUT"])
def update_usuario_online():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute(
        """
            UPDATE usuario_online
            JOIN usuarios ON usuario_online.usuario_id = usuarios.id
            SET 
            usuario_online.usuario_id = usuarios.id,
                usuario_online.usuario = usuarios.usuario,
                usuario_online.email = usuarios.email,
                usuario_online.rol = usuarios.rol
        """
    )
    conn.commit()
    cursor.close()
    conn.close()
    return ("Valores Modificados", 200)