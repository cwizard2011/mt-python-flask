from graphql import GraphQLError
from datetime import datetime

from utility.database import update_entity_fields


def update_request_status(request_object, updated_status):
    update_entity_fields(
        request_object,
        current_status=updated_status,
        updated_at=datetime.now())
    request_object.save()
    return request_object


def request_action(request, status, action, **kwargs):
    if action == 'approve':
        if status != 'pending' and status != 'rejected':
            raise GraphQLError(
                'You can only approve pending or rejected request')
        update_request_status(request, "approved")
    if action == 'resolve':
        if status != 'approved':
            raise GraphQLError('You can only resolve an approved request')
        update_request_status(request, "resolved")
    if action == 'reject':
        if status != 'pending' and status != 'approved':
            raise GraphQLError(
                'You can only reject a pending or approved request')
        update_request_status(request, "rejected")
