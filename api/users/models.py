from sqlalchemy import (Column, String, Integer)
from werkzeug.security import generate_password_hash

from helpers.database import Base

from utility.database import Utility


class User(Base, Utility):
    __tablename__ = 'userlist'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    user_role = Column(String, nullable=False)
    image = Column(String)

    def __init__(
        self,
        user_role='user',
        **kwargs
            ):
        self.password = generate_password_hash(
            kwargs['password'],
            method='sha256'
        )
        self.firstname = kwargs['firstname']
        self.lastname = kwargs['lastname']
        self.email = kwargs['email']
        self.user_role = user_role

    def __repr__(self): return self
