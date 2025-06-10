import os
from flask import Flask, render_template, jsonify, request, redirect
from flask_mail import Mail, Message
import requests

dir_padre = os.path.join(os.path.dirname(__file__), '..')

app = Flask(__name__, root_path = dir_padre)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'mail'
app.config['MAIL_PASSWORD'] = 'clave-temporal' # Password generado desde las passwords para aplicaciones en configuracion de cuenta google.
app.config['MAIL_DEFAULT_SENDER'] = 'mail'
mail = Mail(app)

API_BASE = "http://locahost:5000" # Conexion con la API de app_backend

if __name__ == '__main__':
    app.run(debug = True, port = 5001)