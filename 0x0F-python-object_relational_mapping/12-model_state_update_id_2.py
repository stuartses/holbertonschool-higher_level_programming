#!/usr/bin/python3

"""12. Update a state
This module changes the name of a State object

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

    # update state
    state_obj = session.query(State).get(2)
    state_obj.name = "New Mexico"
    session.commit()
