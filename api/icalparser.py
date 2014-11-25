from icalendar import Calendar
from datetime import datetime, date
from helpers import attendee_to_login as to_log, get_room
import requests
from pytz import timezone

UTC = timezone('Europe/Paris')

ICAL_TEST_DIR = "/home/manu/test.ics"


def ical_to_dict(stream):
    """
    get all event of the current day and format them to a dict ready to be encoded in json

    :param stream: icalendar file object from get request
    :return: a dict containing formated data
    :rtype: dict
    """
    ret = []
    content = ""
    day_end = UTC.localize(datetime.combine(date.today(), datetime.max.time()))
    now = UTC.localize(datetime.now())
    for block in stream.iter_content(1024):
        content += block
    cal = Calendar.from_ical(content)
    for ev in cal.walk():
        if ev.name == 'VEVENT':
            if ev.get('DTEND').dt > now >= ev.get('DTSTART').dt:
                event = {'place': ev.get('LOCATION').to_ical(),
                         'name': ev.get('SUMMARY').to_ical(),
                         'personnes': to_log(ev.get('ATTENDEE'))}
                print event
                print ev.get('LOCATION')
    next_ev = [{'name': ev.get('SUMMARY').to_ical(), 'place': ev.get('LOCATION').to_ical().replace('\\', ''),
                'end': str(ev.get('DTEND').dt),
                'start': str(ev.get('DTSTART').dt)}
               for ev in cal.walk()
               if ev.name == "VEVENT" and (now < ev.get('DTSTART').dt <= day_end)]
    print next_ev


r = requests.get('https://www.google.com/calendar/ical/valett_e%40etna-alternance.net/private-dcbad4791bccb7846db0fdd38f9498f8/basic.ics', stream=True)
ical_to_dict(r)