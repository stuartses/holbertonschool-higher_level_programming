#!/usr/bin/python3

"""10. Get a state
This module prints the State object with the name passed as argument

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

    state_list = session.query(State).filter_by(name=sys.argv[4]).all()

    if state_list == []:
        print("Not found")
    else:
        print(state_list[0].id)

    """
    for state_obj in states_list:
        print("{}: {}".format(state_obj.id, state_obj.name))
    """
