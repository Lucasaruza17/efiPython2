from .base_repository import BaseRepository
from models import Comentario

class ComentarioRepository(BaseRepository):
    model = Comentario

    def get_by_post_id(self, post_id):
        return Comentario.query.filter_by(post_id=post_id).all()
