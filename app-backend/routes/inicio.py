from flask import Blueprint, jsonify, request
from db import get_connection

inicio_bp = Blueprint("inicio", __name__)

@inicio_bp.route("/")
def juegos_incio():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute(
        """
            SELECT 
            juegos.direccion_imagen, juegos.fecha_lanzamiento, generos.id, generos.nombre, juegos.nombre, juegos.precio, juegos.puntuacion, juegos.tipo
            FROM juegos
            JOIN generos ON generos.id = juegos.id_genero
            WHERE juegos.en_oferta = TRUE
        """
    )
    juegos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(juegos)