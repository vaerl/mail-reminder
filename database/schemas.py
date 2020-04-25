from typing import List, Optional
from pydantic import BaseModel
import datetime


class PersonBase(BaseModel):
    name: str
    surname: Optional[str] = None
    birthday: Optional[datetime.datetime] = None


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: int
    name: str
    surname: str
    date: datetime.datetime

    events: List

    class Config:
        orm_mode = True


class EventBase(BaseModel):
    name: str
    type: str
    date: Optional[datetime.date] = None


class EventCreate(EventBase):
    pass


class Event(EventBase):
    id: int
    name: str
    type: str
    date: datetime.datetime

    persons: List

    class Config:
        orm_mode = True
