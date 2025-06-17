from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.usuario_model import Usuario
from views import usuario_view
from werkzeug.security import check_password_hash

usuario_bp = Blueprint('usuario', __name__, url_prefix="/usuarios")

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

#inicié desde acá pdt. Adri
@usuario_bp.route("/")
def index():
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)

@usuario_bp.route("/create", methods = ['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contraseña_hash = request.form['contaseña_hash']
        correo = request.form['correo']
        telefono = request.form['telefono']
        tipo = request.form['tipo']

        usuario = Usuario(nombre, apellido, contraseña_hash, correo, telefono, tipo)
        usuario.save()
        return redirect(url_for('usuario.index'))
    return usuario_view.create()

@usuario_bp.route("/edit/<int:id_usuario>", methods = ['GET', 'POST'])
def edit(id_usuario):
    usuario = Usuario.get_by_id(id_usuario)
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        contraseña_hash = request.form['contaseña_hash']
        correo = request.form['correo']
        telefono = request.form['telefono']
        tipo = request.form['tipo']
        #actualizar
        usuario.update(nombre=nombre, apellido=apellido, contraseña_hash=contraseña_hash, correo=correo, telefono=telefono, tipo=tipo)
        return redirect(url_for('usuario.index'))
    return usuario_view.edit(usuario)

@usuario_bp.route("/delete/<int:id_usuario>")
def delete(id_usuario):
    usuario = Usuario.get_by_id(id_usuario)
    usuario.delete()
    return redirect(url_for('usuario.index'))