from datetime import datetime, date
from icalendar import Calendar
from pytz import timezone
from helpers import attendee_to_login as to_log
import logging

UTC = timezone('Europe/Paris')


def ical_to_dict(stream):
    """
    get all event of the current day and format them to a dict ready to be encoded in json

    :param stream: icalendar file object from get request
    :return: a dict containing formated data
    :rtype: dict
    """

    ret = []
    try:
        content = stream.content
    except AttributeError:
        logging.error('Bad ics file provided')
        return False
    day_end = UTC.localize(datetime.combine(date.today(), datetime.max.time()))
    now = UTC.localize(datetime.now())
    try:
        cal = Calendar.from_ical(content)
    except ValueError:
        logging.error('Bad ics file provided')
        return False
    for ev in cal.walk():
        if ev.name == 'VEVENT':
            if ev.get('DTEND').dt > now >= ev.get('DTSTART').dt:
                event = {'place': ev.get('LOCATION').to_ical(),
                         'name': ev.get('SUMMARY').to_ical(),
                         'personnes': to_log(ev.get('ATTENDEE'))}
                ret.append(event)
    next_ev = [{'name': ev.get('SUMMARY').to_ical(), 'place': ev.get('LOCATION').to_ical().replace('\\', ''),
                'end': str(ev.get('DTEND').dt),
                'start': str(ev.get('DTSTART').dt)}
               for ev in cal.walk()
               if ev.name == "VEVENT" and (now < ev.get('DTSTART').dt <= day_end)]
    val = {'current_events': ret, 'next_events': next_ev}
    return val
