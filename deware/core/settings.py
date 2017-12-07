# -*- coding: utf-8 -*-
from  os import environ
pub_port = 7001
serial_port = environ.get("DEWARE_SERIAL_DEVICE", "/dev/arduino_uno")
class SerialInput():
#   serial device must be set as a udev rule ... to fix in future


    Random = True
class Db():
    dbFile = '../prova.sqlite'
    time = 20
