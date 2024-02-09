from flask import Blueprint, request, jsonify

# blueprint para poder criar várias rotas que vão estar linkadas com esse nome vindo do blueprint
tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create_tag', methods=["POST"])
def create_tags():
    #body da requisição
    print(request.json)
    return jsonify({ "resp": "ok"}), 200
