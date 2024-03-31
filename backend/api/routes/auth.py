from flask import request
from flask_restx import Namespace, Resource, fields
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_required,
                                get_jwt_identity)

auth_namespace = Namespace('Authentication', description="Namespace for authentication")

signup_schema = auth_namespace.model(
    'SignUp', {
        'id': fields.Integer(description="User Identification Number"),
        'username': fields.String(required=True, description="Username"),
        'email': fields.String(required=True, description="User Email"),
        'password': fields.String(required=True, description="User Password"),

    }
)

user_schema = auth_namespace.model(
    'User', {
        'id': fields.Integer(description="User Identification Number"),
        'username': fields.String(required=True, description="Username"),
        'email': fields.String(required=True, description="User Email"),
        'password_hash': fields.String(required=True, description="User Password"),
        'is_active': fields.Boolean(decription="This shows that User is active"),
        'is_staff': fields.Boolean(decription="This shows if User is a staff")
    }
)

login_schema = auth_namespace.model(
    'Login', {
        'email': fields.String(required=True, description="Email"),
        'password': fields.String(required=True, description="Password")
    }
)


@auth_namespace.route('/signup')
class SignUp(Resource):

    @auth_namespace.expect(signup_schema)
    @auth_namespace.marshal_with(user_schema)
    def post(self):
        """
        Create new user
        """
        data = request.get_json()
        new_user = User(
            username=data.get('username'),
            email=data.get('email'),
            password_hash=generate_password_hash(data.get('password'))
        )

        new_user.save()
        return new_user, HTTPStatus.CREATED


@auth_namespace.route('/login')
class Login(Resource):

    @auth_namespace.expect(login_schema)
    def post(self):
        """
        Generate a JWT pair
        """
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        user = User.query.filter_by(email=email).first()
        if (user is not None) and check_password_hash(user.PasswordHash, password):

            access_token = create_access_token(identity=user.Username)
            refresh_token = create_refresh_token(identity=user.Username)

            response = {
                'access_token': access_token,
                'refresh_token': refresh_token,
            }

            return response, HTTPStatus.OK


@auth_namespace.route('/refresh')
class Refresh(Resource):

    @jwt_required(refresh=True)
    def post(self):

        username = get_jwt_identity()
        access_token = create_access_token(identity=username)

        return {'access_token': access_token}, HTTPStatus.OK
