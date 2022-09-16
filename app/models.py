from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class Circuit(Base):
    __tablename__ = "circuit"

    circuitId = Column(Integer, primary_key=True, index=True)
    circuitRef = Column(String)
    name = Column(String)
    location = Column(String)
    country = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    alt = Column(Integer)
    url = Column(String)


class Constructor(Base):
    __tablename__ = "constructor"

    constructorId = Column(Integer, primary_key=True, index=True)
    constructorRef = Column(String)
    name = Column(String)
    nationality = Column(String)
    url = Column(String)


class Driver(Base):
    __tablename__ = "driver"

    driverId = Column(Integer, primary_key=True, index=True)
    driverRef = Column(String)
    number = Column(Float, nullable=True)
    code = Column(String, nullable=True)
    dob = Column(String)
    nationality = Column(String)
    url = Column(String)
    name_forename = Column(String)
    name_surname = Column(String)


class PitStop(Base):
    __tablename__ = "pitstop"

    raceId = Column(Integer, primary_key=True, index=True)
    driverId = Column(Integer, ForeignKey("driver.driverId"))
    stop = Column(Integer)
    lap = Column(Integer)
    time = Column(String)
    duration = Column(String)
    milliseconds = Column(Integer)


class Race(Base):
    __tablename__ = "race"

    raceId = Column(Integer, primary_key=True, index=True)
    year = Column(Integer)
    round = Column(Integer)
    circuitId = Column(Integer)
    name = Column(String)
    date = Column(String)
    time = Column(String)
    url = Column(String)


class Result(Base):
    __tablename__ = "result"

    resultId = Column(Integer, primary_key=True, index=True)
    raceId = Column(Integer, ForeignKey("race.raceId"))
    driverId = Column(Integer, ForeignKey("driver.driverId"))
    constructorId = Column(Integer, ForeignKey("constructor.constructorId"))
    number = Column(Integer)
    grid = Column(Integer)
    position = Column(Integer, nullable=True)
    positionText = Column(String)
    positionOrder = Column(Integer)
    points = Column(Float)
    laps = Column(Integer)
    time = Column(String, nullable=True)
    milliseconds = Column(String, nullable=True)
    fastestLap = Column(String, nullable=True)
    rank = Column(String, nullable=True)
    fastestLapTime = Column(String, nullable=True)
    fastestLapSpeed = Column(String, nullable=True)
    statusId = Column(Integer)


class Qualifying(Base):
    __tablename__ = "qualifying"

    qualifyId = Column(Integer, primary_key=True, index=True)
    raceId = Column(Integer, ForeignKey("race.raceId"))
    driverId = Column(Integer, ForeignKey("driver.driverId"))
    constructorId = Column(Integer, ForeignKey("constructor.constructorId"))
    number = Column(String)
    position = Column(String)
    q1 = Column(String)
    q2 = Column(String, nullable=True)
    q3 = Column(String, nullable=True)


class LabTimesSplit(Base):
    __tablename__ = "labtimessplit"

    raceId = Column(Integer, primary_key=True, index=True)
    driverId = Column(Integer, ForeignKey("driver.driverId"))
    lab = Column(Integer)
    position = Column(Integer)
    time = Column(String)
    milliseconds = Column(Integer)
