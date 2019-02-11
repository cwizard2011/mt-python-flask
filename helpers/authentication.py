import jwt

from flask import request, jsonify
from functools import wraps

from graphql import GraphQLError
from utility.handle_error import handle_http_error

from api.users.models import User


class Authentication:
    """
    Authentication method:
    :methods
        get_token
        decode_token
    """

    def get_token(self):
        token = request.headers['token']
        return token

    def decode_token(self):
        """
        Decodes the auth token
        :param
        :return
            integer|string
        """

        try:
            auth_token = self.get_token()

            if auth_token is None:
                return jsonify({
                    'message': 'Please provide a valid token'
                    }), 401
            payload = jwt.decode(auth_token, verify=False)
            self.user_info = payload['identity']
            return payload['identity']
        except jwt.ExpiredSignatureError:
            return jsonify({
                    'message': 'Signature expired, please login again'
                    }), 401
        except jwt.InvalidTokenError:
            return jsonify({
                    'message': 'Invalid token, please provide a valid token'
                    }), 401

    def user_roles(self, *expected_args):
        """User roles"""

        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                user_data = self.decode_token()
                if type(user_data) is dict:
                    id = user_data['id']
                    user = User.query.filter_by(id=id).first()

                    if user and user.user_role in expected_args:
                        return func(*args, **kwargs)
                    else:
                        message = (
                            'You are not authorized to perform this action')
                        status = 401
                        handle_http_error(message, status, expected_args)
                else:
                    raise GraphQLError(user_data[0].data)

            return wrapper

        return decorator


Auth = Authentication()
