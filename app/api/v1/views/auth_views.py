from flask import jsonify, Blueprint, request, json, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from ..utils.validators import Validation
from ..models.auth_models import Users


v1_auth_blueprint = Blueprint('auth', __name__, url_prefix='/api/v1')

USER = Users()
VALIDATOR = Validation()


@v1_auth_blueprint.route('/signup', methods=['POST'])
def signup():
    """View that controls creation of new users"""
    try:
        data = request.get_json()
    except:
        return jsonify({
            "status": 400,
            "message": "Invalid input"
        }), 400

    firstname = data.get('firstname')
    lastname = data.get('lastname')
    othername = data.get('othername')
    email = data.get('email')
    phone_number = data.get('phone_number')
    username = data.get('username')
    is_admin = data.get('is_admin')
    password = data.get('password')

    if not firstname or not firstname.split():
        return make_response(jsonify({
            "status": 400,
            "message": "Firstname is required"
        })), 400
    if not lastname or not lastname.split():
        return make_response(jsonify({
            "status": 400,
            "message": "Lastname is required"
        })), 400
    if not email or not email.split():
        return make_response(jsonify({
            "status": 400,
            "message": "Email is required"
        })), 400
    if not phone_number:
        return make_response(jsonify({
            "status": 400,
            "message": "Phone number is required"
        })), 400
    if not username or not username.split():
        return make_response(jsonify({
            "status": 400,
            "message": "Username is required"
        })), 400
    if not password or not password.split():
        return make_response(jsonify({
            "status": 400,
            "message": "Password is required"
        })), 400

    if not VALIDATOR.validate_phone_number(phone_number):
        return jsonify({
            "status": 400,
            "message": "Please input valid phone number"
        }), 400

    if VALIDATOR.validate_password(password):
        return jsonify({
            "status": 400,
            "message": "Password not valid"
        }), 400

    if not VALIDATOR.validate_email(email):
        return jsonify({
            "status": 400,
            "message": "Invalid email"
        }), 400

    if VALIDATOR.username_exists(username):
        return jsonify({
            "status": 400,
            "message": "Username exists"
        }), 400

    if VALIDATOR.email_exists(email):
        return jsonify({
            "status": 400,
            "message": "Email exists"
        }), 400

    password = generate_password_hash(
        password, method='pbkdf2:sha256', salt_length=8)

    res = USER.signup(
        firstname, lastname, othername, email, phone_number, username, is_admin, password)
    return jsonify({
        "status": 201,
        "data": [{
            "firstname": firstname,
            "lastname": lastname,
            "othername": othername,
            "email": email,
            "phone_number": phone_number,
            "username": username,
            "is_admin": is_admin
        }]
    }), 201


@v1_auth_blueprint.route('/login', methods=['POST'])
def login():
    """ A view to control users login """
    try:
        data = request.get_json()

    except:
        return make_response(jsonify({
            "status": 400,
            "message": "Wrong input"
        })), 400
    username = data.get('username')
    password = data.get('password')

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

    if not VALIDATOR.username_exists(username):
        return jsonify({
            "status": 404,
            "message": "User does not exist"
        }), 404

    auth_token = user.generate_auth_token(username)
    return make_response(jsonify({
        "status": 200,
        "message": 'Logged in successfuly',
        "token": auth_token
    })), 200
