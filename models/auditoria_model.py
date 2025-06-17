from database import db
from datetime import datetime

class Auditoria(db.Model):
    __tablename__ = 'auditorias'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(100), nullable=False)
    accion = db.Column(db.String(255), nullable=False)
    fecha = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Auditoria {self.usuario} - {self.accion} - {self.fecha}>'
