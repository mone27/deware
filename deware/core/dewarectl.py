#! /usr/bin/env python3
"""reads json from deware socket and prints it with avg on console.
The purpose of this script is providing a simple interface that could replace Qt gui for deware"""
import zmq
import os
from deware.core import settings as setg

count = 0
sum_data = {"temp":0, "hum":0, "co2":0} # second copy/paste :(

ctx = zmq.Context.instance()
sub_socket = ctx.socket(zmq.SUB)
sub_socket.setsockopt_string(zmq.SUBSCRIBE, "")
sub_socket.connect(f"tcp://127.0.0.1:{setg.pub_port}")

while True:
    data = sub_socket.recv_json()
    count += 1
    for key in data:  # not he most elegant and pythonic way
        if key!="time": sum_data[key] += data[key]
    for key in data:
        print(key + ": "+ str(data[key]))
    for key in sum_data:
        print(key + " avg: "+ str(sum_data[key]/count))
    os.system("clear")

