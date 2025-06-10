from flask import Flask, render_template, jsonify, request, redirect
from flask_mail import Mail, Message
import os
import requests

# base_dir es /ruta/completa/app-frontend
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

template_dir = os.path.join(base_dir, "templates")
static_dir = os.path.join(base_dir, "static")

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

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
