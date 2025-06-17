from database import db
from werkzeug.security import generate_password_hash, check_password_hash
    
class Usuario(db.Model):
    id_usuario  = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellido = db.Column(db.String(150))
    contraseña_hash = db.Column(db.String(255))
    correo = db.Column(db.String(100), unique=True)
    telefono = db.Column(db.Integer, nullable = False)
    tipo = db.Column(db.String(20))  # 'lector o admin' o 'bibliotecario'

    def set_password(self, password):
        self.contraseña_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.contraseña_hash, password)
    
    def __init__(self, nombre, apellido, contraseña_hash, correo, telefono, tipo):
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña_hash = contraseña_hash
        self.correo = correo
        self.telefono = telefono
        self.tipo = tipo

    #tener un obj de tipo usuario y guardarlo en la bd
    def save(self):
        db.session.add(self)
        db.session.commit()

    #método para devolver los usuarios de la tabla usuarios
    @staticmethod #no depende de la clase
    def get_all():
        return Usuario.query.all()
    
    #metodo para recuperar un solo registro
    @staticmethod
    def get_by_id(id_usuario):
        return Usuario.query.get(id_usuario)
    
    #metodo para actualizar
    def update(self, nombre=None, apellido=None, contraseña_hash=None, correo=None, telefono=None, tipo=None):
        if nombre and apellido and contraseña_hash and correo and telefono and tipo:
            self.nombre = nombre
            self.apellido = apellido
            self.contraseña_hash = contraseña_hash
            self.correo = correo
            self.telefono = telefono
            self.tipo = tipo
        db.session.commit()
    
    #metodo delete
    def delete(self):
        db.session.delete(self)
        db.session.commit()