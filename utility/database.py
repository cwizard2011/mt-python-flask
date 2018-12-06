from helpers.database import db_session
from flask_bcrypt import Bcrypt


def update_entity_fields(entity, **kwargs):
    """
    Function to update an entities fields
    :param kwargs
    :param entity
    """
    keys = kwargs.keys()
    for key in keys:
        exec("entity.{0} = kwargs['{0}']".format(key))
    return entity

def password_is_valid(self, password):
        """
        Checks the password against it's hash to validates the user's password
        """
        return Bcrypt().check_password_hash(self.password, password)


class Utility(object):

    def save(self):
        """Function for saving new objects"""
        db_session.add(self)
        db_session.commit()

    def delete(self):
        """Function for deleting objects"""
        db_session.delete(self)
        db_session.commit()