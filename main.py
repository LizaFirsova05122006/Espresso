import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QTableWidgetItem


class DBSample(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect("coffee.db")
        self.pushButton.clicked.connect(self.open_main_form)

    def open_main_form(self):
        res = self.connection.cursor().execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Название сорта', 'Степень обжарки',
                                                    'Молотый/в зернах', 'Вкус', 'Цена', 'Объем'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DBSample()
    ex.show()
    sys.exit(app.exec())