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
        self.dataPort = self.ctx.socket(zmq.SUB)
        self.dataPort.setsockopt_string(zmq.SUBSCRIBE, "")
        self.dataPort.connect("tcp://127.0.0.1:7001")
        
        self.timerUpadateValues = QtCore.QTimer()
        self.timerUpadateValues.timeout.connect(self.updateValues)
        self.timerUpadateValues.start(1000)
    def updateValues(self):
        data = self.dataPort.recv_string()
        data = data.split(',')
        print(data)
        self.humidity_lab.setText(data[0].split()[1])
        self.temp_lab.setText(data[1].split()[1])
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = homeGui(Dialog)
Dialog.show()
sys.exit(app.exec_())
