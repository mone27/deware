#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 15:57:08 2017

@author: simone

read a json from zmq port and saves it to a sqlalchemy sb
"""
from threading import Thread
import zmq
import logging

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decimal import Decimal

from deware.core import settings as setg
from deware.core.models import Base, Record


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class DbManager(Thread):

    def __init__(self):
        Thread.__init__(self)
        # connect to zmq pub socket
        ctx = zmq.Context.instance()
        self.sub_socket = ctx.socket(zmq.SUB)
        self.sub_socket.setsockopt_string(zmq.SUBSCRIBE, "")
        self.sub_socket.connect(f"tcp://127.0.0.1:{setg.pub_port}")
        # init databases and sqlalchemy session
        engine = create_engine(f"sqlite:///{setg.db_file}")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def run(self):
        log.info("started db manager")
        sum_data = {"temp":0, "hum":0, "co2":0} # this will crash with arduino!!! since it sends also tim
        avg_data = {}
        count = 0
        last_commit = datetime.utcnow()
        while True:
            data = self.sub_socket.recv_json()
            count +=1
            for key in data:
                if key != "time": sum_data[key] += data[key]
                # log.debug(f"key :{key} value: {data[key]}") #could be removed
            log.debug('sum_data :'+str(sum_data))
            if (datetime.utcnow() - last_commit).seconds >= setg.time:
                # calculate avg
                for key in sum_data:
                    avg_data[key]= round(Decimal(sum_data[key])/count,2)
                    # todo co2 with 2 zeros after point could be imporved low importance
                count = 0
                sum_data = {"temp":0, "hum":0, "co2":0}
                last_commit = datetime.utcnow()
                # need to add time to avg dict
                log.debug("avg_data :"+str(avg_data))
                record_commit = Record(
                    time = datetime.strptime(data["time"], '%H:%M:%S %d/%m/%Y'),
                    temp = avg_data["temp"],
                    hum = avg_data["hum"],
                    co2 = avg_data["co2"])
                self.session.add(record_commit)
                self.session.commit()
                log.info("added to database record:"+repr(record_commit))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    proc = DbManager()
    proc.start()


