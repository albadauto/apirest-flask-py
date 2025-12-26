from flask import Blueprint, request, jsonify

from .extensions import db
from .models import *

user_bp = Blueprint('users', __name__)
products_bp = Blueprint('products', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Usuário criado"}), 201


@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@products_bp.route('/products', methods=['GET'])
def get_products():
    products = Products.query.all()
    return jsonify(products)
    
@user_bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())


@user_bp.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json


    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)


    db.session.commit()
    return jsonify({"message": "Usuário atualizado"})


@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuário deletado"})