from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from p187 import Base, Sensor, Station

def populate(engine):
    #Base.metadata.bind = engine
    Session = sessionmaker(bind=engine)
    session = Session()

    de_bilt = Station(name="De Bilt")
    session.add(de_bilt)

    session.add(Station(name='Utrecht'))
    session.commit()
    print("Station", de_bilt)

    temp_sensor = Sensor(last=20, multiplier=0.1, station=de_bilt)
    session.add(temp_sensor)
    session.commit()
    print("Sensor", temp_sensor)


if __name__ == "__main__":
    print("This script is used by another script. Run python alchemy_query.py")


