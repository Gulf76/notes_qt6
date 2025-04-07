from PyQt6.QtWidgets import QDialogButtonBox

from ui.task import Ui_MainWindow
from ui.dia import Ui_Dialog
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog,QVBoxLayout
import sys
from datetime import datetime
from database_query import create_table, request_query, get_active_notes


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.add_list)
        self.pushButton_2.clicked.connect(self.del_task)
        self.pushButton_3.clicked.connect(self.change_task)
        result = get_active_notes()
        for text in result:
            self.listWidget.addItem(text[0])

    def add_list(self):
        text = self.lineEdit.text()
        self.listWidget.addItem(text)
        request_query(text, "Активна", datetime.now())

    def del_task(self):
        index = self.listWidget.currentRow()
        #text = self.listWidget.item(index)
        current_item = self.listWidget.currentItem()
        text = current_item.text()
        self.listWidget.takeItem(index)
        request_query(text, "Удалена", datetime.now())

    def change_task(self):
        d = Change()
        d.exec()


class Change(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.change)

    def change(self):
        self.buttonBox.accepted.connect(self.test_Ok)
        self.buttonBox.rejected.connect(self.reject)

    def test_Ok(self):
        txt = self.lineEdit.text()
        index = window.listWidget.currentRow()
        window.listWidget.takeItem(index)
        request_query(txt, "Редактирована", datetime.now())
        window.listWidget.insertItem(index, txt)


if __name__ == '__main__':
    app = QApplication([])
    create_table()
    window = Example()
    window.show()
    app.exec()
