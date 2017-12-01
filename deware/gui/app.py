# -*- coding: utf-8 -*-
import sys
from gui_home import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import zmq
class homeGui(Ui_Dialog):
    def __init__(self, dialog):
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)
        #connecting close button
        self.close_butt.clicked.connect(sys.exit)
        self.ctx = zmq.Context.instance()
        self.dataSock = self.ctx.socket(zmq.SUB)
        self.dataSock.setsockopt_string(zmq.SUBSCRIBE, "")
        self.dataSock.connect("tcp://127.0.0.1:7001")
        
        self.timerUpadateValues = QtCore.QTimer()
        self.timerUpadateValues.timeout.connect(self.updateValues)
        self.timerUpadateValues.start(2000)
        self.dataPoll = zmq.Poller()
        self.dataPoll.register(self.dataSock, zmq.POLLIN)
    def updateValues(self):
        print('before poll')
        socks = dict(self.dataPoll.poll(1000))
        print('after poll')
        if self.dataSock in socks and socks[self.dataSock] == zmq.POLLIN:
            data = self.dataSock.recv_string()
            data = data.split(',')
            print(data)
            self.humidity_lab.setText(data[0].split()[1])
            self.temp_lab.setText(data[1].split()[1])
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = homeGui(Dialog)
Dialog.show()
sys.exit(app.exec_())
