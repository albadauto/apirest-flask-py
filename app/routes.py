from flask import Blueprint, request, jsonify
from .extensions import db
from .models import *
from flask_jwt_extended import (create_access_token, jwt_required, get_jwt_identity)

user_bp = Blueprint('users', __name__)
products_bp = Blueprint('products', __name__)
login_bp = Blueprint('login', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User is created"}), 201

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])

@products_bp.route('/products', methods=['GET'])
def get_products():
    products = Products.query.all()
    return jsonify([p.to_dict() for p in products])

@products_bp.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product = Products(name=data['name'], price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product created"}), 201
    
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
    return jsonify({"message": "User updated"})

@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User id deleted"})

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User(email=data['email'], name=data['name'])
    access_token = create_access_token(identity=user.name)
    return jsonify(access_token=access_token), 200