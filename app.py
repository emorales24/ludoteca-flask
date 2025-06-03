from flask import Flask
from flask_cors import CORS
import mysql.connector
from routes.usuarios import usuarios_bp
# from routes.juegos import juegos_bp
# from routes.itemscarrito import itemscarrito_bp

app = Flask(__name__)
CORS(app)


# app.register_blueprint(carritos_bp,url_prefix)
app.register_blueprint(usuarios_bp)

if __name__ == "__main__":
    app.run(debug=True)