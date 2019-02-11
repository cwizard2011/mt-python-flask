from graphql import GraphQLError
from flask_json import JsonError

from sqlalchemy import exc
from utility.validator import ErrorHandler


class SaveDatabaseManager():
    '''Manage sqlalchemy exceptions.'''

    def __init__(self, model_obj, entity_name, entity):
        self.model_obj = model_obj
        self.entity_name = entity_name
        self.entity = entity

    def __enter__(self):
        try:
            self.model_obj.save()
        except exc.IntegrityError as err:
            res = 'Database integrity error'
            if "duplicate key value violates unique constraint" in str(err):
                res = ErrorHandler.check_conflict(
                    self, self.entity_name, self.entity)
            elif "violates foreign key constraint" in str(err):
                res = ErrorHandler.foreign_key_conflict(
                    self, self.entity_name, self.entity)
            return res
        except exc.DBAPIError:
            return ErrorHandler.db_connection(self)

    def __exit__(self, type, value, traceback):
        return False


def handle_http_error(*args):
    """
    Handle exceptionn raised when there is http error.
    """
    message, status, expected_args = args
    if 'REST' in expected_args:
        raise JsonError(message=message, status=status)
    raise GraphQLError(message)
