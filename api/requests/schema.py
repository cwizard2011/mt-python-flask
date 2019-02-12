import graphene
from datetime import datetime

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError

from api.requests.models import Request as RequestModel
from helpers.authentication import Auth
from helpers.user_info import get_user_from_db
from utility.validator import validate_empty_fields, validate_request_field
from utility.handle_error import SaveDatabaseManager


class Request(SQLAlchemyObjectType):
    class Meta:
        model = RequestModel


class CreateRequest(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        details = graphene.String(required=True)

    request = graphene.Field(Request)

    @Auth.user_roles('user')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        validate_request_field(kwargs['title'], kwargs['details'])
        user = get_user_from_db()
        user_id = user.id
        request = RequestModel(
            title=kwargs['title'],
            details=kwargs['details'],
            user_id=user_id,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        with SaveDatabaseManager(request, kwargs['title'], 'Request'):
            return CreateRequest(request=request)


class Query(graphene.ObjectType):
    get_user_request = graphene.List(Request)
    get_single_request = graphene.Field(Request, request_id=graphene.Int())

    @Auth.user_roles('user')
    def resolve_get_user_request(self, info):
        user = get_user_from_db()
        user_id = user.id
        user_request = RequestModel.query.filter_by(user_id=user_id).all()
        if not user_request:
            raise GraphQLError('You have not place any maintenance request')
        return user_request

    def resolve_get_single_request(self, info, request_id):
        user = get_user_from_db()
        user_id = user.id
        single_request = RequestModel.query.filter_by(id=request_id).first()
        if not single_request:
            raise GraphQLError('The request with this id is not found.')
        if single_request and single_request.user_id != user_id:
            raise GraphQLError('The request does not belong to this user')
        return single_request


class Mutation(graphene.ObjectType):
    create_request = CreateRequest.Field()
