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


if __name__ == '__main__':
    meetups = ['elastic-switzerland',
               'Zurich-Apache-Kafka-Meetup-by-Confluent',
               'Machine-Learning-Artificial-Intelligence-Meetup-Bern',
               'docker-switzerland']

    for meetup in meetups:
        get_upcoming_meetups_for_group(meetup)
