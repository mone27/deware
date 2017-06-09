# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home1.0.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 480)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 101, 31))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 90, 131, 41))
        self.label.setObjectName("label")
        self.temp_lab = QtWidgets.QLabel(Dialog)
        self.temp_lab.setGeometry(QtCore.QRect(210, 100, 81, 24))
        self.temp_lab.setText("")
        self.temp_lab.setObjectName("temp_lab")
        self.humidity_lab = QtWidgets.QLabel(Dialog)
        self.humidity_lab.setGeometry(QtCore.QRect(210, 140, 81, 24))
        self.humidity_lab.setText("")
        self.humidity_lab.setObjectName("humidity_lab")
        self.close_butt = QtWidgets.QPushButton(Dialog)
        self.close_butt.setGeometry(QtCore.QRect(460, 230, 116, 32))
        self.close_butt.setObjectName("close_butt")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "umidità:"))
        self.label.setText(_translate("Dialog", "temperatura:"))
        self.close_butt.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

