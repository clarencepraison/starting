import sys
import pyodbc
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QLineEdit,QMainWindow, QMessageBox, QWidget, QTableWidgetItem
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtSql import QSqlDatabase

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

class events:
    def SERIAL_NUMBER(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        SERIAL_NO=self.serial_lineEdit.text()
        #Description=self.description_lineEdit.text()
        #VENDOR=self.vendor_lineEdit.text()
        #DATE=int(self.d_dateEdit.text())

        sqlquery ='SELECT * FROM Sheet1 WHERE ([SERIAL NUMBER])=  ?'
        result=cursor.execute(sqlquery,[SERIAL_NO])

        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def add_data(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        SERIAL_NO = self.serial_lineedit.text()
        DESCRIPTION=self.description_lineedit.text()
        VENDOR=self.vendor_lineedit.text()
        PRICE=str(self.price_lineedit.text())
        PROJECT=self.project_lineedit.text()


        sqlquery = 'INSERT INTO Sheet2 (serial_number,description,vendor,price,project) VALUES (?,?,?,? ?);'
        cursor.execute(sqlquery,SERIAL_NO,DESCRIPTION,VENDOR,PRICE,PROJECT)

    def delete(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        x=self.self.serial_lineEdit.text()
        sqlquery = 'DELETE FROM Sheet2 WHERE serial_number =  ? '
        cursor.execute(sqlquery, x)


class MainWindow(QMainWindow, QWidget, query,events):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_assert.ui", self)
        self.actionSony_2.triggered.connect(self.gotosony)
        self.actionSprite.triggered.connect(self.gotosprite)
        self.actionExit.triggered.connect(self.gotoexit)
        self.search.clicked.connect(self.SERIAL_NUMBER)
        self.cancel.clicked.connect(self.cancel_btn)
        self.data()
        self.query_s()
        widget.setWindowTitle("IT Assert")
        widget.setFixedWidth(800)
        widget.setFixedHeight(700)
        widget.show


    def data(self):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
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

    def cancel_btn(self):
        self.data()
        self.query_s()

    def gotoexit(self):
        sys.exit()


class sony(QDialog, query_ss,events):
    def __init__(self):
        super(sony, self).__init__()
        loadUi("add_sony_data.ui", self)
        #self.cancel.clicked.connect(self.gotomain)
        #self.search.clicked.connect(self.SERIAL_NUMBER)
        #self.add.clicked.connect(self.add_data)
        self.delete_2.clicked.connect(self.delete)
        self.loaddatas()
        self.query_sss()
        widget.setFixedWidth(1000)
        widget.setFixedHeight(700)
        widget.show

    def loaddatas(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        self.sqlquery = cursor.execute("SELECT * FROM Sheet2  ")

    def gotomain(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class sprite(QDialog, query_ss,events):
    def __init__(self):
        super(sprite, self).__init__()
        loadUi("add_sprite_data.ui", self)
        self.cancel.clicked.connect(self.gotomain)
        self.search.clicked.connect(self.SERIAL_NUMBER)
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
