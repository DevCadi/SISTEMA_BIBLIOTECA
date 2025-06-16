from database import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    correo = db.Column(db.String(100), unique=True)
    contraseña = db.Column(db.String(100))
    rol = db.Column(db.String(20))  # 'admin' o 'bibliotecario'
