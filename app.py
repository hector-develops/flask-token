from flask import Flask
from views.usuarios import usuario_blueprint
from config import config
from models.usuariomodelo import db


def create_app(enviroment):
    app = Flask(__name__)
    app.config.from_object(enviroment)

    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app


enviroment = config['development']
app = create_app(enviroment)

app.register_blueprint(usuario_blueprint, url_prefix="/usuarios")

if __name__ == "__main__":
    app.run(port=5000)
