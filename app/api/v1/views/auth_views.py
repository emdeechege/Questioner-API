from flask import jsonify, Blueprint, request, json, make_response
from ..models.auth_models import Users
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

v1_auth_blueprint = Blueprint('auth', __name__, url_prefix='/api/v1')

users = Users()


@v1_auth_blueprint.route('/signup', methods=['POST'])
def signup():
    '''View that controls creation of new users'''
    try:
        data = request.get_json()
    except:
        return make_response(jsonify({
            "status": 400,
            "message": "Wrong input"
        })), 400

    firstname = data.get('firstname')
    lastname = data.get('lastname')
    othername = data.get('othername')
    email = data.get('email')
    phoneNumber = data.get('phoneNumber')
    username = data.get('username')
    isAdmin = data.get('isAdmin')
    password = data.get('password')

    if not firstname:
        return make_response(jsonify({
            "status": 400,
            "message": "Firstname is required"
        })), 400
    if not lastname:
        return make_response(jsonify({
            "status": 400,
            "message": "Lastname is required"
        })), 400
    if not email:
        return make_response(jsonify({
            "status": 400,
            "message": "Email is required"
        })), 400
    if not phoneNumber:
        return make_response(jsonify({
            "status": 400,
            "message": "Phonenumber is required"
        })), 400
    if not username:
        return make_response(jsonify({
            "status": 400,
            "message": "Username is required"
        })), 400
    if not password:
        return make_response(jsonify({
            "status": 400,
            "message": "Password is required"
        })), 400

    password = generate_password_hash(
        password, method='pbkdf2:sha256', salt_length=8)

    user = jsonify(users.signup(
        firstname, lastname, othername, email, phoneNumber, username, isAdmin, password))
    user.status_code = 201
    return user
