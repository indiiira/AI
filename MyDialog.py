import sqlite3

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QTableWidgetItem

from PythonFile.uibd import Ui_Dialog






class MyDialog(QDialog):
    dataChanged = pyqtSignal()
    def __init__(self, root, **kwargs):
        super(MyDialog, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.load_data_from_db()
        self.ui.pushButton.clicked.connect(self.push_button_add_click)
        self.ui.pushButton_2.clicked.connect(self.push_button_delete_click)
        self.load_data_from_db()
        self.ui.buttonBox.clicked.connect(self.closeDialog)
    def push_button_add_click(self):
        material_name = self.ui.lineEdit.text()
        material_area = self.ui.lineEdit_2.text()
        material_area_std = self.ui.lineEdit_3.text()
        material_porous = self.ui.lineEdit_4.text()
        material_porous_std = self.ui.lineEdit_6.text()  # предположим, что это должно быть lineEdit_5
        data = [material_name, material_area, material_area_std, material_porous, material_porous_std]
        flag = all(m != '' for m in data)  # Используем all() для проверки, что все значения заполнены
        if flag:
            try:
                material_area = float(material_area)
                material_area_std = float(material_area_std)
                material_porous = float(material_porous)
                material_porous_std = float(material_porous_std)
                connect = sqlite3.connect('C:/Users/Индира/PycharmProjects/AI/My_DB.db')  # Убедитесь, что self.db_name правильно определено
                crsr = connect.cursor()

                crsr.execute(
                    """INSERT INTO Materials(NAME, PORE_AREA_MEAN, PORE_AREA_STD, POROUS_MEAN, POROUS_STD) VALUES (?,?,?,?,?)""",
                    (material_name, material_area, material_area_std, material_porous, material_porous_std))
                connect.commit()
                connect.close()
                self.load_data_from_db()
                self.ui.lineEdit.clear()
                self.ui.lineEdit_2.clear()
                self.ui.lineEdit_3.clear()
                self.ui.lineEdit_4.clear()
                self.ui.lineEdit_6.clear()

            except Exception as e:
                print(e)

    def load_data_from_db(self):
        # Подключаемся к базе данных
        conn = sqlite3.connect('C:/Users/Индира/PycharmProjects/AI/My_DB.db')
        cur = conn.cursor()
        self.dataChanged.emit()
        # Выполняем запрос SELECT для получения данных
        cur.execute("SELECT * FROM Materials")
        rows = cur.fetchall()

        # Устанавливаем количество строк в tableWidget в соответствии с количеством записей
        self.ui.tableWidget.setRowCount(len(rows))

        # Вставляем данные в tableWidget
        for row_index, row_data in enumerate(rows):
            for column_index, data in enumerate(row_data):
                self.ui.tableWidget.setItem(row_index, column_index, QTableWidgetItem(str(data)))

        conn.close()

    def push_button_delete_click(self):
            index = self.ui.lineEdit_7.text()

            index = int(index)

            connect = sqlite3.connect('C:/Users/Индира/PycharmProjects/AI/My_DB.db')
            crsr = connect.cursor()

            crsr.execute('DELETE FROM Materials WHERE ID=?', (index,))
            connect.commit()
            connect.close()
            self.load_data_from_db()



            self.ui.lineEdit_7.clear()

    def closeDialog(self):
        # Эта функция будет вызвана при нажатии на 'pushButtonClose'
        # Закрывает текущее диалоговое окно
        self.close()




