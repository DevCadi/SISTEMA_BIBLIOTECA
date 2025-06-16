from database import db

class Copia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.Integer, db.ForeignKey('material.id'), nullable=False)
    codigo_interno = db.Column(db.String(20), unique=True, nullable=False)
    estado = db.Column(db.String(20), default='disponible')
    ubicacion = db.Column(db.String(100))

    material = db.relationship('Material', backref=db.backref('copias', lazy=True))