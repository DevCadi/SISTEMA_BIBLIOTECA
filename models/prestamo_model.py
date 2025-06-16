from database import db
from datetime import datetime, timedelta

class Prestamo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    copia_id = db.Column(db.Integer, db.ForeignKey('copia.id'), nullable=False)
    usuario = db.Column(db.String(100), nullable=False)  # nombre del lector
    fecha_prestamo = db.Column(db.Date, default=datetime.utcnow)
    fecha_devolucion = db.Column(db.Date, default=lambda: datetime.utcnow() + timedelta(days=7))
    estado = db.Column(db.String(20), default='activo')

    copia = db.relationship('Copia', backref=db.backref('prestamos', lazy=True))