#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
import time
from session import session
from models import WorkDay
from sqlalchemy.orm.exc import NoResultFound


EVENTS = ('enter', 'lunch', 'back', 'leave')


def commit(obj):
    session.add(obj)
    session.commit()


def get_today():
    today = session.query(WorkDay).filter(WorkDay.day==datetime.date.today())

    try:
        return today.one()
    except NoResultFound:
        commit(WorkDay(day=datetime.date.today()))
        return get_today()


def insert_event(event):
    events = {
        'enter': 'am_enter',
        'lunch': 'am_leave',
        'back': 'pm_enter',
        'leave': 'pm_leave',
    }
    today = get_today()
    setattr(today, events[event], datetime.datetime.now())
    commit(today)


def format_time(time):
    return time.strftime('%H:%M:%S')

def format_timedelta(td):
    return str(td).split('.')[0]


def print_times(day):
    print "enter:", format_time(day.am_enter) if day.am_enter else ''
    print "lunch:", format_time(day.am_leave) if day.am_leave else ''
    print "back: ", format_time(day.pm_enter) if day.pm_enter else ''
    print "leave:", format_time(day.pm_leave) if day.pm_leave else ''
    print
    if not day.am_enter:
        print 'no clock times for today'
        return

    now = datetime.datetime.now()
    workday = now - day.am_enter
    if day.am_leave and day.pm_enter:
        lunch = day.pm_enter - day.am_leave
        workday -= lunch
    print 'worked time:', format_timedelta(workday)
    print 'time left:', format_timedelta(datetime.timedelta(hours=8) - workday)

    return workday


if __name__ == '__main__':
    today = get_today()
    wd = print_times(today)

    if len(sys.argv) > 1 and sys.argv[1] in EVENTS:
        insert_event(sys.argv[1])

    elif wd and 'watch' in sys.argv:
        wd = datetime.timedelta(hours=8) - wd
        try:
            while True:
                timestr = format_timedelta(wd)
                sys.stdout.write(timestr + '\r')
                sys.stdout.flush()
                time.sleep(1)
                wd += datetime.timedelta(seconds=-1)
        except KeyboardInterrupt:
            sys.exit()
