# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import WorkDay, Base

engine = create_engine('sqlite:///workday.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)

session = DBSession()

