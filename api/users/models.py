from sqlalchemy import (Column, String, Integer, Enum)
from sqlalchemy.orm import relationship
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
    user_role = Column(String, nullable=False, default="user")
    image = Column(String)
    
    def __init__(self, password, firstname, lastname, email):
        self.password = generate_password_hash(
            password,
            method='sha256'
        )
        self.firstname = firstname
        self.lastname = lastname
        self.email = email

    def __repr__(self): return self




