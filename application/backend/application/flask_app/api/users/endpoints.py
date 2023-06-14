import flask
from flask import Blueprint, request, current_app
from flask_cors import cross_origin
from sqlalchemy.orm.exc import NoResultFound

from flask_app.api.users.models import User

user_route = Blueprint('user_route', __name__)

# @user_route.route("/api/v2/user/signup", methods=['POST'])
# def signup():
#     data = request.get_json()

# @user_route.route("/api/v2/user/login", methods=['POST'])
# def login():
#     data = request.get_json()

def get_user_json(user):
    return {
        "username": user.username,
        "email": user.email,
    }

def get_users_json(users):
    return {
        "users": [get_user_json(user) for user in users]
    }

def get_clean_username(username: str):
    return username.strip().lower()

@user_route.route("/api/v1/users", methods=['GET'])
@cross_origin(origin='*')
def get_user():
    print(request)
    if request.method == 'GET':
        args = request.args
        try:
            if 'phone_number' in args:
                phone_number = args.get('phone_number').lstrip()
                if phone_number[0] != '+':
                    phone_number = '+' + phone_number
                user = current_app.session.query(User).filter(User.phone_number == phone_number).one()
            elif 'username' in args:
                username = get_clean_username(args.get('username'))
                user = current_app.session.query(User).filter(User.username == username).one()
            else:
                users = current_app.session.query(User).all()
                return flask.jsonify(get_users_json(users)), 200

        except NoResultFound as nrf:
            return "User not found", 404
        
        response = flask.jsonify(get_user_json(user))
        return response, 200
    else:
        return "Method not allowed", 405

# @user_route.route("/api/v1/user/test", methods=['POST'])
# def create_test_user():
#     new_user = User(
#         username="tinynakji",
#         email="tinynakji@gmail.com",
#     )

#     current_app.session.add(new_user)
#     current_app.session.commit()

#     return str(new_user)