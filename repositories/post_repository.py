from .base_repository import BaseRepository
from models import Post

class PostRepository(BaseRepository):
    model = Post

    def get_by_user_id(self, user_id):
        return Post.query.filter_by(usuario_id=user_id).all()
