from app import db
from models import User, UserCredentials
from werkzeug.security import generate_password_hash

class UserService:
    @staticmethod
    def crear_usuario(username, email, password):
        nuevo_usuario = User(username=username, email=email)
        db.session.add(nuevo_usuario)
        db.session.commit()

        cred = UserCredentials(user_id=nuevo_usuario.id)
        cred.set_password(password)
        db.session.add(cred)
        db.session.commit()
        return nuevo_usuario
