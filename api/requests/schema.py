import graphene
from datetime import datetime

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError

from api.requests.models import Request as RequestModel
from helpers.authentication import Auth
from helpers.user_info import get_user_from_db
from helpers.get_request_from_db import get_request_from_db
from utility.validator import validate_empty_fields, validate_request_field
from utility.handle_error import SaveDatabaseManager
from utility.database import update_entity_fields


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
        validate_request_field(**kwargs)
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


class UpdateRequest(graphene.Mutation):
    class Arguments:
        request_id = graphene.Int(required=True)
        title = graphene.String()
        details = graphene.String()

    request = graphene.Field(Request)

    @Auth.user_roles('user')
    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        validate_request_field(**kwargs)
        message = 'Admin is working on this request, it can\'t be updated'
        request = get_request_from_db(
            kwargs['request_id'], action='update', message=message)
        update_entity_fields(request, updated_at=datetime.now(), **kwargs)
        if 'title' in kwargs:
            with SaveDatabaseManager(request, kwargs['title'], 'Request'):
                return UpdateRequest(request=request)
        request.save()
        return UpdateRequest(request=request)


class DeleteRequest(graphene.Mutation):
    class Arguments:
        request_id = graphene.Int(required=True)

    request = graphene.Field(Request)

    @Auth.user_roles('user')
    def mutate(self, info, request_id, **kwargs):
        message = 'Admin is working on this request, it can\'t be deleted'
        request = get_request_from_db(
            request_id, action='delete', message=message)
        update_entity_fields(request, **kwargs)
        request.delete()
        return DeleteRequest(request=request)


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
        request = get_request_from_db(request_id)
        return request


class Mutation(graphene.ObjectType):
    create_request = CreateRequest.Field()
    update_request = UpdateRequest.Field()
    delete_request = DeleteRequest.Field()
