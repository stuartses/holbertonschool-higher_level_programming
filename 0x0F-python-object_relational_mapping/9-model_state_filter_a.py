#!/usr/bin/python3

"""9. Contains `a`
This module lists all State objects that contain the letter a

Holberton School
Foundations - Higher-level programming - Python
By Stuart Echeverry
"""

import sys
from model_state import Base, State
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

    states_list = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)

    for state_obj in states_list:
        print("{}: {}".format(state_obj.id, state_obj.name))
