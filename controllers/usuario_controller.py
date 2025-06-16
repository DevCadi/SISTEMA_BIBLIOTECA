from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.usuario_model import Usuario
from database import db

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        usuario = Usuario.query.filter_by(correo=correo, contraseña=contraseña).first()
        if usuario:
            session['usuario_id'] = usuario.id
            session['usuario_rol'] = usuario.rol
            return redirect(url_for('dashboard'))
        flash('Credenciales incorrectas')
    return render_template('login.html')
