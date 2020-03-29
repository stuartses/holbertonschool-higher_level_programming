#!/usr/bin/python3

"""14. Cities in state
This module that prints all City objects join States

Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import sys
from model_state import Base, State
from model_city import City

import sqlalchemy
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)

    # create a session
    Session = sqlalchemy.orm.sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    # Join query
    list_cities = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()

    for row in list_cities:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
