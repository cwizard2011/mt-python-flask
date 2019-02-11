import graphene
from datetime import datetime

from graphene_sqlalchemy import (SQLAlchemyObjectType)

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


class Mutation(graphene.ObjectType):
    create_request = CreateRequest.Field()
