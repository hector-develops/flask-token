from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models.usuariomodelo import Usuarios
from models.usuariomodelo import db
import uuid



usuario_blueprint = Blueprint('usuarios', __name__)


@usuario_blueprint.route('/nuevo', methods=['POST'])
def nuevo_usuario():

    data = request.get_json()

    hashed_password = generate_password_hash(data['password'], method='sha256')

    nuevo_usuario = Usuarios(id_publico=str(uuid.uuid4()), nombres_usuario=data['name'], password_usuario=hashed_password)

    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'message': 'Nuevo usuario Creado'})

def editar_usuario():
    pass