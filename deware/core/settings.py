# -*- coding: utf-8 -*-
from  os import environ
from deware.core.utilis import serial_ports
pub_port = 7001
serial_port = environ.get("DEWARE_SERIAL_DEVICE", serial_ports()[0] )
class SerialInput():
#   serial device must be set as a udev rule ... to fix in future


    Random = True
class Db():
    dbFile = '../prova.sqlite'
    time = 20


import sys
import glob
import serial
