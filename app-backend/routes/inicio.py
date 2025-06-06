from flask import Blueprint, jsonify, request
from db import get_connection

inicio_bp = Blueprint("inicio", __name__)

@inicio_bp.route("/")
def juegos_incio():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute(
        """
            SELECT generos.id, generos.nombre_genero, juegos.direccion_imagen, juegos.nombre, juegos.precio, juegos.fecha_lanzamiento, juegos.puntuacion, juegos.tipo, juegos.porcentaje_oferta
            FROM juegos
            LEFT JOIN generos ON generos.id = juegos.id_genero
            WHERE juegos.en_oferta = TRUE OR fecha_lanzamiento like '202%'
        """
    )
    juegos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(juegos)