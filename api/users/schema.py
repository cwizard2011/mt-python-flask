import graphene
import datetime

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from flask_jwt_extended import create_access_token
from graphql import GraphQLError
from werkzeug.security import check_password_hash

from utility.handle_error import SaveDatabaseManager
from api.users.models import User as UserModel
from utility.validator import (
    validate_empty_fields,
    validate_password_length,
    check_email,
    validate_fullname)


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        firstname = graphene.String(required=True)
        lastname = graphene.String(required=True)

    user = graphene.Field(User)
    token = graphene.String()

    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        validate_password_length(kwargs['password'])
        check_email(kwargs['email'])
        validate_fullname(kwargs['firstname'], kwargs['lastname'])
        user = UserModel(**kwargs)
        with SaveDatabaseManager(user, kwargs['email'], 'User'):
            expires = datetime.timedelta(days=1)
            token_obj = {
                "id": user.id,
                "email": user.email,
                "user_role": user.user_role,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "image": user.image
            }
            token = create_access_token(
                identity=token_obj,
                expires_delta=expires)
            return CreateUser(user=user, token=token)


class LoginUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(User)
    token = graphene.String()

    def mutate(self, info, **kwargs):
        validate_empty_fields(**kwargs)
        query_user = User.get_query(info)
        existing_user = query_user.filter(
            UserModel.email == kwargs['email']).first()
        if not existing_user:
            raise GraphQLError("User not found")
        if existing_user and check_password_hash(existing_user.password, kwargs['password']):  # noqa: E501
            expires = datetime.timedelta(days=1)
            token_obj = {
                "id": existing_user.id,
                "email": existing_user.email,
                "user_role": existing_user.user_role,
                "firstname": existing_user.firstname,
                "lastname": existing_user.lastname,
                "image": existing_user.image
            }
            token = create_access_token(
                identity=token_obj,
                expires_delta=expires)
            return CreateUser(user=existing_user, token=token)
        raise GraphQLError("email and password does not match")


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login_user = LoginUser.Field()
