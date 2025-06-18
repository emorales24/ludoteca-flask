from flask import Blueprint, render_template, request, redirect, flash
import mysql.connector
import re
from db import get_connection

registro_bp = Blueprint('registro', __name__)

def validar_formulario(usuario, contraseña, email, nombre, apellido, calle, numero, codigo_postal):
    errores = []

    if not re.match(r'^[a-zA-Z0-9_]{4,20}$', usuario):
        errores.append("Usuario inválido. Debe tener entre 4 y 20 caracteres alfanuméricos.")

    if not re.match(r'^.{6,}$', contraseña):
        errores.append("La contraseña debe tener al menos 6 caracteres.")

    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        errores.append("Email inválido.")

    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,30}$', nombre):
        errores.append("Nombre inválido.")

    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]{2,30}$', apellido):
        errores.append("Apellido inválido.")

    if not re.match(r'^.{2,50}$', calle):
        errores.append("Calle inválida.")

    if not re.match(r'^\d{1,5}$', numero):
        errores.append("Número de domicilio inválido.")

    if not re.match(r'^\d{4,8}$', codigo_postal):
        errores.append("Código postal inválido.")

    return errores


@registro_bp.route('/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']
        email = request.form['email']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        calle = request.form['calle']
        numero = request.form['numero']
        codigo_postal = request.form['codigo_postal']

        errores = validar_formulario(usuario, contraseña, email, nombre, apellido, calle, numero, codigo_postal)

        if errores:
            for error in errores:
                flash(error, 'error')
            return render_template('registro.html'), 400
        
        try:
            conn = get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM usuarios WHERE usuario = %s OR email = %s", (usuario, email))
            existente = cursor.fetchone()
            if existente:
                flash('Ya existe un usuario con ese nombre o email.', 'error')
                return render_template('registro.html'), 400


            query = """
                INSERT INTO usuarios (rol, usuario, contraseña, email, nombre, apellido, calle, direccion, codigo_postal)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = ('final', usuario, contraseña, email, nombre, apellido, calle, numero, codigo_postal)

            cursor.execute(query, valores)
            conn.commit()

            cursor.close()
            conn.close()

            flash('¡Registro exitoso! Iniciá sesión.')
            return redirect('/login'), 201

        except mysql.connector.Error as err:
            flash(f'Error en el registro: {err}', 'error')
            return render_template('registro.html'), 500


    return render_template('registro.html')
