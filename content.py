from database import crud, models, database, types, schemas
from sqlalchemy.orm import Session
from random import randrange

# create all tables
models.Base.metadata.create_all(bind=database.engine)

# TODO outsource strings
birthday_today_messages = {
    1: "It's {}'s birthday! Make sure to congratulate them.",
    2: "{} turns one year older today!",
    3: "{}'s birthday is today!",
    4: "{} has birthday today!"
}

additional_birthday_today_messages = {
    1: "There's another birthday today: {}!",
    2: "{} also has birthday today!",
    3: "{} also turns one year older today!"
}

birthday_today_with_event_messages = {
    1: "It's {}'s birthday today! Their party is on {} at {}.",
    2: "{} turns one year older today! Their party is on {} at {}.",
    3: "{}'s birthday is today! Their party is on {} at {}.",
    4: "{} has birthday today! Their party is on {} at {}.",
    5: "It's {}'s birthday today! They've invited you for {} on {}.",
    6: "{} turns one year older today! They've invited you for {} on {}.",
    7: "{}'s birthday is today! They've invited you for {} on {}.",
    8: "{} has birthday today! They've invited you for {} on {}."
}

birthday_tomorrow_messages = {
    1: "It's {}'s birthday tomorrow! Make sure to congratulate them.",
    2: "{} turns one year older tomorrow!",
    3: "{}'s birthday is tomorrow!",
    4: "{} has birthday tomorrow!"
}

birthday_tomorrow_with_event_messages = {
    1: "It's {}'s birthday tomorrow! Their party is on {} at {}.",
    2: "{} turns one year older tomorrow! Their party is on {} at {}.",
    3: "{}'s birthday is tomorrow! Their party is on {} at {}.",
    4: "{} has birthday tomorrow! Their party is on {} at {}.",
    5: "It's {}'s birthday tomorrow! They've invited you for {} on {}.",
    6: "{} turns one year older tomorrow! They've invited you for {} on {}.",
    7: "{}'s birthday is tomorrow! They've invited you for {} on {}.",
    8: "{} has birthday tomorrow! They've invited you for {} on {}."
}

birthday_messages = {
    1: "It's {}'s birthday on {}! Make sure to congratulate them.",
    2: "{} turns one year older on {}!",
    3: "{}'s birthday is on {}!",
    4: "{} has birthday on {}!"
}

birthday_with_event_messages = {
    1: "It's {}'s birthday on {}! Their party is on {} at {}.",
    2: "{} turns one year older on {}! Their party is on {} at {}.",
    3: "{}'s birthday is on {}! Their party is on {} at {}.",
    4: "{} has birthday on {}! Their party is on {} at {}.",
    5: "It's {}'s birthday on {}! They've invited you for {} on {}.",
    6: "{} turns one year older on {}! They've invited you for {} on {}.",
    7: "{}'s birthday is on {}! They've invited you for {} on {}.",
    8: "{} has birthday on {}! They've invited you for {} on {}."
}

event_today_messages = {
    1: "You have your appointment {} at {}.",
    2: "Remember: today you have your appointment {} at {}!"
}

event_today_with_person_messages = {
    1: "You have your appointment {} at {}. {} will also be there."
}


# TODO outsource xml
def today() -> str:
    """Returns todays' birthdays and events."""
    birthdays = ["<h1>Today</h1>"]

    db = database.SessionLocal()
    message = ""

    persons = crud.get_today_birthdays(db)
    if persons:
        birthdays.append("<h3>Birthdays</h3>")
        for person in persons:
            print(person)
            birthdays.append("<p>")
            name = person.name + " " + person.surname

            # check if there are related events with type party
            party: schemas.Event = None
            for event in person.events:
                if event.type.name == "party":
                    party = event

            # set message if party is present
            if party:
                message = birthday_today_with_event_messages.get(
                    randrange(100) % len(birthday_today_with_event_messages)).format(name, party.date.timetuple())
            else:
                message = birthday_today_messages.get(
                    randrange(100) % len(birthday_today_messages)).format(name)

            birthdays.append(message)
            birthdays.append("</p>")

    return "".join(message)


def up_next() -> str:
    """Returns events in the next two weeks."""
    events = ["<h1>Up Next</h1>"]
    events.append("<p>Implement!<p>")
    return "".join(events)


def news() -> str:
    """Returns some current news."""
    appointments = ["<h1>News</h1>"]
    appointments.append("<p>Implement!<p>")
    return "".join(appointments)


def status() -> str:
    """Returns the current status: added/updated/deleted entries, ..."""
    status = ["<h1>Status</h1>"]
    status.append("<p>Implement!<p>")
    return "".join(status)
