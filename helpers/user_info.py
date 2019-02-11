from helpers import authentication
from api.users.models import User


def get_user_from_db():
    user_token = authentication.Auth.decode_token()
    user_id = user_token['id']
    user = User.query.filter_by(id=user_id).first()
    return user
