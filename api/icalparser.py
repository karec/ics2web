from icalendar import Calendar
from datetime import datetime, date
from helpers import attendee_to_login as to_log
import requests
from pytz import timezone
import requests_cache


UTC = timezone('Europe/Paris')

ICAL_TEST_DIR = "/home/manu/test.ics"

requests_cache.configure('/tmp/cache', expire_after=10)


def ical_to_dict(stream):
    """
    get all event of the current day and format them to a dict ready to be encoded in json

    :param stream: icalendar file object from get request
    :return: a dict containing formated data
    :rtype: dict
    """

    ret = []
    content = r.content
    day_end = UTC.localize(datetime.combine(date.today(), datetime.max.time()))
    now = UTC.localize(datetime.now())
    cal = Calendar.from_ical(content)
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


r = requests.get('https://www.google.com/calendar/ical/valett_e%40etna-alternance.net/private-dcbad4791bccb7846db0fdd38f9498f8/basic.ics', stream=True)
print ical_to_dict(r)