from flask import Flask
# from flask_cors import CORS
import mysql.connector
from routes.usuarios import usuarios_bp
from routes.juegos import juegos_bp
from routes.admin import admin_bp
from routes.items_carrito import items_carrito_bp

app = Flask(__name__)
# CORS(app)

app.register_blueprint(usuarios_bp, url_prefix="usuarios") #podria cambiarse por login o dividirse con login
app.register_blueprint(juegos_bp, url_prefix="juegos")
app.register_blueprint(admin_bp, url_prefix="admin")
app.register_blueprint(items_carrito_bp, url_prefix="items_carrito")

if __name__ == "__main__":
    app.run(debug=True)