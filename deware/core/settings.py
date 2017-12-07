# -*- coding: utf-8 -*-
from  os import environ
class SerialInput():
    SerialPort = environ.get("DEWARE_SERIAL_DEVICE", "/dev/arduino_uno")
    PubPort = 7001
    Random = True
class Db():
    dbFile = '../prova.sqlite'
    time = 20
