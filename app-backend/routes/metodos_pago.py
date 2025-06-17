from flask import Blueprint, jsonify, request
from db import get_connection

metodos_pago_bp = Blueprint("metodos_pago", __name__)

@metodos_pago_bp.route("/<int:usuario_id>")
def get_metodos_pago(usuario_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute(
        """
            SELECT * FROM metodos_pago
            WHERE usuario_id = %s
        """, (usuario_id,)
    )
    metodos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(metodos)