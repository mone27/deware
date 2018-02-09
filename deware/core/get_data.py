# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# author Simone Massaro
# date 14/4/17
"""driver that reads from serial port sent by arduino in json
    and sends data on zmq pub socket"""
from threading import Thread
import serial
import zmq
import json
import logging
import time

#import settings
from deware.core import settings as setg
from deware.core.utilis import OutOfRangeError
from deware.core.utilis import get_random_data

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class SensorRead(Thread):
    """
    a thread that reads data from a serial port
    check it's in valid range and sends the json on the zmq pub socket
    """
    def __init__(self):
        """initialaze serial port and zmq pub socket"""
        Thread.__init__(self)
        try:
            self.ser_port = serial.serial_for_url(setg.serial_port)
            if setg.serial_port=="loop://": # fix it! not best idea for testing device
                log.warning("no serial port found! using loop device "
                            "if not running tests please check wiring.")
                self.ser_port.readline = get_random_data

        except serial.SerialException as msg:
            log.warning(msg)
        # initialize zmq socket
        self.ctx = zmq.Context.instance()
        self.pub_socket = self.ctx.socket(zmq.PUB)
        self.pub_socket.bind(f"tcp://127.0.0.1:{setg.pub_port}")
        self.serial_exception_count = 0

    def run(self):
        """starts read loop"""
        log.info("starting sensor reads")
        while True:
            try:
                data = self.ser_port.readline().decode()  # better names at variable?
                log.debug(data)

                data_dict = json.loads(data)
                log.debug(data_dict)

                # check whether the data is in valid range to avoid recording outlier
                # maybe fixed values aren't the best TODO should be imported from settings
                if not data_dict["temp"] < -50 and data_dict["temp"] > 150:
                    raise OutOfRangeError("temp",data_dict["temp"])
                if data_dict["hum"]<0  and data_dict["hum"] > 100:
                    raise OutOfRangeError("hum", data_dict["hum"])
                if data_dict["co2"] <0:
                    raise OutOfRangeError("co2", data_dict["co2"])

            except serial.SerialException as msg:
                # raise an exception if serial port does not work for too long
                # it doesn't work as intended: change way to handle the problem may be restarting serial connection
                if self.serial_exception_count > 10 :
                    log.error(f"serial error: {msg} raising exception")
                    raise
                log.warning(msg)
                self.serial_exception_count += 1
                time.sleep(3)
            except json.JSONDecodeError as msg:
                # error can be generated when parsing serial data
                log.warning(f"input data '{data}' is not a valid json")
            except OutOfRangeError as msg:
                # what can trigger this?
                log.warning(msg)
            else:
                self.pub_socket.send_string(data)
                log.debug("zmq socket sent data: " + data)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    proc = SensorRead()
    proc.start()
