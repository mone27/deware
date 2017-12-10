# -*- coding: utf-8 -*-
from  os import environ
<<<<<<< HEAD
pub_port = 7001
serial_port = environ.get("DEWARE_SERIAL_DEVICE", "/dev/arduino_uno")
class SerialInput():
#   serial device must be set as a udev rule ... to fix in future


=======
class SerialInput():
    SerialPort = environ.get("DEWARE_SERIAL_DEVICE", "/dev/arduino_uno")
    PubPort = 7001
>>>>>>> 446806a991660d50d47a51e93ef5e4f31fb77966
    Random = True
class Db():
    dbFile = '../prova.sqlite'
    time = 20
