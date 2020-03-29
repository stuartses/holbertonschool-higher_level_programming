#!/usr/bin/python3

"""7. All states via SQLAlchemy
This module print the first object found in State Query

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

    state_obj = session.query(State).first()

    if state_obj is None:
        print("Nothing")
    else:
        print("{}: {}".format(state_obj.id, state_obj.name))
