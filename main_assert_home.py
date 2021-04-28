import sys
import pyodbc
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel

server = '10.209.25.201'
database = 'AssertDB'
username = 'sa'
password = 'devctti@123'


class query:
    def query_s(self):
        self.tableWidget.setRowCount(1000)
        tablerow = 0
        for row in self.sqlquery:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1


class query_ss:
    def query_sss(self):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(self.sqlquery):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


class MainWindow(QMainWindow, QWidget, query,query_ss):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_assert.ui", self)
        self.actionSony_2.triggered.connect(self.gotosony)
        self.actionSprite.triggered.connect(self.gotosprite)
        self.actionExit.triggered.connect(self.gotoexit)
        self.serial_lineEdit.textChanged.connect(self.serial_no_search)
        self.setWindowTitle('Assert Details')
        self.searchinput=self.serial_lineEdit
        self.data()
        self.query_s()
        widget.setFixedWidth(800)
        widget.setFixedHeight(700)
        widget.show

    def serial_no_search(self):

        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        searchol=""
        search = cursor.execute("SELECT * FROM Sheet1 WHERE [SERIAL NUMBER]= '+str(searchol)';" )
        row=search .fetchone()


        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(search):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        model=QStandardItemModel(4,4)
        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(1)



    def data(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        self.sqlquery = cursor.execute('SELECT * FROM Sheet1')

    def gotosony(self):
        Sony = sony()
        widget.addWidget(Sony)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotosprite(self):
        Sprite = sprite()
        widget.addWidget(Sprite)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotoexit(self):
        sys.exit()


class sony(QDialog, query):
    def __init__(self):
        super(sony, self).__init__()
        loadUi("add_sony_data.ui", self)
        self.cancel.clicked.connect(self.gotomain)
        self.loaddatas()
        self.query_s()
        widget.setFixedWidth(1000)
        widget.setFixedHeight(700)
        widget.show

    def loaddatas(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        self.sqlquery = cursor.execute("SELECT * FROM Sheet1 WHERE Project='Sony' ")

    def gotomain(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class sprite(QDialog, query_ss):
    def __init__(self):
        super(sprite, self).__init__()
        loadUi("add_sprite_data.ui", self)
        self.cancel.clicked.connect(self.gotomain)
        self.loaddata_s()
        self.query_sss()
        widget.setFixedWidth(1000)
        widget.setFixedHeight(700)
        widget.show

    def loaddata_s(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        self.sqlquery = cursor.execute("SELECT * FROM Sheet1 WHERE Project='Sprite' ")

    def gotomain(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

mainwindow = MainWindow()
widget.addWidget(mainwindow)
widget.show()

try:
    sys.exit(app.exec_())

except:
    print("Exiting")
