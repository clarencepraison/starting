import sys
import pyodbc
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem,QLineEdit, QTableWidget,QHeaderView, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtCore import Qt
from PyQt5.QtSql import *
from PyQt5.QtSql import QSqlTableModel
import re


server = '10.209.25.201'
database = 'AssertDB'
username = 'sa'
password = 'devctti@123'


class query:
    def query_s(self):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(self.sqlquery):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

class events:
    def add_data(self):
        self.SERIAL_NO = self.serial_lineEdit.text()
        self.DESCRIPTION = self.description_lineEdit.text()
        self.VENDOR = self.vendor_lineEdit.text()
        self.DATE = str(self.received_dateEdit.text())
        self.PRICE = str(self.price_lineEdit.text())
        self.PROJECT = self.project_lineEdit.text()
        self.list = [self.SERIAL_NO, self.DESCRIPTION, self.VENDOR, self.DATE, self.PRICE, self.PROJECT]
        x = re.findall("[a-z,A-Z]", self.SERIAL_NO or self.DESCRIPTION or self.VENDOR)
        if not x:
            QMessageBox.about(self, "ERROR", "Enter any data")
        else:
            conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            cursor = conn.cursor()
            sqlquery_ = '''INSERT INTO Sheet1 (SERIAL_NUMBER,DESCRIPTION,VENDOR,DATE,PRICE,Project) VALUES (?,?,?,?,?,?);'''
            QMessageBox.about(self, "SUCCESS", "Data Added Sucessfully!")
            cursor.execute(sqlquery_, self.list)
            conn.commit()

    def serial_search(self):

        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        command = '''SELECT * FROM Sheet1 WHERE SERIAL_NUMBER=? or DESCRIPTION=? or VENDOR=? or DATE=? '''

        self.SERIAL_NO = self.serial_lineEdit.text()
        self.DESCRIPTION_NO=self.description_lineEdit.text()
        self.VENDOR_=self.vendor_lineEdit.text()
        self.DATE_=self.received_dateEdit.text()
        self.y=[self.SERIAL_NO,self.DESCRIPTION_NO,self.VENDOR_,self.DATE_]
        result = cursor.execute(command,self.y)

        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conn.commit()

    def delete_data(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

        cursor = conn.cursor()
        SERIAL_NO = self.serial_lineEdit.text()
        command = '''DELETE FROM Sheet1 WHERE SERIAL_NUMBER=?'''

        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            print(command)

        cursor.execute(command, SERIAL_NO)
        conn.commit()

class Users(QMainWindow):
    def __init__(self):
        super(Users,self).__init__()
        loadUi("user_details.ui",self)
        widget.setFixedWidth(950)
        widget.setFixedHeight(700)
        widget.show


class MainWindow(QMainWindow, QWidget, query,events):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_assert.ui", self)
        self.actionSony_2.triggered.connect(self.gotosony)
        self.actionSprite.triggered.connect(self.gotosprite)
        self.actionExit.triggered.connect(self.closeEvent)
        self.actionUsers.triggered.connect(self.gotousers)
        self.cancel.clicked.connect(self.cancel_btn)
        self.search.clicked.connect(self.serial_search)
        self.data()
        self.query_s()
        widget.setFixedWidth(800)
        widget.setFixedHeight(700)
        widget.setWindowTitle("IT Assert")
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

    def gotomain_(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def gotousers(self):
        User = Users()
        widget.addWidget(User)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure do you want to close window',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            exits = sys.exit()
            event.accept()
            print(exits)

class sony(QMainWindow, query,events):
    def __init__(self):
        super(sony, self).__init__()
        loadUi("add_sony_data.ui", self)

        self.add.clicked.connect(self.add_data)
        self.search.clicked.connect(self.serial_search)
        self.cancel.clicked.connect(self.gotomain)
        self.refreshbutton.clicked.connect(self.gotomain)
        self.delete_2.clicked.connect(self.delete_data)
        self.homebutton.clicked.connect(self.gotomain_)
        self.loaddatas()
        self.query_s()


        widget.setFixedWidth(950)
        widget.setFixedHeight(700)
        widget.show

    def loaddatas(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        self.sqlquery = cursor.execute("SELECT * FROM Sheet1 WHERE Project='Sony'  ")

    def gotomain(self):
        self.loaddatas()
        self.query_s()

    def gotomain_(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class sprite(QMainWindow, query,events):
    def __init__(self):
        super(sprite, self).__init__()
        loadUi("add_sprite_data.ui", self)

        self.add.clicked.connect(self.add_data)
        self.search.clicked.connect(self.serial_search)
        self.delete_2.clicked.connect(self.delete_data)
        self.cancel.clicked.connect(self.gotomain)
        self.refreshbutton.clicked.connect(self.gotomain)
        self.homebutton.clicked.connect(self.gotomain_)
        self.loaddata_s()
        self.query_s()
        widget.setFixedWidth(1000)
        widget.setFixedHeight(700)
        widget.show

    def loaddata_s(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        self.sqlquery = cursor.execute("SELECT * FROM Sheet1 WHERE Project='Sprite' ")

    def gotomain(self):
        self.loaddata_s()
        self.query_s()

    def gotomain_(self):
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
