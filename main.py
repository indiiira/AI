import sys

# Form implementation generated from reading ui file 'C:/Users/Индира/PycharmProjects/AI/UI/uisppr.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtGui

from MainWindow import MainWindow
from PythonFile.uisppr import *

from PyQt5 import QtCore, QtGui, QtWidgets


app = QtWidgets.QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())