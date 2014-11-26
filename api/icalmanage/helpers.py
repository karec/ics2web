from datetime import datetime
from pytz import timezone


def attendee_to_login(attendee):
    """
    Get a list of vCalAddress and return a list of string without domain name in mail address

    :param attendee: list of vCalAddress
    :return: list of string
    :rtype: list
    """
    if not attendee:
        return attendee
    ret = []
    for i in attendee:
        ret.append(i.to_ical().split('mailto:')[1].split('@')[0])
    return ret


def set_utc(dt):
    """
    This function is used for correct a bug in icalendar datetime from google agendat
    It will add the utc offset of the localised current datetime to the dt param and return it

    :param dt: the datetime to update
    :return: dt
    :rtype: datetime
    """
    utc_of = timezone('Europe/Paris')
    now = datetime.now()
    return dt + utc_of.utcoffset(now)


def get_room(events, room):
    """
    Get all events from events dict where event is in location room

    :param events: dictionary of events
    :type events: dict
    :param room: the name of the room
    :type room: str
    :return: a list of events for the given room
    :rtype: list
    """
    pass


def format_dt(dt):
    """
    return a formated string from dt object
    It will remove utc information

    :param dt: datetime object to format
    :type dt: datetime
    :return: the formated string
    :rtype: str
    """
    return dt.replace(tzinfo=None).isoformat()


def format_room(room):
    """
    Format room name for display

    :param room: The string representing the room
    :type room: str
    :return: the formatted string
    :rtype: str
    """
    room = room.replace('Salle - ', '')
    room = room.replace('SM -', 'Salle')
    return room