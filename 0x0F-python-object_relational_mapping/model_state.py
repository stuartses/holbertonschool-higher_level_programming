#!/usr/bin/python3

"""6. First state model
This module creates a new Base class, State class and states table

Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# Define Base class
Base = declarative_base()


# create table states and Class State
class State(Base):
    """Class State
    Creates a new table states in mySQL db

    """

    __tablename__ = 'states'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=128), nullable=False)
