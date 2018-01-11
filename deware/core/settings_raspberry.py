# -*- coding: utf-8 -*-
from  os import environ
import os
from . utilis import serial_ports
import logging

pub_port = 7001
scanned_serial_port = '/dev/zero'
try:
    scanned_serial_port = serial_ports()[0]
except IndexError:
    #means no port found todo stop doing this awful thing
    scanned_serial_port = "loop://"
serial_port = environ.get("DEWARE_SERIAL_DEVICE", scanned_serial_port)


db_file = "/home/pi/deware_data/db.sqlite" # should do this using sed # cominti? todo be less lazy
print(db_file)
time = 16

log_file = "/home/pi/deware_data/logs.txt"
log_to_console = False
log_level = logging.INFO
