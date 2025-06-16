from flask import Flask, redirect, url_for, session, render_template
from controllers import usuario_controller, reporte_controller, prestamo_controller, material_controller, devolucion_controller, copia_controller, auditoria_controller
from models.material_model import Material
from models.copia_model import Copia
from models.prestamo_model import Prestamo
from models.usuario_model import Usuario
from database import db

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registrar blueprints
app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(material_controller.material_bp)
app.register_blueprint(copia_controller.copia_bp)
app.register_blueprint(prestamo_controller.prestamo_bp)
app.register_blueprint(reporte_controller.reporte_bp)
app.register_blueprint(devolucion_controller.devolucion_bp)
app.register_blueprint(auditoria_controller.auditoria_bp)

@app.route('/')
def home():
    if 'usuario_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('usuario_view.login'))
@app.route('/dashboard')
def dashboard():
    total_materiales = Material.query.count()
    copias_disponibles = Copia.query.filter_by(estado='disponible').count()
    prestamos_activos = Prestamo.query.filter_by(estado='activo').count()
    total_usuarios = Usuario.query.count()
    return render_template('dashboard.html',
        total_materiales=total_materiales,
        copias_disponibles=copias_disponibles,
        prestamos_activos=prestamos_activos,
        total_usuarios=total_usuarios
    )

if __name__ == '__main__':
    app.run(debug=True)