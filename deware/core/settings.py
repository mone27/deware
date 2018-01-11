# -*- coding: utf-8 -*-
from  os import environ
import os
from . utilis import serial_ports
import logging

pub_port = 7001
scanned_serial_port = serial_ports()

serial_port = environ.get("DEWARE_SERIAL_DEVICE", scanned_serial_port)


db_file = os.path.abspath(os.getcwd())+"/prova.sqlite"

time = 16

log_file = "log.txt"
log_to_console = True
log_level = logging.INFO
