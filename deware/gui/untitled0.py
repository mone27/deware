#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 18:22:53 2017

@author: simone
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from First import Ui_myfirstgui
 
class MyFirstGuiProgram(Ui_myfirstgui):
	def __init__(self, dialog):
		Ui_myfirstgui.__init__(self)
		self.setupUi(dialog)
 
		# Connect "add" button with a custom function (addInputTextToListbox)
		self.addBtn.clicked.connect(self.addInputTextToListbox)
 
	def addInputTextToListbox(self):
		txt = self.myTextInput.text()
		self.listWidget.addItem(txt)
 
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()
 
	prog = MyFirstGuiProgram(dialog)
 
	dialog.show()
	sys.exit(app.exec_())