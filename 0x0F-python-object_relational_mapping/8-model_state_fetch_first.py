#!/usr/bin/python3
"""class definition of a State"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).first()

    if (result):
        print("{}: {}".format(result.id, result.name))
    else:
        print("Nothing")

