#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
from session import session
from models import WorkDay
from sqlalchemy.orm.exc import NoResultFound

'''
    events: enter, lunch, back, leave
'''

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

if __name__ == '__main__':
    today = get_today()
    if len(sys.argv) == 1:
        today.print_times()
    else:
        insert_event(sys.argv[1])
        today.print_times()
