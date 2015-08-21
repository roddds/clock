#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
from sqlalchemy import types, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class WorkDay(Base):
    __tablename__ = 'workday'
    id = Column(Integer, primary_key=True)
    day = Column(types.Date())
    am_enter = Column(types.DateTime())
    am_leave = Column(types.DateTime())
    pm_enter = Column(types.DateTime())
    pm_leave = Column(types.DateTime())

    def print_times(self):
        print "enter:", self.am_enter or ''
        print "lunch:", self.am_leave or ''
        print "back: ", self.pm_enter or ''
        print "leave:", self.pm_leave or ''
        print
        now = datetime.datetime.now()
        workday = now - self.am_enter
        if self.am_leave and self.pm_enter:
            lunch = self.pm_enter - self.am_leave
            workday -= lunch
        print 'worked hours:', workday
        print 'time left:', datetime.timedelta(hours=8) - workday

engine = create_engine('sqlite:///workday.db')

Base.metadata.create_all(engine)
