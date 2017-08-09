#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:10:59 2017

@author: simone
"""


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Float, DateTime
class Record(Base):
    __tablename__ = 'records'
    
    time = Column(DateTime, primary_key=True)
    temp = Column(Float( asdecimal = True ))
    hum = Column(Float( asdecimal = True ))
    def prova_str(self):
        print(self.time)
    def __repr__(self):
        return "<Record: date='%s', temp='%s', hum='%s'>"\
        %(self.time, self.temp, self.hum)
    def __str__(self):
        return "'%s, '%s, '%s'>"\
        %(self.time, str(self.temp), str(self.hum))
        