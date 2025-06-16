from flask import Blueprint
from controllers.material_controller import material_controller

material_view = Blueprint('material_view', __name__)
material_view.register_blueprint(material_controller)
