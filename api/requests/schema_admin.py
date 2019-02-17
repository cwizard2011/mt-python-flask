import graphene

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError

from api.requests.models import Request as RequestModel
from helpers.authentication import Auth
from api.requests.schema import Request
from utility.validator import (
    validate_empty_fields,
    validate_request_action_field)
from helpers.admin_role import request_action


class AdminAction(SQLAlchemyObjectType):
    class Meta:
        model = RequestModel


class UpdateRequestStatus(graphene.Mutation):
    class Arguments:
        request_id = graphene.Int()
        action = graphene.String()

    request = graphene.Field(AdminAction)

    @Auth.user_roles('admin', 'super_admin')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        validate_request_action_field(kwargs['action'])
        request = RequestModel.query.filter_by(
            id=kwargs['request_id']).first()
        if not request:
            raise GraphQLError('The request with this id does not exist')
        status = request.current_status
        request_action(request, status, kwargs['action'])
        return UpdateRequestStatus(request=request)


class Query(graphene.ObjectType):
    get_all_request = graphene.List(Request)

    @Auth.user_roles('admin', 'super_admin')
    def resolve_get_all_request(self, info):
        all_requests = RequestModel.query.all()
        return all_requests


class Mutation(graphene.ObjectType):
    update_request_status = UpdateRequestStatus.Field()
