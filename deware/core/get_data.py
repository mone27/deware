# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# author Simone Massaro
# date 14/4/17
"""driver that reads from serial port
    and sends data on zmq pub socket"""
# %cd deware/core
from multiprocessing import Process
import settings as setg
import time
import serial
import zmq
import json
import logging
from utilis import OutOfRangeError
import time
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class sensors_read(Process):
    def __init__(self):
        Process.__init__(self)
        log.info("starting sensor reads")
        try:
            self.ser_port = serial.Serial(setg.serial_port)
        except serial.SerialException as msg:
            warning(msg)
        # zmq inizialization
        self.ctx = zmq.Context.instance()
        self.pub_socket = self.ctx.socket(zmq.PUB)
        self.pub_socket.bind(f"tcp://127.0.0.1:{setg.pub_port}")
        self.serial_exception_count = 0

    def run(self):

        while True:
            try:
                data = self.ser_port.readline().decode()
                debug(data)
                # must perform checks on data!!
                data_dict = json.loads(data)
                debug(data_dict)
                if not data_dict["temp"] < -50 and data_dict["temp"] > 150:
                    raise OutOfRangeError("temp",data_dict["temp"])
                    #warning(f"temp out of range:{data_dict['temp']}")

            except serial.SerialException as msg:
                #raise an exception if serial port does not work for too long
                if self.serial_exception_count > 10 :
                    log.error("serial error: "+ msg +" raising exception")
                    raise
                log.warning(msg)
                self.serial_exception_count += 1
                time.sleep(3)
            except json.JSONDecodeError as msg:
                log.warning(f"input data '{data}' is not a valid json")
            except OutOfRangeError as msg:
                log.warning(msg)
            else:
                self.pub_socket.send_string(data)
                log.debug("zmq socket sent data: " + data)

        # open serial port # just another stupid comment!!!!






#        while True:
            #try:

# this is kept for hystorical reason
#            data = ''
#            for c in SerPort.readlin-
#            if data[0] == 'OK':
#                print('humidity:',data[1])
#                print('temperature:',data[2])
#                PubSock.send_string("hum {}, temp {}".format(data[1], data[2]))
#            else:
#                # raise error to implement
#                pass
             #time.sleep(2)

if __name__ == '__main__':
    proc = sensors_read()
    proc.start()
