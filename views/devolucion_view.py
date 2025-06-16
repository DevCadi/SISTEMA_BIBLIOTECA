from flask import Blueprint
from controllers.devolucion_controller import devolucion_controller

devolucion_view = Blueprint('devolucion_view', __name__)
devolucion_view.register_blueprint(devolucion_controller)
