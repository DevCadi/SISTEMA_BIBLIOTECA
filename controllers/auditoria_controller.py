from flask import Blueprint, render_template
from models.auditoria_model import Auditoria
from database import db

auditoria_controller = Blueprint('auditoria_controller', __name__)

@auditoria_controller.route('/auditoria')
def index_auditoria():
    registros = Auditoria.query.order_by(Auditoria.fecha.desc()).all()
    return render_template('auditoria/index.html', registros=registros)

def registrar_evento(usuario, accion):
    registro = Auditoria(usuario=usuario, accion=accion)
    db.session.add(registro)
    db.session.commit()