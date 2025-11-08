from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    from views import PostAPI, ComentarioAPI, CategoriaAPI, UserAPI
    app.register_blueprint(PostAPI)
    app.register_blueprint(ComentarioAPI)
    app.register_blueprint(CategoriaAPI)
    app.register_blueprint(UserAPI)

    return app
