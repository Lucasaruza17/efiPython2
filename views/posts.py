from flask.views import MethodView
from flask import jsonify, request
from services.post_service import PostService
from schemas import PostSchema
from flask_jwt_extended import jwt_required

post_schema = PostSchema()
posts_schema = PostSchema(many=True)


class PostAPI(MethodView):
    @jwt_required(optional=True)
    def get(self, post_id):
        if post_id:
            post = PostService.repo.get_by_id(post_id)
            if not post:
                return jsonify({"msg": "Post no encontrado"}), 404
            return jsonify(post_schema.dump(post))
        posts = PostService.repo.get_all()
        return jsonify(posts_schema.dump(posts))

    @jwt_required()
    def post(self, post_id=None):
        data = request.get_json()
        titulo = data.get("titulo")
        contenido = data.get("contenido")
        usuario_id = data.get("usuario_id")
        categorias = data.get("categorias", [])
        nuevo_post = PostService.crear_post(titulo, contenido, usuario_id, categorias)
        return jsonify(post_schema.dump(nuevo_post)), 201

    @jwt_required()
    def put(self, post_id):
        data = request.get_json()
        post = PostService.repo.get_by_id(post_id)
        if not post:
            return jsonify({"msg": "Post no encontrado"}), 404
        titulo = data.get("titulo")
        contenido = data.get("contenido")
        categorias = data.get("categorias", [])
        actualizado = PostService.editar_post(post, titulo, contenido, categorias)
        return jsonify(post_schema.dump(actualizado))

    @jwt_required()
    def delete(self, post_id):
        post = PostService.repo.get_by_id(post_id)
        if not post:
            return jsonify({"msg": "Post no encontrado"}), 404
        PostService.eliminar_post(post)
        return jsonify({"msg": "Post eliminado"})
