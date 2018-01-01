# -*- coding: utf-8 -*-
from  os import environ
from . utilis import serial_ports
pub_port = 7002
serial_port = environ.get("DEWARE_SERIAL_DEVICE", serial_ports()[0])

db_file = "prova.sqlite"
time = 2
