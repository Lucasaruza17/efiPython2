from app import db

class BaseRepository:
    model = None

    def get_all(self):
        return self.model.query.all()

    def get_by_id(self, id):
        return self.model.query.get(id)

    def save(self, instance):
        db.session.add(instance)
        db.session.commit()
        return instance

    def delete(self, instance):
        db.session.delete(instance)
        db.session.commit()

    def filter_by(self, **kwargs):
        return self.model.query.filter_by(**kwargs).all()
