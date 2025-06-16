from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.devolucion_model import Devolucion
from models.prestamo_model import Prestamo
from models.copia_model import Copia
from database import db
from datetime import datetime

devolucion_bp = Blueprint('devolucion_controller', __name__)

@devolucion_bp.route('/devoluciones')
def index_devoluciones():
    devoluciones = Devolucion.query.all()
    return render_template('devoluciones/index.html', devoluciones=devoluciones)

@devolucion_bp.route('/devoluciones/registrar/<int:prestamo_id>', methods=['GET', 'POST'])
def registrar_devolucion(prestamo_id):
    prestamo = Prestamo.query.get_or_404(prestamo_id)
    if request.method == 'POST':
        devolucion = Devolucion(
            prestamo_id=prestamo.id,
            fecha_devolucion=datetime.utcnow(),
            observacion=request.form['observacion']
        )
        prestamo.estado = 'devuelto'
        copia = Copia.query.get(prestamo.copia_id)
        copia.estado = 'disponible'

        db.session.add(devolucion)
        db.session.commit()
        flash('Devolución registrada correctamente')
        return redirect(url_for('devolucion_controller.index_devoluciones'))
    return render_template('devoluciones/registrar.html', prestamo=prestamo)
