from extensions import db
from models import Comentario

class ComentarioService:
    @staticmethod
    def crear_comentario(texto, usuario_id, post_id):
        comentario = Comentario(texto=texto, usuario_id=usuario_id, post_id=post_id)
        db.session.add(comentario)
        db.session.commit()
        return comentario