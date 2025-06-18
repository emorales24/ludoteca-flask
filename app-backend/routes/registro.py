from flask import Blueprint, request, jsonify
from db import get_connection

registro_bp = Blueprint("registro", __name__)


@registro_bp.route("/", methods=["GET", "POST"])
def registro():
    conn = get_connection()
    cursor = conn.cursor()
    data = request.json
    usuario = data.get("usuario")
    nombre = data.get("nombre")
    apellido = data.get("apellido")
    email = data.get("email")
    pais = data.get("pais")
    ciudad = data.get("ciudad")
    contra = data.get("contra")

    cursor.execute(
        "SELECT id FROM usuarios WHERE usuario = %s OR email = %s", (usuario, email)
    )
    existente = cursor.fetchone()

    if existente:
        cursor.close()
        conn.close()
        return jsonify("El usuario ya existe"), 409

    query = """
        INSERT INTO usuarios
        (rol, usuario, contra, email, nombre, apellido, pais, ciudad)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    valores = ("final", usuario, contra, email, nombre, apellido, pais, ciudad)

    cursor.execute(query, valores)
    conn.commit()

    cursor.close()
    conn.close()
    return jsonify("Usuario creado exitosamente"), 201
