from database import db

class Material(db.Model):
    id_material = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100), nullable=False)
    titulo = db.Column(db.String(200), nullable=False)
    fecha_ingreso = db.Column(db.String(100))
    estado = db.Column(db.String(100), nullable=False)

    #relacion con categoria
    categoria = db.relationship('Categoria', back_populates='categoria')

    def __init__(self, tipo, titulo, fecha_ingreso, estado):
        self.tipo = tipo
        self.titulo = titulo
        self.fecha_ingreso = fecha_ingreso
        self.estado = estado
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    #devolver los mteriales
    @staticmethod
    def get_all():
        return Material.query.all()
    
    #devolver un solo material
    @staticmethod
    def get_by_id(id_material):
        return Material.query.get(id_material)
    
    #met para actualizar
    def update(self, tipo=None, titulo=None, fecha_ingreso=None, estado=None):
        if tipo and titulo and fecha_ingreso and estado:
            self.tipo = tipo
            self.titulo = titulo
            self.fecha_ingreso = fecha_ingreso
            self.estado = estado
        db.session.commit()
    
    #met para eliminar
    def delete(self):
        db.session.delete(self)
        db.session.commit()

