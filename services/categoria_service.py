from app import db
from models import Categoria

class CategoriaService:
    @staticmethod
    def crear_categoria(nombre):
        categoria = Categoria(nombre=nombre)
        db.session.add(categoria)
        db.session.commit()
        return categoria
