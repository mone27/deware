# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# author Simone Massaro
# date 14/4/17
"""driver that reads from serial port
    and sends data on zmq pub socket"""
# %cd deware/core
from threading import Thread
import serial
import zmq
import json
import logging
import time

from deware.core import settings as setg
from deware.core.utilis import OutOfRangeError
from deware.core.utilis import get_random_data

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


class SensorRead(Thread):
    def __init__(self):
        Thread.__init__(self)
        log.info("starting sensor reads")
        try:
            self.ser_port = serial.serial_for_url(setg.serial_port)
            if setg.serial_port=="loop://":
                log.warning("no serial port found! using loop device "
                            "if not running tests please check wiring.")
                self.ser_port.readline = get_random_data

        except serial.SerialException as msg:
            log.warning(msg)
        # zmq inizialization
        self.ctx = zmq.Context.instance()
        self.pub_socket = self.ctx.socket(zmq.PUB)
        self.pub_socket.bind(f"tcp://127.0.0.1:{setg.pub_port}")
        self.serial_exception_count = 0

    def run(self):
        while True:
            try:
                data = self.ser_port.readline().decode()
                log.debug(data)
                # must perform checks on data!!
                data_dict = json.loads(data)
                log.debug(data_dict)

                # check whether the data is in valid range to avoid recording outlier
                if not data_dict["temp"] < -50 and data_dict["temp"] > 150:
                    raise OutOfRangeError("temp",data_dict["temp"])
                if data_dict["hum"]<0 and data_dict["hum"] > 100:
                    raise OutOfRangeError("hum", data_dict["hum"])
                if data_dict["co2"] <0:
                    raise OutOfRangeError("co2", data_dict["co2"])

            except serial.SerialException as msg:
                # raise an exception if serial port does not work for too long
                if self.serial_exception_count > 10 :
                    log.error(f"serial error: {msg} raising exception")
                    raise
                log.warning(msg)
                self.serial_exception_count += 1
                time.sleep(3)
            except json.JSONDecodeError as msg:
                log.warning(f"input data '{data}' is not a valid json")
            except OutOfRangeError as msg:
                log.warning(msg)
            else:
                self.pub_socket.send_string(data)
                log.debug("zmq socket sent data: " + data)
                # db_manager.on_data(data)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    proc = SensorRead()
    proc.start()
