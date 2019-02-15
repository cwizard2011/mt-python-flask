from .user_info import get_user_from_db
from graphql import GraphQLError

from api.requests.models import Request


def get_request_from_db(request_id, action=None, message=None):
    """Checking if a user request exist in the database"""
    user = get_user_from_db()
    request = Request.query.filter_by(id=request_id, user_id=user.id).first()
    if not request:
        raise GraphQLError(
            'The request with this id does not belong to this user')
    if request and action:
        if request.current_status != 'pending':
            raise GraphQLError(message)
        return request
    return request
