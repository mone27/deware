# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# author Simone Massaro
# date 14/4/17
"""driver that reads from serial port
    and sends data on zmq pub socket"""
from settings import SerialInput as setg
import time
import serial
import zmq
        
# open serial port
SerPort = serial.Serial(setg.SerialPort)

# zmq inizialization
ctx = zmq.Context.instance()
PubSock = ctx.socket(zmq.PUB)
PubSock.bind("tcp://127.0.0.1:%s" %setg.PubPort)
while True:
    data = ''
    for c in SerPort.readline():
        data += (chr(c))
    data = data.split(',')
    print(data)
    if data[0] == 'OK':
        print('humidity:',data[1])
        print('temperature:',data[2])
        PubSock.send_string("hum {}, temp {}".format(data[1], data[2]))
    else:
        # raise error to implement
        pass
    time.sleep(2)
