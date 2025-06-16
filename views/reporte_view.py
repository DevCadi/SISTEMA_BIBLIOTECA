from flask import Blueprint
from controllers.reporte_controller import reporte_controller

reporte_view = Blueprint('reporte_view', __name__)
reporte_view.register_blueprint(reporte_controller)
