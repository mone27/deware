# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# author Simone Massaro
# date 14/4/17
"""driver that reads from serial port
    and sends data on zmq pub socket"""
from multiprocessing import Process
from settings import SerialInput as setg
import time
import serial
import zmq
class SerialInput(Process):
    def __init__(self):
        Process.__init__(self)
    def run(self):
        # open serial port # just another stupid comment!!!!
        SerPort = serial.Serial(setg.SerialPort)
        # zmq inizialization
        ctx = zmq.Context.instance()
        PubSock = ctx.socket(zmq.PUB)
        PubSock.bind(f"tcp://127.0.0.1:{setg.PubPort}")
        while True:
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
            time.sleep(2)

if __name__ == '__main__':
    proc = SerialInput()
    proc.start()
