from flask.views import MethodView
from flask import jsonify, request
from services.user_service import UserService
from schemas import UserSchema
from flask_jwt_extended import jwt_required

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserAPI(MethodView):
    @jwt_required()
    def get(self, user_id):
        if user_id:
            user = UserService.repo.get_by_id(user_id)
            if not user:
                return jsonify({"msg": "Usuario no encontrado"}), 404
            return jsonify(user_schema.dump(user))
        users = UserService.repo.get_all()
        return jsonify(users_schema.dump(users))

    @jwt_required()
    def delete(self, user_id):
        user = UserService.repo.get_by_id(user_id)
        if not user:
            return jsonify({"msg": "Usuario no encontrado"}), 404
        UserService.repo.delete(user)
        return jsonify({"msg": "Usuario eliminado"})

    @jwt_required()
    def patch(self, user_id):
        data = request.get_json()
        role = data.get("role")
        user = UserService.repo.get_by_id(user_id)
        if not user:
            return jsonify({"msg": "Usuario no encontrado"}), 404
        user.role = role
        UserService.repo.save(user)
        return jsonify({"msg": "Rol actualizado", "role": user.role})
