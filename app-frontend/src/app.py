import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

# Importa funciones de peticiones a la API
from api.queries_juegos import obtener_juego,obtener_juegos_rebajados, obtener_juegos_recientes, obtener_juegos_recomendados, modificar_juego, buscar_juegos, buscar_juegos_por_genero
from api.queries_carrito import obtener_carrito, comprar_carrito, colocar_item_carrito, sacar_item_carrito, obtener_historial_compras
from api.queries_usuarios import obtener_usuario, validar_usuario, actualizar_usuario, eliminar_usuario, registrar_usuario
from api.queries_usuario_online import loguear_usuario, desloguear_usuario, actualizar_usuario_online, buscar_usuario_online
from api.queries_metodo_pago import obtener_metodos_pago, agregar_metodo_pago

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(__name__, root_path=base_dir)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USE_SSL"] = False
app.config["MAIL_USERNAME"] = "mail"
app.config["MAIL_PASSWORD"] = "clave-temporal"
app.config["MAIL_DEFAULT_SENDER"] = "mail"
mail = Mail(app)


# LOGIN PRIMERO
@app.route("/login", methods=["GET", "POST"])
def login():
    usuario_online = buscar_usuario_online()

    if usuario_online:
        flash("Error, ya hay sesion iniciada")
        return redirect(url_for("index"))

    if request.method == "POST":
        user = request.form["usuario"]
        contra = request.form["contra"]

        validacion_usuario = validar_usuario(user, contra)

        if validacion_usuario == 404:
            flash("Usuario no encontrado. Debe registrarse")
            return redirect(url_for("login"))
        elif validacion_usuario == 401:
            flash("Contaseña Invalida.")
            return redirect(url_for("login"))
        else:
            loguear_usuario(user)
            if validacion_usuario["rol"] == "admin":
                return redirect(url_for("inicioAdmin"))
            else:
                return redirect(url_for("index"))

    return render_template("login.html")


# PAGINA DE PERFIL
@app.route("/verificar_login")
def redirigir_perfil():
    usuario_online = buscar_usuario_online()

    if not usuario_online:
        flash("Necesitás iniciar sesión para acceder a tu perfil.", "error")
        return redirect(url_for("index"))

    return redirect(url_for("perfil", usr = usuario_online["usuario"]))


@app.route("/perfil/<usr>", methods=["GET", "POST"])
def perfil(usr):
    datos_usr = obtener_usuario(usr)

    if datos_usr == None:
        flash("Usuario no Encontrado.")
        return redirect(url_for("login"))

    if request.method == "POST":
        if request.form.get("eliminar"):
            eliminar_usuario(datos_usr["usuario"])
            flash("Perfil eliminado correctamente")
            return redirect(url_for("index"))
        else:
            username = request.form["username"]
            email = request.form["email"]
            contra = request.form["contra"]
            nombre = request.form["nombre"]
            apellido = request.form["apellido"]
            calle = request.form["calle"]
            direccion = request.form["direccion"]
            codigo_postal = request.form["cp"]
            ciudad = request.form["ciudad"]
            pais = request.form["pais"]

            actualizar_usuario(username, email, contra, nombre, apellido, calle, direccion, codigo_postal, ciudad, pais, datos_usr["usuario"])

            actualizar_usuario_online()

            datos_usr = obtener_usuario(username)
            return redirect(url_for("perfil", usr = datos_usr["usuario"]))
          
    return render_template("perfil.html", usuario = datos_usr)

@app.route("/desloguear", methods=["POST"])
def desloguear():

    response = desloguear_usuario()  # falta manejar posibles errores aca nada mas
    return redirect(url_for("index"))


# PAGINA DE ADMIN
@app.route("/admin", methods=["POST", "GET"])
def inicioAdmin():
    usuario_online = buscar_usuario_online()

    if usuario_online:
        if usuario_online["rol"] == "admin":
            juegos_recientes = obtener_juegos_recientes()
            juegos_rebajados = obtener_juegos_rebajados()
            juegos_recomendados = obtener_juegos_recomendados()

            if request.method == "POST":
                id_juego = request.form["id_juego"]
                precio = request.form["precio"]
                porcentaje_oferta = request.form["porcentaje_oferta"]
                en_oferta = request.form["en_oferta"]

                modificar_juego(id_juego, precio, porcentaje_oferta, en_oferta)

                return redirect(url_for("inicioAdmin", juegos_recientes = juegos_recientes, juegos_rebajados = juegos_rebajados, juegos_recomendados = juegos_recomendados))

            return render_template("admin.html", juegos_recientes = juegos_recientes, juegos_rebajados = juegos_rebajados, juegos_recomendados = juegos_recomendados)

        else:
            flash("Necesitas iniciar sesion con una cuenta valida de administrador para esa seccion")
            return redirect(url_for("index"))

    else:
        flash("Error, necesitas iniciar sesion.")
        return redirect(url_for("index"))


# PAGINA DE INICIO USUARIO FINAL
@app.route("/")
def index():
    try:
        juegos_recientes = obtener_juegos_recientes()
        juegos_rebajados = obtener_juegos_rebajados()
        juegos_recomendados = obtener_juegos_recomendados()
    except:
        flash("No se pudo obtener la lista de juegos. El servidor está caído")
        return redirect(url_for("index"))

    return render_template(
        "inicio.html",
        juegos_recientes=juegos_recientes,
        juegos_rebajados=juegos_rebajados,
        juegos_recomendados=juegos_recomendados,
    )


# PAGINA DE BUSQUEDA
@app.route("/buscar")
def buscar():
    query = request.args.get("q", "")
    busqueda = buscar_juegos(query)
    if not busqueda:
        flash("No se han encontrado resultado para la busqueda")
        return redirect(url_for("index"))

    return render_template("buscador.html", busqueda = busqueda)


@app.route("/buscar/<string:genero>")
def buscar_por_genero(genero):
    busqueda = buscar_juegos_por_genero(genero)
    if not busqueda:
        flash("No se han encontrado resultados para la busqueda")
        return redirect(url_for('index'))
    
    return render_template("buscador.html", busqueda = busqueda)

@app.route("/ofertas")
def buscar_ofertas():
    busqueda = obtener_juegos_rebajados()
    if not busqueda:
        flash("No se han encontrado resultados para la busqueda")
        return redirect(url_for('index'))

    return render_template("buscador.html", busqueda = busqueda)


# PAGINA DE DETALLE DE JUEGO
@app.route("/juego/<int:id>")
def ver_juego(id):
    juego = obtener_juego(id)
    if not juego:
        flash(
            "No se puede obtener el juego. El servidor debe estar caido.",
            "Error interno",
        )
        return redirect(url_for("index"))
    return render_template("juego.html", juego=juego)

# PAGINA DE CARRITO
@app.route("/carrito")
def carrito():
    usuario = buscar_usuario_online()

    if usuario:
        itemsCarrito = obtener_carrito()
        total = sum(item["precio"] for item in itemsCarrito)
        return render_template("carrito.html", carrito = itemsCarrito, total=total)

    flash("Para ver tu carrito necesitas iniciar sesión.")
    return redirect(url_for("index"))


# es mejor que el boton solo agregue y no modifique la pagina (en nuestro
# caso deberia estar el boton de comprar solo en la pantalla donde se ve un juego unico)
@app.route("/carrito/agregar", methods=["POST"])
def post_itemCarrito():
    usuario = buscar_usuario_online()
    id = int(request.form["id_juego"])

    if usuario:        
        tipo_envio = "digital" if "opcion_digital" in request.form else "fisico"
        precio = float(request.form["precio"])

        response = colocar_item_carrito(id, tipo_envio, precio)
        flash("Juego agregado a tu carrito!")
        return redirect(url_for("ver_juego", id=id))

    flash("Debes iniciar sesión para agregar items al carrito.")
    return redirect(url_for('ver_juego', id = id))


@app.route("/carrito/eliminar/<int:id>")
def eliminar_itemCarrito(id):
    # usuario = buscar_usuario_online()
    # if usuario:
    response = sacar_item_carrito(id)
    return redirect(url_for("carrito"))

    # flash("Para ver tu carrito necesitas iniciar sesión.")
    # return redirect(url_for('index'))


@app.route("/carrito/comprar")
def comprar_itemsCarrito():

    comprar_carrito()
    flash("Carrito comprado!")
    return redirect(url_for("carrito"))


@app.route("/perfil/historial_carrito")
def ver_historial_compras():

    historial_compras = obtener_historial_compras()
    return render_template("historial_compras.html", compras = historial_compras)


@app.route("/perfil/metodos_pago", methods = ["GET", "POST"])
def ver_metodos_pago():
    usuario_online = buscar_usuario_online()

    metodos_pago = obtener_metodos_pago(usuario_online["usuario_id"])

    if not usuario_online:
        flash("Necesitás iniciar sesión para acceder a tu perfil.")
        return redirect(url_for("index"))
    
    if request.method == "POST":
        tipo = request.form["tipo"]
        marca = request.form["marca"]
        numero_tarjeta = request.form["numero"]
        vencimineto = request.form["vencimiento"]
        codigo_cvv = request.form["numero_cvv"]

        agregado = agregar_metodo_pago(usuario_online["usuario_id"], tipo, marca, numero_tarjeta, vencimineto, codigo_cvv)
        if agregado:
            flash("Metodo de Pago Agregado Exitosamente.")
            metodos_pago = obtener_metodos_pago(usuario_online["usuario_id"])
            return redirect(url_for("ver_metodos_pago", metodos_pago = metodos_pago))

    metodos_pago = obtener_metodos_pago(usuario_online["usuario_id"])

    return render_template("metodos_pago.html", metodos_pago = metodos_pago)


@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contra = request.form["contra"]
        email = request.form["email"]
        nombre = request.form["nombre"]
        apellido = request.form["apellido"]
        pais = request.form["pais"]
        ciudad = request.form["ciudad"]

        registrado = registrar_usuario(usuario, nombre, apellido, email, contra, pais, ciudad)

        if registrado == 201:
            flash("Usuario registrado")
            return redirect(url_for("index"))
        elif registrado == 409:
            flash("Error. El Usuario ya existe.")
            return redirect(url_for("registro"))
        else:
            flash("Error. No se ha podido registrar el Usuario")
            return redirect(url_for("registro"))

    return render_template("registro.html")


if __name__ == "__main__":
    app.run(debug = True, port = 5001)
