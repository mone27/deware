#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:10:59 2017

@author: simone
"""


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Float, DateTime, Integer
class Record(Base):
    __tablename__ = 'records'

    time = Column(DateTime, primary_key=True)
    temp = Column(Float( asdecimal = True ))
    hum = Column(Float( asdecimal = True ))
    co2 = Column(Float( asdecimal = True ))
    def __repr__(self):
        return (f"<Record: date='{self.time}', temp='{self.temp}'"
                f", hum='{self.hum}, co2='{self.co2}'>")
    
    def __str__(self):
        return f"'{self.time}', '{self.temp}', '{self.hum}', '{self.co2}'"
