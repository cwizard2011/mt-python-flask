import graphene
import datetime

from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError
from flask_jwt_extended import create_access_token

from utility.handle_error import SaveDatabaseManager
from api.users.models import User as UserModel
from utility.validator import (
    validate_empty_fields,
    validate_password_length,
    check_email,
    validate_username,
    validate_fullname)

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()
        firstname = graphene.String()
        lastname = graphene.String()
        
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
            token = create_access_token(identity=token_obj, expires_delta=expires)
            return CreateUser(user=user, token=token)

# class LoginUser(graphene.Mutation):

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
