from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from typing import List
from .database import Base
from sqlalchemy.sql.schema import Table
from .types import Type

association_table = Table('association', Base.metadata,
                          Column('person_id', Integer,
                                 ForeignKey('persons.id')),
                          Column('event_id', Integer, ForeignKey('events.id'))
                          )


class Person(Base):
    __tablename__ = "persons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False, index=True)
    surname = Column(String, unique=False, index=True)
    birthday = Column(DateTime)

    events = relationship(
        "Event",
        secondary=association_table,
        back_populates="persons")


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    type = Column(Enum(Type))
    date = Column(DateTime)

    persons = relationship(
        "Person",
        secondary=association_table,
        back_populates="events")
