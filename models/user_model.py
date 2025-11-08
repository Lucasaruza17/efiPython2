from ..extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


# Tabla intermedia opcional (si tus usuarios tienen credenciales separadas)
class UserCredentials(db.Model):
    __tablename__ = "user_credentials"

    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False, unique=True)

    user = db.relationship("User", back_populates="credentials")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class User(db.Model, UserMixin):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role = db.Column(db.String(20), default="user")

    # Relación con credenciales
    credentials = db.relationship("UserCredentials", uselist=False, back_populates="user")

    # Relación con posts y comentarios
    posts = db.relationship("Post", back_populates="usuario", cascade="all, delete-orphan")
    comentarios = db.relationship("Comentario", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<User {self.username}>"

    def set_password(self, password):
        if not self.credentials:
            self.credentials = UserCredentials()
        self.credentials.set_password(password)

    def check_password(self, password):
        if not self.credentials:
            return False
        return self.credentials.check_password(password)
