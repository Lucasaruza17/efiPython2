from models import User, UserCredentials, Post, Comentario, Categoria
from app import db

# User Repositorio
class UserRepository:
    def get_by_id(self, user_id):
        return User.query.get(user_id)

    def get_by_email(self, email):
        return User.query.filter_by(email=email, is_active=True).first()

    def get_by_username(self, username):
        return User.query.filter_by(username=username, is_active=True).first()

    def get_by_username_or_email(self, username, email):
        return User.query.filter((User.username==username)|(User.email==email)).first()

    def get_all(self):
        return User.query.all()

    def delete(self, user):
        db.session.delete(user)
        db.session.commit()

# Post Repo
class PostRepository:
    def get_all_active(self):
        return Post.query.filter_by(is_active=True).order_by(Post.fecha_creacion.desc()).all()

    def get_by_id(self, post_id):
        return Post.query.get(post_id)

    def save(self, post):
        db.session.add(post)
        db.session.commit()

    def delete(self, post):
        db.session.delete(post)
        db.session.commit()

#Comentario repositor

class ComentarioRepository:
    def get_by_id(self, comment_id):
        return Comentario.query.get(comment_id)

    def save(self, comentario):
        db.session.add(comentario)
        db.session.commit()

    def delete(self, comentario):
        db.session.delete(comentario)
        db.session.commit()


#Categoria repositorio
class CategoriaRepository:
    def get_all(self):
        return Categoria.query.all()

    def get_by_id(self, categoria_id):
        return Categoria.query.get(categoria_id)

    def get_by_ids(self, categoria_ids):
        return Categoria.query.filter(Categoria.id.in_(categoria_ids)).all() if categoria_ids else []

    def save(self, categoria):
        db.session.add(categoria)
        db.session.commit()

    def delete(self, categoria):
        db.session.delete(categoria)
        db.session.commit()
