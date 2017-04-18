#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:57:08 2017

@author: simone
"""
from settings import Db as setg
from sqlalchemy_models import Record

from datetime import datetime
from decimal import Decimal

import zmq
ctx = zmq.Context.instance()
dataSock = ctx.socket(zmq.SUB)
dataSock.setsockopt_string(zmq.SUBSCRIBE, "")
dataSock.connect("tcp://127.0.0.1:7001")
dataPoll = zmq.Poller()
dataPoll.register(dataSock, zmq.POLLIN)


from sqlalchemy import create_engine
engine = create_engine('sqlite:///%s'%setg.dbFile)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()



while True:
    socks = dict(dataPoll.poll())
    if dataSock in socks and socks[dataSock] == zmq.POLLIN:
        data = dataSock.recv_string()
        data = data.split(',')
        print(data)
        temp = Decimal(data[0].split()[1])
        hum = Decimal(data[1].split()[1])
        record = Record(time = datetime.utcnow(), temp=temp, hum=hum)
        session.add(record)
        session.commit()
