from datetime import datetime, date, timedelta
from icalendar import Calendar
import pytz
from helpers import attendee_to_login as to_log, format_room, set_utc, format_dt
import logging


def ev_to_partial_dict(ev):
    return {
        'name': ev.get('SUMMARY').to_ical(),
        'place': format_room(ev.get('LOCATION').to_ical().replace('\\', '')),
        'end': format_dt(set_utc(ev.get('DTEND').dt)),
        'start': format_dt(set_utc(ev.get('DTSTART').dt))
    }


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
            if ev_end > now >= ev_start:
                event = {'place': format_room(ev.get('LOCATION').to_ical()),
                         'name': ev.get('SUMMARY').to_ical(),
                         'personnes': to_log(ev.get('ATTENDEE')),
                         'start': format_dt(ev_start),
                         'desc': ev.get('DESCRIPTION').to_ical(),
                         'end': format_dt(ev_end)}
                ret.append(event)
    next_ev = [ev_to_partial_dict(ev)
               for ev in cal.walk()
               if ev.name == "VEVENT" and (now < ev.get('DTSTART').dt <= day_end)]
    next_day = [ev_to_partial_dict(ev)
                for ev in cal.walk()
                if ev.name == "VEVENT" and (day_end < ev.get('DTSTART').dt <= day_end + timedelta(days=1))]
    next_ev = sorted(next_ev, key=lambda k: k['start'])
    val = {'current_events': ret, 'next_events': next_ev, 'next_day': next_day}
    return val
