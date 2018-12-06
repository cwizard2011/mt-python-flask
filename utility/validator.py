from email_validator import validate_email, EmailNotValidError
from graphql import GraphQLError

def validate_empty_fields(**kwargs):
    """
    Function to validate empty fields when
    saving an object
    :params kwargs
    """
    for field in kwargs:
        if not kwargs.get(field):
            raise AttributeError(field + " is required field")

def validate_password_length(password):
    """
    Function to validate length of password 
    when saving user password to database
    :params password
    """
    if len(password) < 8 or len(password) > 32:
        raise AttributeError("password must be between 8 and 32 characters")

def validate_username(username):
    """
    Function to validate username
    when saving username to database
    :params username
    """
    if len(username) < 5 or len(username) > 15:
        raise AttributeError("username must be between 5 and 15 characters")

def check_email(email):
    """
    Function to validate email
    when saving email to database
    :params email
    """
    try:
        v = validate_email(email)
        email = v["email"]
    except EmailNotValidError:
        raise AttributeError("email is not valid")

def validate_fullname(firstname, lastname):
    """
    Function to validate firstname and lastname
    when saving firstname and lastname to database
    :params firstname, lastname
    """
    if not firstname.replace(' ', '').isalpha() or len(firstname) < 3 or len(firstname) > 15:
        raise AttributeError("firstname can only be alphabets between 3 to 15 characters")
    if not lastname.replace(' ', '').isalpha() or len(lastname) < 3 or len(lastname) > 15:
        raise AttributeError("lastname can only be alphabets between 3 to 15 characters")

class ErrorHandler():
    '''Handles error'''

    def check_conflict(self, entity_name, entity):
        # Database integrity error
        raise GraphQLError(
            '{} {} already exists'.format(entity_name, entity))

    def foreign_key_conflict(self, entity_name, entity):
        # Database foreign key error
        raise GraphQLError(
            '{} {} does not exists'.format(entity_name, entity))

    def db_connection(self):
        # Database connection error
        raise GraphQLError('Error: Could not connect to Db')