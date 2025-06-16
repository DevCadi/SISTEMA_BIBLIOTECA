from flask import Blueprint
from controllers.usuario_controller import usuario_controller

usuario_view = Blueprint('usuario_view', __name__)
usuario_view.register_blueprint(usuario_controller)
