from flask import Blueprint, jsonify, request
from db import get_connection

juegos_bp = Blueprint("juegos",__name__)

# @juegos_bp.route("/")
# def get_juegos():
#     conn = get_connection()
#     cursor = conn.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM juegos")
#     juegos = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return jsonify(juegos)

@juegos_bp.route("/ofertas")
def get_juegos_oferta():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute(
        """
        SELECT
        generos.nombre_genero, juegos.id, juegos.nombre, juegos.tipo, juegos.fecha_lanzamiento, juegos.precio, juegos.porcentaje_oferta, juegos.en_oferta, juegos.puntuacion, juegos.direccion_imagen
        FROM juegos
        JOIN generos ON generos.id = juegos.id_genero
        WHERE en_oferta = TRUE
        """
    )
    ofertas = cursor.fetchall()
    conn.close()
    cursor.close()
    return jsonify(ofertas)

@juegos_bp.route("/recientes/<int:fecha>")
def get_juegos_recientes(fecha):
    """
    Obtener juegos recientes por fecha minima
    ---
    parameters:
      - name: fecha
        in: juegos/recientes/<int:fecha>
        type: string
        required: true
        description: devuelve una lista de juegos recientes
    responses:
      200:
        description: juego
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute(
        """
        SELECT
        generos.nombre_genero, juegos.id, juegos.nombre, juegos.tipo, juegos.fecha_lanzamiento, juegos.precio, juegos.porcentaje_oferta, juegos.en_oferta, juegos.puntuacion, juegos.direccion_imagen
        FROM juegos
        JOIN generos ON generos.id = juegos.id_genero
        WHERE fecha_lanzamiento like '%s%'
        """, (fecha,)
    )
    recientes = cursor.fetchall()
    conn.close()
    cursor.close()
    return jsonify(recientes)

@juegos_bp.route("/mas_valorados/<int:puntaje>")
def get_juegos_mas_valorados(puntaje):
    """
    Obtener juegos recientes por puntaje minimo
    ---
    parameters:
      - name: puntaje
        in: juegos/mas_valorados/<int:puntaje>
        type: string
        required: true
        description: devuelve una lista de juegos mejor puntuados
    responses:
      200:
        description: juego
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute(
        """
        SELECT
        generos.nombre_genero, juegos.id, juegos.nombre, juegos.tipo, juegos.fecha_lanzamiento, juegos.precio, juegos.porcentaje_oferta, juegos.en_oferta, juegos.puntuacion, juegos.direccion_imagen
        FROM juegos
        JOIN generos ON generos.id = juegos.id_genero
        WHERE puntuacion >= %s
        """, (puntaje,)
    )
    mas_valorados = cursor.fetchall()
    conn.close()
    cursor.close()
    return jsonify(mas_valorados)


@juegos_bp.route("/<int:id>")
def get_juego(id):
    """
    Obtener juego por ID
    ---
    parameters:
      - name: id
        in: juegos/{id}
        type: integer
        required: true
        description: ID del juego
    responses:
      200:
        description: juego
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """
            SELECT 
            juegos.*, generos.nombre_genero
            FROM juegos 
            JOIN generos on juegos.id_genero = generos.id 
            WHERE juegos.id = %s 
        """, (id,)
    )
    juego = cursor.fetchone()
    cursor.close()
    conn.close()
    if juego and juego['fecha_lanzamiento']:
        juego['fecha_lanzamiento'] = juego['fecha_lanzamiento'].strftime('%d %b %Y')
    return jsonify(juego)


@juegos_bp.route("/buscar", methods=["GET"])
def buscar():
    query = request.args.get('q', '').lower()
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    juegos = []

    cursor.execute(
        """
        SELECT
            generos.nombre_genero, juegos.id, juegos.nombre, juegos.tipo, juegos.fecha_lanzamiento, juegos.precio, juegos.porcentaje_oferta, juegos.en_oferta, juegos.puntuacion, juegos.direccion_imagen
        FROM juegos
        JOIN generos ON generos.id = juegos.id_genero
        WHERE LOWER(juegos.nombre) LIKE %s OR LOWER(generos.nombre_genero) LIKE %s
        """,
        (f'%{query}%', f'%{query}%')
    )
    juegos = cursor.fetchall()

    if not juegos and len(query) > 2:
        reduced_query = query[:len(query)-1]
        while not juegos and len(reduced_query) >= 2:
            cursor.execute(
                """
                SELECT
                    generos.nombre_genero, juegos.id, juegos.nombre, juegos.tipo, juegos.fecha_lanzamiento, juegos.precio, juegos.porcentaje_oferta, juegos.en_oferta, juegos.puntuacion, juegos.direccion_imagen
                FROM juegos
                JOIN generos ON generos.id = juegos.id_genero
                WHERE LOWER(juegos.nombre) LIKE %s OR LOWER(generos.nombre_genero) LIKE %s
                """,
                (f'%{reduced_query}%', f'%{reduced_query}%')
            )
            juegos = cursor.fetchall()
            reduced_query = reduced_query[:len(reduced_query)-1]

    cursor.close()
    conn.close()
    return jsonify(juegos)