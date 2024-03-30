import sqlite3
import sys
from PyQt5 import QtWidgets
from uibd1 import Ui_Dialog  # импорт нашего сгенерированного файла
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QTableWidgetItem, QTableWidget, QVBoxLayout, QWidget, \
    QDialog
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class mywindow(Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.load_data_from_db()
    def load_data_from_db(self):
        conn = sqlite3.connect('C:/Users/Индира/PycharmProjects/AI/My_DB.db')
        cur = conn.cursor()

        cur.execute("SELECT * FROM Materials")
        rows = cur.fetchall()

        self.ui.tableWidget.setRowCount(len(rows))
        self.ui.tableWidget.setColumnCount(len(rows[0]))
        for row_index, row_data in enumerate(rows):
                for column_index, data in enumerate(row_data):
                    self.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))
        conn.close()


app = QApplication(sys.argv)
window = mywindow()
window.show()
sys.exit(app.exec_())