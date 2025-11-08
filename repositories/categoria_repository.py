from .base_repository import BaseRepository
from models import Categoria

class CategoriaRepository(BaseRepository):
    model = Categoria

    def get_by_name(self, nombre):
        return Categoria.query.filter_by(nombre=nombre).first()
