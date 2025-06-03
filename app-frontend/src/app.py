import os
from flask import Flask, render_template, jsonify, request, redirect
from flask_mail import Mail, Message
import requests

dir_padre = os.path.join(os.path.dirname(__file__), '..')

app = Flask(__name__, root_path=dir_padre)

if __name__ == 'main':
    app.run(debug = True)