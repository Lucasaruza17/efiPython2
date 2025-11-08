from ..extensions import db
from datetime import datetime

class Comentario(db.Model):
    __tablename__ = "comentarios"

    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)

    usuario = db.relationship("User", back_populates="comentarios")
    post = db.relationship("Post", back_populates="comentarios")
    respuestas = db.relationship("Respuesta", back_populates="comentario", cascade="all, delete-orphan")