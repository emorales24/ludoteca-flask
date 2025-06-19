from flask import Blueprint, jsonify, request
from db import get_connection

metodos_pago_bp = Blueprint("metodos_pago", __name__)

@metodos_pago_bp.route("/<int:usuario_id>")
def get_metodos_pago(usuario_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute(
        """
            SELECT 
            id,
            usuario_id,
            tipo,
            marca,
            numero_tarjeta,
            DATE_FORMAT(metodos_pago.fecha_vencimiento, '%d %b %Y') AS fecha_vencimiento,
            codigo_cvv 
            FROM metodos_pago
            WHERE usuario_id = %s
        """, (usuario_id,)
    )
    metodos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(metodos)

@metodos_pago_bp.route("/add/<int:usuario_id>", methods = ["POST"])
def add_metodo_pago(usuario_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)

    data = request.json

    tipo = data.get("tipo")
    marca = data.get("marca")
    numero_tarjeta = data.get("numero_tarjeta")
    fecha_vencimiento = data.get("fecha_vencimiento")
    numero_cvv = data.get("numero_cvv")

    cursor.execute(
        """
        INSERT INTO metodos_pago
        (usuario_id, tipo, marca, numero_tarjeta, fecha_vencimiento, codigo_cvv)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (usuario_id, tipo, marca, numero_tarjeta, fecha_vencimiento, numero_cvv,)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify("Tarjeta Agregada Correctamente"), 201