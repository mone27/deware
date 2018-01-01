# -*- coding: utf-8 -*-
from  os import environ
from . utilis import serial_ports
pub_port = 7002
scanned_serial_port = '/dev/zero'
try:
    scanned_serial_port = serial_ports()[0]
except IndexError:
    #means no port found
    pass
serial_port = environ.get("DEWARE_SERIAL_DEVICE", scanned_serial_port)

db_file = "prova.sqlite"
time = 2
