from flask import Flask
import mysql.connector
from routes.usuarios import usuarios_bp
from routes.juegos import juegos_bp
from routes.admin import admin_bp
from routes.items_carrito import items_carrito_bp

app = Flask(__name__)

app.register_blueprint(usuarios_bp, url_prefix="/usuarios") #podria cambiarse por login o dividirse con login
app.register_blueprint(juegos_bp, url_prefix="/juegos")
app.register_blueprint(admin_bp, url_prefix="/admin")
app.register_blueprint(items_carrito_bp, url_prefix="/items_carrito")

# Esto sirve para ver todos los url de los endpoints ya configurados
# descomentar en caso de querer chequear si la nueva peticion fue agregada
# for rule in app.url_map.iter_rules():
#     print(rule)

if __name__ == "__main__":
    app.run(debug = True, port = 5000)
    