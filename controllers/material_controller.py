from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.material_model import Material
from database import db

material_bp = Blueprint('material_controller', __name__)

@material_bp.route('/materiales')
def index_materiales():
    materiales = Material.query.all()
    return render_template('materiales/index.html', materiales=materiales)

@material_bp.route('/materiales/crear', methods=['GET', 'POST'])
def crear_material():
    if request.method == 'POST':
        nuevo = Material(
            isbn=request.form['isbn'],
            titulo=request.form['titulo'],
            autor=request.form['autor'],
            editorial=request.form['editorial'],
            anio=request.form['anio'],
            edicion=request.form['edicion'],
            genero=request.form['genero'],
            descripcion=request.form['descripcion'],
            palabras_clave=request.form['palabras_clave']
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Material creado exitosamente')
        return redirect(url_for('material_controller.index_materiales'))
    return render_template('materiales/create.html')

@material_bp.route('/materiales/editar/<int:id>', methods=['GET', 'POST'])
def editar_material(id):
    material = Material.query.get_or_404(id)
    if request.method == 'POST':
        material.isbn = request.form['isbn']
        material.titulo = request.form['titulo']
        material.autor = request.form['autor']
        material.editorial = request.form['editorial']
        material.anio = request.form['anio']
        material.edicion = request.form['edicion']
        material.genero = request.form['genero']
        material.descripcion = request.form['descripcion']
        material.palabras_clave = request.form['palabras_clave']
        db.session.commit()
        flash('Material actualizado')
        return redirect(url_for('material_controller.index_materiales'))
    return render_template('materiales/edit.html', material=material)