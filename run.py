from flask import Flask, redirect, url_for, session
from views.usuario_view import usuario_view
from views.material_view import material_view
from views.copia_view import copia_view
from views.prestamo_view import prestamo_view
from views.reporte_view import reporte_view
from views.auditoria_view import auditoria_view
from views.devolucion_view import devolucion_view
from database import db

app = Flask(__name__)
app.secret_key = 'clave_secreta_para_sesiones'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/biblioteca.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Registrar blueprints
app.register_blueprint(usuario_view)
app.register_blueprint(material_view)
app.register_blueprint(copia_view)
app.register_blueprint(prestamo_view)
app.register_blueprint(reporte_view)
app.register_blueprint(devolucion_view)
app.register_blueprint(auditoria_view)

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