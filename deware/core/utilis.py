import sys
import glob
import serial
import json
from datetime import datetime
import random
import time

class OutOfRangeError(Exception):
    def __init__(self, name="sensor reading", value=0):
        self.name = name
        self.value = value
    def __repr__(self):
        return (f"the reading of {self.name} is out of range, "
                f"read value is : {self.value}")
    def __str__(self):
        return (f"the reading of {self.name} is out of range, "
                f"read value is : {self.value}")


def get_random_data():  # may be in external file not a very good way for testing  idea:spawn a thread from main
    time.sleep(4)
    data = dict(time=datetime.utcnow().strftime('%H:%M:%S %d/%m/%Y'),
                temp=random.randint(-20, 50), hum=random.randint(0, 95), co2=random.randint(0, 20000))
    return json.dumps(data).encode()

def serial_ports():
    #patched from a verison found on stack overflow may be refacorest
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    if len(result) == 0:
        return "loop://"
    else:
        return result[0]
