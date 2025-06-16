from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.usuario_model import Usuario
from database import db
from werkzeug.security import check_password_hash

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']

        usuario = Usuario.query.filter_by(correo=correo).first()

        if usuario and check_password_hash(usuario.contraseña_hash, contraseña):
            session['usuario_id'] = usuario.id
            session['usuario_rol'] = usuario.rol
            flash('Bienvenido al sistema')
            return redirect(url_for('dashboard'))

        flash('Credenciales incorrectas')
    return render_template('login.html')