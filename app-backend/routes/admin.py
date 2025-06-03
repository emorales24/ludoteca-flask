from flask import Blueprint, jsonify, request
from db import get_connection

admin_bp = Blueprint("usuarios",__name__)