from flask import Blueprint, jsonify, request
from db import get_connection

juegos_bp = Blueprint("usuarios",__name__)

@juegos_bp.route("/")
def get_juegos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM juegos")
    juegos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(juegos)

