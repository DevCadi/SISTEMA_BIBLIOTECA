from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.prestamo_model import Prestamo
from models.copia_model import Copia
from database import db
from datetime import datetime, timedelta

prestamo_bp = Blueprint('prestamo_controller', __name__)

@prestamo_bp.route('/prestamos')
def index_prestamos():
    prestamos = Prestamo.query.all()
    return render_template('prestamos/index.html', prestamos=prestamos)

@prestamo_bp.route('/prestamos/crear', methods=['GET', 'POST'])
def crear_prestamo():
    copias = Copia.query.filter_by(estado='disponible').all()
    if request.method == 'POST':
        nuevo = Prestamo(
            copia_id=request.form['copia_id'],
            usuario=request.form['usuario'],
            fecha_prestamo=datetime.strptime(request.form['fecha_prestamo'], '%Y-%m-%d'),
            fecha_devolucion=datetime.strptime(request.form['fecha_devolucion'], '%Y-%m-%d'),
            estado='activo'
        )
        db.session.add(nuevo)
        copia = Copia.query.get(request.form['copia_id'])
        copia.estado = 'prestado'
        db.session.commit()
        flash('Préstamo registrado')
        return redirect(url_for('prestamo_controller.index_prestamos'))
    return render_template('prestamos/create.html', copias=copias)

@prestamo_bp.route('/prestamos/devolver/<int:id>', methods=['POST'])
def devolver_prestamo(id):
    prestamo = Prestamo.query.get_or_404(id)
    prestamo.estado = 'devuelto'
    copia = Copia.query.get(prestamo.copia_id)
    copia.estado = 'disponible'
    db.session.commit()
    flash('Préstamo devuelto correctamente')
    return redirect(url_for('prestamo_controller.index_prestamos'))
