import os
from flask import Flask, render_template, jsonify, request, redirect
from flask_mail import Mail, Message
import requests

# Base dir es la raíz del proyecto
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

template_dir = os.path.join(base_dir, "templates")
static_dir = os.path.join(base_dir, "static")  # Corregido

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'mail'
app.config['MAIL_PASSWORD'] = 'clave-temporal'  # Contraseña de aplicación
app.config['MAIL_DEFAULT_SENDER'] = 'mail'
mail = Mail(app)

# API Backend
API_BASE = "http://localhost:5000"


generos = {
    1: "rpg",
    2: "aventura",
    3: "deportes",
    4: "visual novel",
    5: "terror",
    6: "cozy"
}

juegos = {
    1: {
        "id": 1,
        "nombre": "The Witcher 3",
        "tipo": "BASE",
        "id_genero": 1,
        "fecha_lanzamiento": "2015-05-19",
        "precio": 59.99,
        "porcentaje_oferta": 50,
        "en_oferta": True,
        "puntuacion": 92,
        "direccion_imagen": "images/witcher3.jpg"
    },
    2: {
        "id": 2,
        "nombre": "Hogwarts Legacy",
        "tipo": "BASE",
        "id_genero": 2,
        "fecha_lanzamiento": "2023-02-10",
        "precio": 74.99,
        "porcentaje_oferta": 13,
        "en_oferta": True,
        "puntuacion": 85,
        "direccion_imagen": "images/hogwarts.jpg"
    },
    3: {
        "id": 3,
        "nombre": "Cyberpunk 2077",
        "tipo": "BASE",
        "id_genero": 1,
        "fecha_lanzamiento": "2020-12-10",
        "precio": 49.99,
        "porcentaje_oferta": 20,
        "en_oferta": True,
        "puntuacion": 78,
        "direccion_imagen": "images/cyberpunk.jpg"
    },
    4: {
        "id": 4,
        "nombre": "Monster Hunter World: Iceborne",
        "tipo": "DLC",
        "id_genero": 1,
        "fecha_lanzamiento": "2019-09-06",
        "precio": 19.99,
        "porcentaje_oferta": None,
        "en_oferta": False,
        "puntuacion": 88,
        "direccion_imagen": "images/mhiceborn.jpg"
    },
    5: {
        "id": 5,
        "nombre": "Resident Evil Village",
        "tipo": "BASE",
        "id_genero": 5,
        "fecha_lanzamiento": "2021-05-07",
        "precio": 59.99,
        "porcentaje_oferta": 25,
        "en_oferta": True,
        "puntuacion": 84,
        "direccion_imagen": "images/revillage.jpg"
    },
    6: {
        "id": 6,
        "nombre": "Stardew Valley",
        "tipo": "BASE",
        "id_genero": 6,
        "fecha_lanzamiento": "2016-02-26",
        "precio": 14.99,
        "porcentaje_oferta": None,
        "en_oferta": False,
        "puntuacion": 89,
        "direccion_imagen": "images/stardew.jpg"
    },
    7: {
        "id": 7,
        "nombre": "Doki Doki Literature Club",
        "tipo": "BASE",
        "id_genero": 4,
        "fecha_lanzamiento": "2017-09-22",
        "precio": 0.00,
        "porcentaje_oferta": None,
        "en_oferta": False,
        "puntuacion": 91,
        "direccion_imagen": "images/dokidoki.jpg"
    },
    8: {
        "id": 8,
        "nombre": "Little Nightmares",
        "tipo": "BASE",
        "id_genero": 5,
        "fecha_lanzamiento": "2017-04-28",
        "precio": 24.99,
        "porcentaje_oferta": 60,
        "en_oferta": True,
        "puntuacion": 83,
        "direccion_imagen": "images/littlenightmares.jpg"
    },
    9: {
        "id": 9,
        "nombre": "Animal Crossing: New Horizons",
        "tipo": "BASE",
        "id_genero": 6,
        "fecha_lanzamiento": "2020-03-20",
        "precio": 59.99,
        "porcentaje_oferta": 17,
        "en_oferta": True,
        "puntuacion": 90,
        "direccion_imagen": "images/animalcrossing.jpg"
    }
}


# LOGIN PRIMERO
@app.route("/")
def login():
    return render_template("login.html")

#PAGINA DE ADMIN
@app.route("/admin")
def inicioAdmin():
    return render_template("inicio.html")

#INICIO DE PAG USUARIO FINAL
@app.route("/inicio")
def index():
    return render_template("inicio.html")

#PAGINA DE LISTA DE JUEGOS
@app.route("/juegos")
def buscador():
    return render_template("buscador.html")

#PAGINA DE DETALLE DE JUEGO
@app.route("/juego/<int:id>")
def ver_juego(id):

    juego = juegos.get(id)
    if juego:
        juego["nombre_genero"] = generos.get(juego["id_genero"], "desconocido")
        return render_template("juego.html", juego= juego)
    return render_template("inicio.html")

#PAGINA DE PERFIL
@app.route("/perfil")
def perfil():
    return render_template("perfil.html")

#PAGINA DE CARRITO
@app.route("/carrito")
def carrito():
    return render_template("carrito.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)