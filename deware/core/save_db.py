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
from multiprocessing import Process
import zmq
from zmq.eventloop import ioloop, zmqstream
from sqlalchemy import create_engine
from sqlalchemy_models import Base
from sqlalchemy.orm import sessionmaker
class db_manager(Process):
    def __init__(self):
        Process.__init__(self)
    def run(self):

        def onData(msg):
            data = ''
            for c in msg[0]:
                data += chr(c)
            data = data.split(',')
            print(data)
            temp = float(data[1].split()[1])
            hum = float(data[0].split()[1])
            onData.temp += temp
            onData.hum += hum
            onData.count += 1
            if (datetime.utcnow() - onData.lastCommit).seconds >= setg.time :
                record = Record(time = datetime.utcnow(),\
                                temp = Decimal(onData.temp / onData.count)\
                                , hum = Decimal(onData.hum / onData.count))
                print(record)
                session.add(record)
                session.commit()
                onData.lastCommit = datetime.utcnow()
                onData.temp = 0
                onData.hum = 0
                onData.count = 0
        # for inizialize time
        onData.lastCommit = datetime.utcnow()
        onData.temp = 0
        onData.hum = 0
        onData.count = 0


        engine = create_engine('sqlite:///%s'%setg.dbFile)

        Base.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()


        #inizialize zmq
        ioloop.install()
        ctx = zmq.Context.instance()
        dataSock = ctx.socket(zmq.SUB)
        dataSock.setsockopt_string(zmq.SUBSCRIBE, "")
        dataSock.connect("tcp://127.0.0.1:7001")
        #dataPoll = zmq.Poller()
        #dataPoll.register(dataSock, zmq.POLLIN)
        dataStream = zmqstream.ZMQStream(dataSock)
        dataStream.on_recv(onData)
        try:
            ioloop.IOLoop.instance().start()
        except:
            pass

if __name__ == '__main__':
    proc = db_manager()
    proc.start()

#while True:
#    socks = dict(dataPoll.poll())
#    if dataSock in socks and socks[dataSock] == zmq.POLLIN:
#        data = dataSock.recv_string()
#        data = data.split(',')
#        print(data)
#        temp = Decimal(data[0].split()[1])
#        hum = Decimal(data[1].split()[1])
#        record = Record(time = datetime.utcnow(), temp=temp, hum=hum)
#        session.add(record)
#        session.commit()
