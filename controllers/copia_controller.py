from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.copia_model import Copia
from models.material_model import Material
from database import db

copia_controller = Blueprint('copia_controller', __name__)

@copia_controller.route('/copias')
def index_copias():
    copias = Copia.query.all()
    return render_template('copias/index.html', copias=copias)

@copia_controller.route('/copias/crear', methods=['GET', 'POST'])
def crear_copia():
    materiales = Material.query.all()
    if request.method == 'POST':
        nueva = Copia(
            material_id=request.form['material_id'],
            codigo_interno=request.form['codigo_interno'],
            estado=request.form['estado'],
            ubicacion=request.form['ubicacion']
        )
        db.session.add(nueva)
        db.session.commit()
        flash('Copia registrada exitosamente')
        return redirect(url_for('copia_controller.index_copias'))
    return render_template('copias/create.html', materiales=materiales)

@copia_controller.route('/copias/editar/<int:id>', methods=['GET', 'POST'])
def editar_copia(id):
    copia = Copia.query.get_or_404(id)
    materiales = Material.query.all()
    if request.method == 'POST':
        copia.material_id = request.form['material_id']
        copia.codigo_interno = request.form['codigo_interno']
        copia.estado = request.form['estado']
        copia.ubicacion = request.form['ubicacion']
        db.session.commit()
        flash('Copia actualizada')
        return redirect(url_for('copia_controller.index_copias'))
    return render_template('copias/edit.html', copia=copia, materiales=materiales)