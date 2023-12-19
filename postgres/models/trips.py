import os
from sqlalchemy import Column, Integer, String, TIMESTAMP, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

Base = declarative_base()


class Trips(Base):
    __tablename__ = 'trips'

    trip_id = Column(Integer, primary_key=True)
    duration_sec = Column(Integer)
    start_date = Column(TIMESTAMP)
    start_station_name = Column(String)
    start_station_id = Column(Integer)
    end_date = Column(TIMESTAMP)
    end_station_name = Column(String)
    end_station_id = Column(Integer)
    bike_number = Column(Integer)
    zip_code = Column(String)
    subscriber_type = Column(String)


def create_engine_and_session(db_uri):
    engine = create_engine(db_uri)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return engine, Session