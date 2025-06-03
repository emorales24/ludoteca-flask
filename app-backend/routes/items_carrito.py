from flask import Blueprint, jsonify, request
from db import get_connection

items_carrito_bp = Blueprint("usuarios",__name__)