from flask.views import MethodView
from flask import jsonify, request
from ..services.comentario_service import ComentarioService
from schemas import ComentarioSchema
from flask_jwt_extended import jwt_required

comentario_schema = ComentarioSchema()
comentarios_schema = ComentarioSchema(many=True)


class ComentarioAPI(MethodView):
    @jwt_required(optional=True)
    def get(self, post_id):
        comentarios = ComentarioService.repo.get_by_post_id(post_id)
        return jsonify(comentarios_schema.dump(comentarios))

    @jwt_required()
    def post(self, post_id):
        data = request.get_json()
        texto = data.get("texto")
        usuario_id = data.get("usuario_id")
        nuevo_comentario = ComentarioService.crear_comentario(texto, usuario_id, post_id)
        return jsonify(comentario_schema.dump(nuevo_comentario)), 201

    @jwt_required()
    def delete(self, comment_id):
        comentario = ComentarioService.repo.get_by_id(comment_id)
        if not comentario:
            return jsonify({"msg": "Comentario no encontrado"}), 404
        ComentarioService.eliminar_comentario(comentario)
        return jsonify({"msg": "Comentario eliminado"})
