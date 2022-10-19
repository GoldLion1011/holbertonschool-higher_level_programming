#!/usr/bin/python3
""" Class definition of Base """

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declaritive import declarative_base

Base = declarative_base()


class State(Base):
    """ State class that inherits from Base"""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, auto_increment=True)
    name = Column(String(128), nullable=False)
