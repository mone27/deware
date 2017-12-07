# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# author Simone Massaro
# date 14/4/17
"""driver that reads from serial port
    and sends data on zmq pub socket"""
from multiprocessing import Process
import deware.core.settings as setg
dir(setg)
import time
import serial
import zmq
import json
from logging import info, debug, warning

class sensors_read(Process):
    def __init__(self):
        Process.__init__(self)
        try:
            self.ser_port = serial.Serial(setg.serial_port)
        except serial.SerialException as msg:
            warning(msg)
        # zmq inizialization
        self.ctx = zmq.Context.instance()
        self.pub_socket = self.ctx.socket(zmq.PUB)
        self.pub_socket.bind(f"tcp://127.0.0.1:{setg.pub_port}")
    def run(self):
        while True:
            try:
                data = self.ser_port.readline().deconde()

            except serial.SerialException as msg:
                warning(msg)

        # open serial port # just another stupid comment!!!!






#        while True:
            #try:

# this is kept for hystorical reason
#            data = ''
#            for c in SerPort.readline():
#                data += (chr(c))
#            data = data.split(',')
#            print(data)
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
