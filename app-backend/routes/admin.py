from flask import Blueprint, jsonify, request
from db import get_connection

admin_bp = Blueprint("admin",__name__)

@admin_bp.route("/modificar_juego/<int:id_juego>", methods = ["POST"])
def modificar_juego(id_juego):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    data = request.json
    precio = data.get("precio")
    porcentaje_oferta = data.get("porcentaje_oferta")
    en_oferta = data.get("en_oferta")
    cursor.execute(
        """
            UPDATE juegos
            SET precio = %s,
                porcentaje_oferta = %s,
                en_oferta = %s
            WHERE id = %s
        """, (precio, porcentaje_oferta, en_oferta, id_juego,)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return ("Valores Modificados", 200)