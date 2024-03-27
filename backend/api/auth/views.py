from flask import request
from flask_restx import Namespace, Resource, fields
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus

auth_namespace = Namespace('auth', description="Namespace for authentication")
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

    def post(self):
        """
        Generate a JWT pair
        """
        pass