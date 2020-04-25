from sqlalchemy.orm import Session
from typing import List
import array
import datetime
from . import models, schemas


def get_today_events(db: Session) -> List[models.Event]:
    return db.query(models.Event).filter(models.Event.date == datetime.date.today())


def get_today_birthdays(db: Session) -> List[schemas.Person]:
    return db.query(models.Person).filter(models.Person.birthday == datetime.date.today())


# TODO create_*: add support for specifying id and/or name to establish connection
def create_person(db: Session, person: schemas.PersonCreate) -> models.Person:
    db_person = models.Person(
        name=person.name, surname=person.surname, birthday=person.birthday)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


def create_event(db: Session, event: schemas.Event):
    # TODO implement
    # TODO implement update_*()
    return None
