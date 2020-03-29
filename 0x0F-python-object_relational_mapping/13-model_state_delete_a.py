#!/usr/bin/python3

"""13. Delete states
This module deletes all State objects with a name containing the letter 'a'

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

    # delete states
    count_states = session.query(State).filter(
        State.name.like('%a%')).delete(synchronize_session=False)

    session.commit()
