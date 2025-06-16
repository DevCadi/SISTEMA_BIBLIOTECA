from database import db
from datetime import datetime

class Devolucion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prestamo_id = db.Column(db.Integer, db.ForeignKey('prestamo.id'), nullable=False)
    fecha_devolucion = db.Column(db.DateTime, default=datetime.utcnow)
    observacion = db.Column(db.String(255))

    prestamo = db.relationship('Prestamo', backref=db.backref('devoluciones', lazy=True))