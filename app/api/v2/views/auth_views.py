from flask import jsonify, Blueprint, request, json, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from ..utils.validators import Validation
from ..models.auth_models import Users


v2_auth = Blueprint('authenticate', __name__, url_prefix='/api/v2')

user = Users()
validator = Validation()


@v2_auth.route('/signup', methods=['POST'])
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

    """ Check for empty inputs"""
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
    if not phone_number or not phone_number.split():
        return make_response(jsonify({
            "status": 400,
            "message": "Phonenumber is required"
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

    if not validator.validate_phone_number(phone_number):
        return jsonify({
            "status": 400,
            "message": "Please input valid phone number"
        }), 400

    if validator.validate_password(password):
        return jsonify({
            "status": 400,
            "message": "Password not valid"
        }), 400

    if not validator.validate_email(email):
        return jsonify({
            "status": 400,
            "message": "Invalid email"
        }), 400

    if validator.username_exists(username):
        return jsonify({
            "status": 400,
            "message": "Username exists"
        }), 400

    if validator.email_exists(email):
        return jsonify({
            "status": 400,
            "message": "Email exists"
        }), 400

    password = generate_password_hash(
        password, method='pbkdf2:sha256', salt_length=8)

    res = user.signup(
        firstname, lastname, othername, email, phone_number, username, is_admin, password)

    username = data.get('username')
    is_admin = data.get('is_admin')

    auth_token = user.generate_auth_token(username, is_admin)
    return jsonify(res, {
        "status": 201,
        "token": auth_token,
        "message": "successfuly registered"
    }), 201

@v2_auth.route('/login', methods=['POST'])
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

    if not validator.username_exists(username):
        return jsonify({
            "status": 404,
            "message": "User does not exist"
        }), 404

    curr = user.db.conn.cursor()
    login_query = "SELECT * FROM users WHERE username = '%s'" % (
        username)
    curr.execute(login_query)
    record = curr.fetchall()

    for user_data in record:
        found_password = user_data[7]
        found_username = user_data[6]
        is_admin = user_data[8]
        if found_username:
            if check_password_hash(found_password, password):
                access_token = user.generate_auth_token(username, is_admin)
                return jsonify({"Message": "User logged in successfully",\
                 "status": 200, \
                 "data": [{"token": access_token,\
                  "Welcome back": found_username}]}), 200
            return jsonify({
                "status": 404,
                "message": "Please input valid credentials"
            }), 404
