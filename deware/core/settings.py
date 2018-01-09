# -*- coding: utf-8 -*-
from  os import environ
import os
from . utilis import serial_ports

pub_port = 7001
scanned_serial_port = '/dev/zero'
try:
    scanned_serial_port = serial_ports()[0]
except IndexError:
    #means no port found todo stop doing this awful thing
    scanned_serial_port = "loop://"
serial_port = environ.get("DEWARE_SERIAL_DEVICE", scanned_serial_port)


db_file = os.path.abspath(os.getcwd())+"/prova.sqlite"
print(db_file)
time = 16

log_file = "log.txt"
log_to_console = True
