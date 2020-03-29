#!/usr/bin/python3

"""city model
This module creates a new City class and cities table

Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

from model_state import Base
import sqlalchemy

# create table states and Class City
class City(Base):
    """Class City
    Creates a new table cities in mySQL db

    """

    __tablename__ = 'cities'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=128), nullable=False)
    state_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey('states.id'),
                                 nullable=False)
