import os
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_mail import Mail, Message
import requests

from datos_auxiliares import generos,juegos
# Importo funciones de peticiones a la API
from querys_api import obtener_usuario, validar_usuario, modificar_juego, obtener_ofertas, actualizar_usuario, eliminar_usuario,obtener_juego

# Base dir es la ra�z del proyecto
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

template_dir = os.path.join(base_dir, "templates")
static_dir = os.path.join(base_dir, "static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# (descomentar esto para poder usar lo de los flash pasar a archivo env quizas)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'mail'
app.config['MAIL_PASSWORD'] = 'clave-temporal'  # Contrase�a de aplicaci�n
app.config['MAIL_DEFAULT_SENDER'] = 'mail'
mail = Mail(app)

# API Backend (ver de quitar)
API_BASE = "http://localhost:5000"

# LOGIN PRIMERO
@app.route("/login", methods=["GET", "POST"])
def login():
    issue = None

    if request.method == "POST":
        user = request.form["usuario"]
        contra = request.form["contraseña"]
        
        usuario = validar_usuario(user)
        if usuario == None:                         # Si la query return None, se modifica la variable issue
            issue = "Usuario no encontrado"
        elif usuario["contraseña"] == contra:       # Evalua si son iguales los campos
            if usuario["rol"] == "admin":
                return redirect(url_for("inicioAdmin"))
            else:
                return redirect(url_for("perfil", usr = usuario["usuario"]))
        else:
            issue = "Contaseña Invalida."
    
    return render_template("login.html", error = issue)

#PAGINA DE PERFIL (agregar validacion de usuario online)
@app.route("/perfil/<usr>", methods = ["GET", "POST"])
def perfil(usr):
    datos_usr = obtener_usuario(usr)

    if datos_usr == None:
        flash("Usuario no Encontrado")
        return redirect(url_for("index")) # CAMBIAR POR REGISTRARSE
    
    if request.method == "POST":
        if request.form.get("eliminar"):
            eliminar_usuario(datos_usr["usuario"])
            flash("Perfil eliminado correctamente")
            return redirect(url_for("index"))
        else:
            username = request.form["username"]
            email = request.form["email"]
            contraseña = request.form["contraseña"]
            nombre = request.form["nombre"]
            apellido = request.form["apellido"]
            calle = request.form["calle"]
            direccion = request.form["direccion"]
            codigo_postal = request.form["cp"]
            ciudad = request.form["ciudad"]
            pais = request.form["pais"]

            actualizar_usuario(username, email, contraseña, nombre, apellido, calle, direccion, codigo_postal, ciudad, pais, datos_usr["usuario"])
            datos_usr = obtener_usuario(username)
            
            return redirect(url_for("perfil", usr = datos_usr["usuario"]))

    return render_template("perfil.html", usuario = datos_usr)

#PAGINA DE ADMIN
@app.route("/admin", methods=["POST", "GET"])
def inicioAdmin():
    ofertas = obtener_ofertas()

    if request.method == "POST":
        id_juego = request.form["id_juego"]
        precio = request.form["precio"]
        porcentaje_oferta = request.form["porcentaje_oferta"]
        en_oferta = request.form["en_oferta"]

        modificar_juego(id_juego, precio, porcentaje_oferta, en_oferta)
        return redirect(url_for("inicioAdmin", juegos = ofertas))

    return render_template("admin.html", juegos = ofertas)

#INICIO DE PAG USUARIO FINAL
@app.route("/")
def index():

    juegosRecientes = requests.get(f"{API_BASE}/juegos/recientes")
    juegosRebajados = requests.get(f"{API_BASE}/juegos/ofertas")
    juegosRecomendados = requests.get(f"{API_BASE}/juegos/mas_valorados/{50}") 
    #esto lo podriamos hacer un boton o similar como una constante igual a como manejamos los usuarios y setearlo para aprovecharlo -> es facil y rapido

    return render_template("inicio.html", juegosRecientes=juegosRecientes,juegosRebajados=juegosRebajados,juegosRecomendados=juegosRecomendados)

#PAGINA DE LISTA DE JUEGOS
@app.route("/juegos")
def buscador():
    # horribles los nombres aca pero se entiende que es 
    # variable = datos_auxiliares.juegos, cambiarlo despues

    juegos = requests.get(f"{API_BASE}/juegos") 
    return render_template("buscador.html", juegos=juegos) 

#PAGINA DE DETALLE DE JUEGO
@app.route("/juego/<int:id>")
def ver_juego(id):

    juego = obtener_juego(id)
    if juego:
        return render_template("juego.html", juego=juego)
    
    return render_template("inicio.html")

#PAGINA DE CARRITO
@app.route("/carrito")
def carrito():

    #el carrito lo puedo obtener
    itemsCarrito = requests.get(f"{API_BASE}/itemsCarrito/{usuario_online['usuario']}")
    return render_template("carrito.html", itemsCarrito=itemsCarrito)


# es mejor que el boton solo agregue y no modifique la pagina (en nuestro
# caso deberia estar el boton de comprar solo en la pantalla donde se ve un juego unico)
@app.route("/carrito/agregar/<int:id>")
def post_itemCarrito(id): 

    #obtengo el id del user o hago un create basandome solo en el nombre de usuario que
    #ya tengo en el dato global usuario_online
        #<codigo>
    #guarda el item en bd creando un dato itemCarrito enlazando el id del juego y el del user actual
        #<codigo>
    
    return redirect(url_for('ver_juego', id=id))


## falta el borrar item carrito pero es un delete nada mas y podriamos no agregarlo (dejar para el final)

@app.route("/carrito/comprar")
def comprar_carrito():
    # a partir del nombre del user genero un script de UPDATE para pasar
    # todos los items de carrito que esten en estado de proceso de compra a "comprados" (no me acuerdo como era el nombre de estado)

    # reinicio el como veo la pantalla (aca podriamos agregar un mini mensaje por magia de javascript al apretar
    # comprar que le diga al usuario que ya compró para que no se vea tan brusco)
    return render_template("carrito.html", itemsCarrito=None)


if __name__ == '__main__':
    app.run(debug = True, port = 5001)