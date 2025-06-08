from flask import Blueprint, jsonify, request
from db import get_connection

juegos_bp = Blueprint("juegos",__name__)

@juegos_bp.route("/juegos")
def get_juegos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM juegos")
    juegos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(juegos)

@juegos_bp.route("/juegos/ofertas")
def get_juegos_oferta():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute(
        """
        SELECT
        generos.nombre_genero, juegos.nombre, juegos.tipo, juegos.fecha_lanzamiento, juegos.precio, juegos.porcentaje_oferta, juegos.puntuacion, juegos.direccion_imagen
        FROM juegos
        LEFT JOIN generos ON generos.id = juegos.id_genero
        WHERE en_oferta = TRUE
        """
    )
    ofertas = cursor.fetchall()
    conn.close()
    cursor.close()
    return jsonify(ofertas)

@juegos_bp.route("/juegos/recientes/<int:fecha>")
def get_juegos_recientes(fecha):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute(
        """
        SELECT
        generos.nombre_genero, juegos.nombre, juegos.tipo, juegos.fecha_lanzamiento, juegos.precio, juegos.porcentaje_oferta, juegos.puntuacion, juegos.direccion_imagen
        FROM juegos
        LEFT JOIN generos ON generos.id = juegos.id_genero
        WHERE fecha_lanzamiento like '%s%'
        """, (fecha,)
    )
    recientes = cursor.fetchall()
    conn.close()
    cursor.close()
    return jsonify(recientes)

@juegos_bp.route("/juegos/mas_valorados/<int:puntaje>")
def get_juegos_mas_valorados(puntaje):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute(
        """
        SELECT
        generos.nombre_genero, juegos.nombre, juegos.tipo, juegos.fecha_lanzamiento, juegos.precio, juegos.porcentaje_oferta, juegos.puntuacion, juegos.direccion_imagen
        FROM juegos
        LEFT JOIN generos ON generos.id = juegos.id_genero
        WHERE puntuacion >= %s
        """, (puntaje,)
    )
    mas_valorados = cursor.fetchall()
    conn.close()
    cursor.close()
    return jsonify(mas_valorados)