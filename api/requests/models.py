from sqlalchemy import (Column, String, Integer, DateTime, ForeignKey)
from sqlalchemy.orm import relationship, validates

from helpers.database import Base
from utility.database import Utility


class Request(Base, Utility):
    __tablename__ = 'requests'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('userlist.id'))
    title = Column(String, nullable=False, unique=True)
    details = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    current_status = Column(String, nullable=False, server_default="pending")
    userlist = relationship('User', foreign_keys=user_id)

    @validates('title')
    def convert_upper(self, key, value):
        return value.title()
