#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:57:08 2017

@author: simone
"""
#%cd deware/core
import settings  as setg
from models import Record
import json

from datetime import datetime
from decimal import Decimal
from multiprocessing import Process

import zmq
from zmq.eventloop import ioloop, zmqstream
from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker

import logging
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
class db_manager(Process):
    def __init__(self):
        Process.__init__(self)
        print(" anche io ci sono!!!!!")
    def on_data(msg, f_run=True):
        if f_run == True :
            f_run = False
            db_manager.on_data.lastCommit = datetime.utcnow()
            db_manager.on_data.temp = 0
            db_manager.on_data.hum = 0
            db_manager.on_data.co2 = 0
            db_manager.on_data.count = 1

            engine = create_engine(f"sqlite:///{setg.db_file}")
            Base.metadata.create_all(engine)
            Session = sessionmaker(bind=engine)
            db_manager.on_data.session = Session()

        log.debug(f"received {msg}")
        data_dict = json.loads(msg)
        temp = float(data_dict["temp"])
        hum = float(data_dict["hum"])
        co2 = int(data_dict["co2"])

        # db_manager.on_data.temp += temp
        # db_manager.on_data.hum += hum
        # db_manager.on_data.co2 += co2
        # db_manager.on_data.count += 1
        #if (datetime.utcnow() - db_manager.on_data.lastCommit).seconds >= setg.time :
        record = Record(time = datetime.utcnow(),
        #time = datetime.fromtimestamp(data_dict["time"]),
                        temp = Decimal(temp ),
                        hum = Decimal(hum),
                        co2 = co2
                        )
                        # temp = Decimal(db_manager.on_data.temp / db_manager.on_data.count),
                        # hum = Decimal(db_manager.on_data.hum / db_manager.on_data.count),
                        # co2 = db_manager.on_data.co2 / db_manager.on_data.count
                        # )
        log.debug(record)
        db_manager.on_data.session.add(record)
        db_manager.on_data.session.commit()
        db_manager.on_data.lastCommit = datetime.utcnow()
        db_manager.on_data.temp = 0
        db_manager.on_data.hum = 0
        db_manager.on_data.count = 1

    def run(self):
        ioloop.install()
        ctx = zmq.Context.instance()
        dataSock = ctx.socket(zmq.SUB)
        dataSock.setsockopt_string(zmq.SUBSCRIBE, "")
        dataSock.connect(f"tcp://127.0.0.1:{setg.pub_port}")
        #dataPoll = zmq.Poller()
        #dataPoll.register(dataSock, zmq.POLLIN)
        dataStream = zmqstream.ZMQStream(dataSock)
        dataStream.on_recv(db_manager.on_data)
        log.info("started db_manager")
        ioloop.IOLoop.instance().start()



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
