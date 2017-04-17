# -*- coding: utf-8 -*-
#tring pyqt5
# update me!!
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from MainWindow_prova import Ui_MainWindow
app = QApplication(sys.argv)

def ciao_mondo():
    print('ciao mondo')
window = QMainWindow()
ui2 = loadUi('gui.ui')
ui2.show()
ui = Ui_MainWindow
ui.setupUi(window)
#ui.actionCiao_mondo.clicked.connect(ciao_mondo)
window.show()
#w.resize(250, 150)
#w.move(0, 0)
#w.setWindowTitle('Simple')
#w.show()

sys.exit(app.exec_())