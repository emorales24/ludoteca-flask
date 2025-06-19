from flask import Blueprint, jsonify, request
from db import get_connection

items_carrito_bp = Blueprint("carrito",__name__)

@items_carrito_bp.route("/<int:id>/<tipo_envio>/<float:precio>",  methods = ["POST"])
def post_item_carrito(id, tipo_envio,precio):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("""
        INSERT INTO items_carrito (estado, usuario_id, juego_id, precio, tipo_envio)
        SELECT 'pendiente', usuario_id, %s, %s, %s
        FROM usuario_online
        WHERE id = 1;
    """, (id,precio,tipo_envio)) 
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify("Se agrego correctamente"), 201


@items_carrito_bp.route("/items/<int:id>",  methods = ["DELETE"])
def delete_item_carrito(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("""
        DELETE FROM items_carrito
        WHERE id = %s and estado='pendiente';
    """, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify("Se elimino correctamente"), 204

@items_carrito_bp.route("/comprar_carrito",  methods = ["PUT"])
def put_item_carrito():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("""
        UPDATE items_carrito 
        SET estado = 'comprado'
        WHERE estado = 'pendiente'
        AND usuario_id = (SELECT usuario_id FROM usuario_online WHERE id = 1);
    """)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify("Se compró correctamente"), 204

@items_carrito_bp.route("/items")
def get_items_carrito():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("""
        SELECT items_carrito.*,juegos.nombre, juegos.direccion_imagen, generos.nombre_genero as genero
        from items_carrito
        inner join juegos
        on juegos.id = items_carrito.juego_id
        inner join generos
        on generos.id = juegos.id_genero
        WHERE items_carrito.estado = 'pendiente'
        AND items_carrito.usuario_id = (SELECT usuario_id FROM usuario_online WHERE id = 1);
    """)
    carrito = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(carrito), 200

@items_carrito_bp.route("/items/historial")
def get_historial_items_carrito():
    conn = get_connection()
    cursor = conn.cursor(dictionary = True)
    cursor.execute("""
        SELECT items_carrito.*,juegos.nombre, juegos.direccion_imagen, generos.nombre_genero as genero
        from items_carrito
        inner join juegos
        on juegos.id = items_carrito.juego_id
        inner join generos
        on generos.id = juegos.id_genero
        WHERE items_carrito.estado = 'comprado'
        AND items_carrito.usuario_id = (SELECT usuario_id FROM usuario_online WHERE id = 1);
    """)
    carrito = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(carrito), 200

