from flask import Blueprint
from controllers.auditoria_controller import auditoria_controller

auditoria_view = Blueprint('auditoria_view', __name__)
auditoria_view.register_blueprint(auditoria_controller)
