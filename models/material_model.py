from database import db

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    titulo = db.Column(db.String(200), nullable=False)
    autor = db.Column(db.String(100))
    editorial = db.Column(db.String(100))
    anio = db.Column(db.String(4))
    edicion = db.Column(db.String(50))
    genero = db.Column(db.String(50))
    descripcion = db.Column(db.Text)
    palabras_clave = db.Column(db.String(100))