from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class Usuarios(db.Model):

    """Useario Modelo"""
    __tablename__ = "tbl_usuarios_empresa"
    id_usuario_empresa = db.Column(db.Integer, primary_key=True)
    id_publico = db.Column(db.String(50), unique=True)
    nombres_usuario = db.Column(db.String(50))
    apellidos_usuario = db.Column(db.String(50))
    password_usuario = db.Column(db.String(80))
    status_usuario = db.Column(db.Boolean)
    fk_tipousuario = db.Column(db.String(25))
    fk_licencia = db.Column(db.String(25))
    fecha_registro = db.Column(db.DateTime, default=datetime.datetime.now)

class Tipousuarios(db.Model):

    """Tabla de perfiles de usuario"""
    __tablename__ = "tbl_perfil_usuarios"
    id_perfil_usurio = db.Column(db.Integer, primary_key=True)
    serie_perfil = db.Column(db.String(12), unique=True)
    nombre_perfil = db.Column(db.String(40))
    fk_usuario_alta = db.Column(db.String(25))
    fecha_alta = db.Column(db.DateTime, default=datetime.datetime.now)
