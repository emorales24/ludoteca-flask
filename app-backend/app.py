from flask import Flask
import mysql.connector
from routes.usuarios import usuarios_bp
from routes.juegos import juegos_bp
from routes.admin import admin_bp
from routes.items_carrito import items_carrito_bp
from routes.metodos_pago import metodos_pago_bp
from flasgger import Swagger

app = Flask(__name__)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API del sitio web FLASK AND FURIOUS",
        "description": "Documentación de la API de ludoteca",
        "version": "1.0.0",
        "contact": {
            "name": "Equipo Soporte Flask and Furious",
            "email": "calle_falsa_123@fi.uba.ar"
        },
        "basePath": "/"
    },
}
swagger = Swagger(app, template=swagger_template)


app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
app.register_blueprint(juegos_bp, url_prefix="/juegos")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(items_carrito_bp, url_prefix="/carrito")
app.register_blueprint(metodos_pago_bp, url_prefix="/metodos_pago")

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
    