import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import QApplication
from pyqt5_plugins.examplebutton import QtWidgets

app = QtWidgets.QApplication([])
win= uic.loadUi("C:/Users/Индира/PycharmProjects/AI/UI/uibd.ui")


win.show()
sys.exit(app.exec())