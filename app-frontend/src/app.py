import os
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash
from flask_mail import Mail, Message
import requests

from datos_auxiliares import generos,juegos
# Importo funciones de peticiones a la API
from querys_api import obtener_usuario, validar_usuario, modificar_juego, obtener_ofertas, actualizar_usuario, eliminar_usuario,obtener_juego, loguear_usuario, desloguear_usuario, buscar_usuario_online, actualizar_usuario_online,
obtener_carrito, colocar_item_carrito, sacar_item_carrito, comprar_carrito

# Base dir es la ra�z del proyecto
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

template_dir = os.path.join(base_dir, "templates")
static_dir = os.path.join(base_dir, "static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
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
    usuario_online = buscar_usuario_online()

    if usuario_online:
        flash("Error, ya hay sesion iniciada")
        return redirect(url_for("index"))

    if request.method == "POST":
        user = request.form["usuario"]
        contra = request.form["contraseña"]
        
        usuario = validar_usuario(user)
        if usuario == None:
            flash("Usuario no encontrado")
            return redirect(url_for("login"))
        elif usuario["contraseña"] == contra:  
            loguear_usuario(user)
            if usuario["rol"] == "admin":
                return redirect(url_for("inicioAdmin"))
            else:
                return redirect(url_for("index"))
        else:
            flash("Contaseña Invalida.")
            return redirect(url_for("login"))
    
    return render_template("login.html")

#PAGINA DE PERFIL
@app.route("/verificar_login")
def redirigir_perfil():
    usuario_online = buscar_usuario_online()

    if not usuario_online:
        flash("Necesitás iniciar sesión para acceder a tu perfil.", "error")
        return redirect(url_for("index"))
    
    return redirect(url_for("perfil", usr=usuario_online["usuario"]))


@app.route("/perfil/<usr>", methods = ["GET", "POST"])
def perfil(usr):
        
    datos_usr = obtener_usuario(usr)

    if datos_usr == None:
        flash("Usuario no Encontrado. Si no tenes cuenta, completa el registro para comenzar a comprar juegos!")
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
            
            actualizar_usuario_online()

            datos_usr = obtener_usuario(username)
            
            return redirect(url_for("perfil", usr = datos_usr["usuario"]))

    return render_template("perfil.html", usuario = datos_usr)
    

@app.route("/desloguear", methods=['POST'])
def desloguear():
    
    response = desloguear_usuario() # falta manejar posibles errores aca nada mas
    return redirect(url_for("index"))

#PAGINA DE ADMIN
@app.route("/admin", methods=["POST", "GET"])
def inicioAdmin():

    usuario_online = buscar_usuario_online()

    if usuario_online:
        if usuario_online["rol"] == "admin":
            ofertas = obtener_ofertas()

            if request.method == "POST":
                id_juego = request.form["id_juego"]
                precio = request.form["precio"]
                porcentaje_oferta = request.form["porcentaje_oferta"]
                en_oferta = request.form["en_oferta"]

                modificar_juego(id_juego, precio, porcentaje_oferta, en_oferta)
                return redirect(url_for("inicioAdmin", juegos = ofertas))

            return render_template("admin.html", juegos = ofertas)
        else:
            flash("Necesitas iniciar sesion con una cuenta valida de administrador para esa seccion")
            return redirect(url_for("index"))
    
    else:
        flash("Error, necesitas iniciar sesion.")
        return redirect(url_for("index"))

#INICIO DE PAG USUARIO FINAL
@app.route("/")
def index():


    # juegosRecientes = requests.get(f"{API_BASE}/juegos/recientes")
    # juegosRebajados = requests.get(f"{API_BASE}/juegos/ofertas")
    # juegosRecomendados = requests.get(f"{API_BASE}/juegos/mas_valorados/{50}") 
    #esto lo podriamos hacer un boton o similar como una constante igual a como manejamos los usuarios y setearlo para aprovecharlo -> es facil y rapido
    # if not juegosRecientes and not juegosRebajados and not juegosRecomendados:
    #     flash("No se pudo obtener la lista de juegos. El servidor esta caido", "Error interno")    
    #     redirect(url_for("index"))
    return render_template("inicio.html", juegosRecientes=[],juegosEnOferta=[],juegosRecomendados=[])

#PAGINA DE LISTA DE JUEGOS
@app.route("/juegos")
def buscador():
    juegos = requests.get(f"{API_BASE}/juegos") 
    return render_template("buscador.html", juegos=juegos) 

#PAGINA DE DETALLE DE JUEGO
@app.route("/juego/<int:id>")
def ver_juego(id):

    usuario_online = buscar_usuario_online()
    if usuario_online:
        juego = obtener_juego(id)
        if not juego:
            flash("No se puede obtener el juego. El servidor debe estar caido.", "Error interno")
            return redirect(url_for("index"))
        return render_template("juego.html", juego=juego)
    
    flash("Necesitás iniciar sesión para ver juegos!")
    return redirect(url_for("login"))

#PAGINA DE CARRITO
@app.route("/carrito")
def carrito():

    usuario = buscar_usuario_online()

    if usuario:
        itemsCarrito = obtener_carrito()
        total = sum(item['precio'] for item in itemsCarrito)
        return render_template("carrito.html", carrito=itemsCarrito, total=total)
    
    flash("Para ver tu carrito necesitas iniciar sesión.")
    return redirect(url_for('index'))

# es mejor que el boton solo agregue y no modifique la pagina (en nuestro
# caso deberia estar el boton de comprar solo en la pantalla donde se ve un juego unico)
@app.route("/carrito/agregar", methods=['POST'])
def post_itemCarrito(): 
    # usuario = buscar_usuario_online()

    # if usuario:
    id = int(request.form['id_juego'])
    tipo_envio = 'digital' if 'opcion_digital' in request.form else 'fisico'
    precio = float(request.form['precio'])

    response = colocar_item_carrito(id, tipo_envio, precio)
    flash("Juego agregado a tu carrito!")
    return redirect(url_for('ver_juego', id=id))
    
    # flash("Para ver tu carrito necesitas iniciar sesión.")
    # return redirect(url_for('index'))

@app.route("/carrito/eliminar/<int:id>")
def eliminar_itemCarrito(id):
    # usuario = buscar_usuario_online()
    # if usuario:
    response = sacar_item_carrito(id)
    return redirect(url_for('carrito'))

    # flash("Para ver tu carrito necesitas iniciar sesión.")
    # return redirect(url_for('index'))  

@app.route("/carrito/comprar")
def comprar_itemsCarrito():

    comprar_carrito()
    flash("Carrito comprado!")
    return redirect(url_for('carrito'))


if __name__ == '__main__':
    app.run(debug = True, port = 5001)