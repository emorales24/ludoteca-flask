from flask import Flask
import mysql.connector
from routes.usuarios import usuarios_bp
from routes.juegos import juegos_bp
from routes.admin import admin_bp
from routes.items_carrito import items_carrito_bp
from routes.metodos_pago import metodos_pago_bp
from routes.registro import registro_bp

app = Flask(__name__)


app.register_blueprint(usuarios_bp, url_prefix="/usuarios")
app.register_blueprint(juegos_bp, url_prefix="/juegos")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(items_carrito_bp, url_prefix="/carrito")
app.register_blueprint(metodos_pago_bp, url_prefix="/metodos_pago")
app.register_blueprint(registro_bp, url_prefix="/registro")

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
    