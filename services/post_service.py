from ..extensions import db
from ..models import Post, Categoria

class PostService:
    @staticmethod
    def get_all():
        return [post.to_dict() for post in Post.query.all()]
    def crear_post(titulo, contenido, user_id, categorias=None):
        nuevo_post = Post(titulo=titulo, contenido=contenido, usuario_id=user_id)
        if categorias:
            nuevo_post.categorias.extend(categorias)
        db.session.add(nuevo_post)
        db.session.commit()
        return nuevo_post



