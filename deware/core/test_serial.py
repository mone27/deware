import unittest
import os
import threading
import time
import random


from deware.core.get_data import SensorRead

class GetDataTestCase(unittest.TestCase):
    def send_test_data(self, serial):
        "sends random data in a valid range to a given serial port every two seconds "
        while True:
            serial.write('{ "temp": {}, "hum": {}, "co2": {} }'.format(
                random.randint(-20, 50), random.randint(0, 95), random.randint(0, 20000)).encode())
            time.sleep(2)
    def setUp(self):
        os.environ["DEWARE_SERIAL_DEVICE"] = "loop://" #set debug serial device
        random.seed(10)

        #
        # random_input_thread = threading.Thread(target=send_test_data, args=SensorRead.ser_port)
        # random_input_thread.start()
    def test_input(self):
        sensor_read = SensorRead()
        send_thread = threading.Thread(target=self.send_test_data, args=sensor_read.ser_port)
        send_thread.start()
        sensor_read.start()
        while True:
            time.sleep(100)





