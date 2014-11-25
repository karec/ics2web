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


def get_room(events, room):
    """
    Get all events from events dict where event is in location room

    :param events: dictionary of events
    :type events: list
    :param room: the name of the room
    :type room: str
    :return: a list of events for the given room
    :rtype: list
    """
    pass