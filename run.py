import meetup


if __name__ == '__main__':
    groups = meetup.find_groups('switzerland', 'machine learning')
    for g in groups:
        print(g['name'])
        meetup.get_upcoming_meetups_for_group(g['urlname'])
