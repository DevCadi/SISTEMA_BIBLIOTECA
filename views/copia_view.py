from flask import Blueprint
from controllers.copia_controller import copia_controller

copia_view = Blueprint('copia_view', __name__)
copia_view.register_blueprint(copia_controller)
