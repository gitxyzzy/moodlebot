from typing import NamedTuple

import requests
from bs4 import BeautifulSoup

from credentials_manager import get_cookies, set_cookies


def get_sesskey():
    url = 'https://courses.iris.nitk.ac.in/my/'
    is_redirect = True

    html = ''
    while is_redirect:
        r = requests.get(url, cookies=get_cookies(), allow_redirects=False)

        set_cookies(r.cookies)

        is_redirect = r.is_redirect
        if is_redirect:
            url = r.headers.get('Location')
        else:
            html = r.text

    soup = BeautifulSoup(html, features='html.parser')
    input_el = soup.find('input', attrs={'type': 'hidden', 'name': 'sesskey'})
    return input_el['value']


class MoodleCourse(NamedTuple):
    full_name: str
    short_name: str


class MoodleEvent(NamedTuple):
    name: str
    description: str
    time_sort: float
    url: str
    course: MoodleCourse


def upcoming_events() -> list[MoodleEvent]:
    sesskey = get_sesskey()
    payload = [
        {
            'index': 0,
            'methodname': 'core_calendar_get_calendar_upcoming_view',
            'args': {
                'courseid': 1,
                'categoryid': 0
            }
        }
    ]

    url = f'https://courses.iris.nitk.ac.in/lib/ajax/service.php?sesskey={sesskey}&info=core_calendar_get_calendar_upcoming_view'
    r = requests.post(url, json=payload, cookies=get_cookies())

    moodle_events: list[MoodleEvent] = []
    data = r.json()[0]
    for event in data['data']['events']:
        moodle_events.append(MoodleEvent(
            name=event['name'],
            description=' '.join(BeautifulSoup(event['description'], features='html.parser').get_text().split()),
            time_sort=event['timesort'],
            url=event['url'],
            course=MoodleCourse(
                full_name=event['course']['fullname'],
                short_name=event['course']['shortname'],
            ),
        ))

    return moodle_events
