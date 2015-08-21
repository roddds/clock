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

engine = create_engine('sqlite:///workday.db')

Base.metadata.create_all(engine)
