from database import db

class Material(db.Model):
    id_material = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    titulo = db.Column(db.String(200), nullable=False)
    fecha_ingreso = db.Column(db.String(100))
    estado = db.Column(db.String(100), nullable=False)
    id_categoria = db.Column(db.Integer)