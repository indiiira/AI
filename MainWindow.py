import sqlite3

from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QGraphicsPixmapItem, QGraphicsScene, QMessageBox

from MyDialog import MyDialog
from PythonFile.uibd import Ui_Dialog
from PythonFile.uisppr import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

# Form implementation generated from reading ui file 'C:/Users/Индира/PycharmProjects/AI/UI/uisppr.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.dialog = MyDialog(self)
        self.loadMaterial()
        self.ui.comboBox.currentIndexChanged.connect(self.comboBoxChanged)  # Связываем сигнал с слотом
        self.ui.pushButton_2.clicked.connect(self.dialog.open)
        self.dialog.dataChanged.connect(self.loadMaterial)
        self.ui.actionOpen.triggered.connect(self.openImage)

    def loadMaterial(self):
        self.ui.comboBox.clear()
        conn = sqlite3.connect('C:/Users/Индира/PycharmProjects/AI/My_DB.db')
        cur = conn.cursor()
        # Выполнение запроса для получения списка материалов
        cur.execute("SELECT name FROM Materials")
        rows = cur.fetchall()

        # Добавление материалов в comboBox
        for row in rows:
            self.ui.comboBox.addItem(row[0])

        conn.close()


    def comboBoxChanged(self, index):
        # Этот метод вызывается при изменении выбора в comboBox
        material_name = self.ui.comboBox.currentText()

        conn = sqlite3.connect('C:/Users/Индира/PycharmProjects/AI/My_DB.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Materials WHERE name = ?", (material_name,))
        row = cur.fetchone()
        conn.close()

        if row:
            # Обновляем QLabel нормативными значениями для выбранного материала
            # Предполагается, что интересующие нас данные находятся в конкретных столбцах row[x]
            self.ui.label_12.setText(str(row[2]))
            self.ui.label_14.setText(str(row[3]))
            self.ui.label_16.setText(str(row[4]))
            self.ui.label_18.setText(str(row[5]))

    def open_edit_dialog(self):
        self.edit_dialog = Ui_Dialog(self)
        self.edit_dialog.show()

    def openImage(self):
        try:
            imagePath, _ = QFileDialog.getOpenFileName(self, "Open Image File", "",
                                                       "Images (*.png *.xpm *.jpg *.bmp *.gif)")
            if imagePath:
                pixmap = QPixmap(imagePath)
                if pixmap.isNull():
                    raise Exception("Не удалось загрузить изображение из файла.")
                scene = QGraphicsScene()
                item = QGraphicsPixmapItem(pixmap)
                scene.addItem(item)
                # Устанавливаем сцену для graphicsView вашего интерфейса пользователя
                self.ui.graphicsView.setScene(scene)
                # Подгоняем изображение под размер graphicsView с сохранением пропорций
                self.ui.graphicsView.fitInView(item, QtCore.Qt.KeepAspectRatio)
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при загрузке изображения: {str(e)}")
            print(f"Ошибка: {str(e)}")  # Отладочное сообщение в консоль