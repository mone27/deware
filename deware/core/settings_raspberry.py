# -*- coding: utf-8 -*-
from  os import environ
import os
from . utilis import serial_ports
import logging

pub_port = 7001

scanned_serial_port = serial_ports()
serial_port = environ.get("DEWARE_SERIAL_DEVICE", scanned_serial_port)


db_file = "/home/pi/deware_data/db.sqlite" # should do this using sed # cominti? todo be less lazy

time = 120

log_file = "/home/pi/deware_data/logs.txt"
log_to_console = False
log_level = logging.INFO
