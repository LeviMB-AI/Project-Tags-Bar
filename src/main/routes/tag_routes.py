from flask import Blueprint, request, jsonify

# blueprint para poder dar nomes personalizados as rotas

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])
def create_tags():
    pass