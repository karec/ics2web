from datetime import datetime, date, timedelta
from icalendar import Calendar
import pytz
from helpers import attendee_to_login as to_log, format_room, set_utc, format_dt
import logging


def ev_to_partial_dict(ev):
    """
    Return a dict for a given event, this dict is for next_events only

    :param ev: icalendar event object
    :return: a dict containing basic informations about the event
    """
    ev_start = ev.get('DTSTART').dt
    ev_end = ev.get('DTEND').dt
    if not isinstance(ev_start, datetime) and not isinstance(ev_end, datetime):
        ev_start = datetime.combine(ev_start, datetime.min.time()).replace(tzinfo=pytz.UTC)
        ev_end = datetime.combine(ev_end, datetime.max.time()).replace(tzinfo=pytz.UTC)
        ev_end = ev_end - timedelta(days=1)
    return {
        'name': ev.get('SUMMARY').to_ical(),
        'place': format_room(ev.get('LOCATION').to_ical().replace('\\', '')),
        'end': format_dt(set_utc(ev_end)),
        'start': format_dt(set_utc(ev_start)),
        'desc': ev.get('DESCRIPTION').to_ical()
    }


def check_event_next_day(ev, day_end):
    """
    Check if an event occur the nex day

    :param ev: icalendar event object
    :param day_end: the end of the current day
    :return: True or False for the event
    """
    if ev.name != "VEVENT":
        return False
    ev_start = set_utc(ev.get('DTSTART').dt)
    if not isinstance(ev_start, datetime):
        ev_start = datetime.combine(ev_start, datetime.min.time()).replace(tzinfo=pytz.UTC)
    return day_end < ev_start <= day_end + timedelta(days=1)


def check_event_current(ev, day_end):
    """
    Check if an event is today and after now

    :param ev: icalendar event object
    :param day_end: the end of the current day
    :return: True or False for the event
    """
    if ev.name != "VEVENT":
        return False
    ev_start = set_utc(ev.get('DTSTART').dt)
    if not isinstance(ev_start, datetime):
        ev_start = datetime.combine(ev_start, datetime.min.time()).replace(tzinfo=pytz.UTC)
    now = set_utc(datetime.now(tz=pytz.UTC))
    return now < ev_start <= day_end


def ical_to_dict(stream):
    """
    get all event of the CURRENT day and format them to a dict ready to be encoded in json

    :param stream: icalendar file object from get request
    :return: a dict containing formated data
    :rtype: dict
    """
    ret = []
    try:
        if hasattr(stream, 'content'):
            content = stream.content
        else:
            content = stream.read()
    except AttributeError:
        logging.error('Bad ics file provided')
        return False
    day_end = datetime.combine(date.today(), datetime.max.time()).replace(tzinfo=pytz.UTC)
    now = set_utc(datetime.now(tz=pytz.UTC))
    try:
        cal = Calendar.from_ical(content)
    except ValueError:
        logging.error('Bad ics file provided')
        return False
    for ev in cal.walk():
        if ev.name == 'VEVENT':
            ev_start = set_utc(ev.get('DTSTART').dt)
            ev_end = set_utc(ev.get('DTEND').dt)
            if not isinstance(ev_start, datetime) and not isinstance(ev_end, datetime):
                ev_start = datetime.combine(ev_start, datetime.min.time()).replace(tzinfo=pytz.UTC)
                ev_end = datetime.combine(ev_end, datetime.max.time()).replace(tzinfo=pytz.UTC)
                ev_end = ev_end - timedelta(days=1)
            if ev_end > now >= ev_start:
                event = {'place': format_room(ev.get('LOCATION').to_ical()),
                         'name': ev.get('SUMMARY').to_ical(),
                         'personnes': to_log(ev.get('ATTENDEE')),
                         'start': format_dt(ev_start),
                         'desc': ev.get('DESCRIPTION').to_ical(),
                         'end': format_dt(ev_end)}
                ret.append(event)
    next_ev = [ev_to_partial_dict(ev) for ev in cal.walk() if check_event_current(ev, day_end)]
    next_day = [ev_to_partial_dict(ev) for ev in cal.walk() if check_event_next_day(ev, day_end)]
    next_ev = sorted(next_ev, key=lambda k: k['start'])
    val = {'current_events': ret, 'next_events': next_ev, 'next_day': next_day}
    return val
