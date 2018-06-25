import os
import time

import requests


TIME_FORMAT = '%Y-%m-%d %H:%M'


def format_time(timestamp):
    return time.strftime(TIME_FORMAT, time.localtime(timestamp))


def get_upcoming_meetups_for_group(group_name):
    current_time = time.time()

    params = {'group_urlname': group_name}
    r = requests.get('https://api.meetup.com/2/events', params=params)
    try:
        events = r.json()['results']
    except:
        return

    for e in events:
        event_name = e['name']
        event_time = e['time'] / 1000
        if event_time > current_time:
            event_date = format_time(event_time)
            print('%s (%s)' % (event_name, event_date))


def find_groups(country=None, text=None):
    api_key = os.environ.get('API_KEY')

    if not api_key:
        raise ValueError("The environmental variable 'API_KEY' has to be set"
                         + " in order to use the 'find_groups' method")

    params = {'country': country,
              'text': text,
              'sign': True,
              'key': api_key}
    r = requests.get('https://api.meetup.com/find/groups', params=params)
    groups = r.json()

    return groups


if __name__ == '__main__':
    groups = find_groups('switzerland', 'machine learning')
    for g in groups:
        print(g['name'])
        get_upcoming_meetups_for_group(g['urlname'])
