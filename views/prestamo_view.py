from flask import Blueprint
from controllers.prestamo_controller import prestamo_controller

prestamo_view = Blueprint('prestamo_view', __name__)
prestamo_view.register_blueprint(prestamo_controller)
