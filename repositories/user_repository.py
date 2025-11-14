from .base_repository import BaseRepository
from models import User

class UserRepository(BaseRepository):
    model = User

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()