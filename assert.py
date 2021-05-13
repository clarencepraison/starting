import sys
import pyodbc
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem, QLineEdit, \
    QTableWidget, QHeaderView, QVBoxLayout
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
    def add_user(self):
        self.serial_no=self.serial_lineEdit.text()
        self.description=self.description_lineEdit.text()
        self.user_name=self.user_lineEdit.text()
        self.issue_date=str(self.issue_dateEdit.text())
        self.location=self.location_lineEdit.text()
        self.project=self.project_lineEdit.text()
        self.list_=[self.serial_no,self.description,self.user_name,self.issue_date,self.location,self.project]
        x = re.findall("[a-z,A-Z]",self.serial_no or self.description or self.user_name or self.issue_date or self.location or self.project)
        if not x:
            QMessageBox.about(self, "ERROR", "Enter any data")
        else:
            conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
            cursor = conn.cursor()
            sqlquery_ = '''INSERT INTO user_details (SERIAL_NO,DESCRIPTION,USER_NAME,ISSUE_DATE,LOCATION,PROJECT) VALUES (?,?,?,?,?,?);'''
            QMessageBox.about(self, "SUCCESS", "Data Added Sucessfully!")
            cursor.execute(sqlquery_, self.list_)
            conn.commit()
    def serial_search(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor_ = conn.cursor()
        self.SERIAL_NO = self.serial_lineEdit.text()
        self.DESCRIPTION_NO = self.description_lineEdit.text()
        self.VENDOR_ = self.vendor_lineEdit.text()
        self.DATE_ = self.received_dateEdit.text()
        self.PRICE_ = self.price_lineEdit.text()
        self.PROJECT_ = self.project_lineEdit.text()
        self.y = [self.SERIAL_NO, self.DESCRIPTION_NO, self.VENDOR_, self.DATE_, self.PRICE_, self.PROJECT_]
        x = re.findall("[a-z,A-Z]", self.SERIAL_NO or self.DESCRIPTION_NO or self.VENDOR_ or self.PROJECT_)
        y = re.findall("[0-9]", self.DATE_ or self.PRICE_)
        if x or y:
            c = ("SELECT count(*) FROM Sheet1 WHERE SERIAL_NUMBER=? or DESCRIPTION=? or VENDOR=? or DATE=? or PRICE=? or Project=?")
            cursor_.execute(c, self.y)
            resul = cursor_.fetchall()
            x_ = (resul[-1][-1])
            print(x_)
            if x_ == 0:
                QMessageBox.about(self, "Error", "No data Found")

            else:
                command = '''SELECT * FROM Sheet1 WHERE SERIAL_NUMBER=? or DESCRIPTION=? or VENDOR=? or DATE=? or PRICE=? or Project=?'''
                result = cursor_.execute(command, self.y)
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(result):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                conn.commit()

        else:
            QMessageBox.about(self, "Error", "Enter Any DataFields")
        conn.close()
    def search_user(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor_ = conn.cursor()
        self.serial_no = self.serial_lineEdit.text()
        self.description = self.description_lineEdit.text()
        self.user_name = self.user_lineEdit.text()
        self.issue_date = self.issue_dateEdit.text()
        self.location = self.location_lineEdit.text()
        self.project = self.project_lineEdit.text()
        self.list_ = [self.serial_no, self.description, self.user_name, self.issue_date, self.location, self.project]
        x = re.findall("[a-z,A-Z]",self.serial_no or self.description or self.user_name  or self.location or self.project)
        y = re.findall("[0-9]", self.issue_date )
        if x or y:
            c = ("SELECT count(*) FROM user_details WHERE SERIAL_NO=? or DESCRIPTION=? or USER_NAME=? or ISSUE_DATE=? or LOCATION=? or PROJECT=?")
            cursor_.execute(c, self.list_)
            resul = cursor_.fetchall()
            x_ = (resul[-1][-1])
            print(x_)
            if x_ == 0:
                QMessageBox.about(self, "Error", "No data Found")

            else:
                command = '''SELECT * FROM user_details WHERE SERIAL_NO=? or DESCRIPTION=? or USER_NAME=? or ISSUE_DATE=? or LOCATION=? or PROJECT=?'''
                result = cursor_.execute(command, self.list_)
                self.tableWidget.setRowCount(0)
                for row_number, row_data in enumerate(result):
                    self.tableWidget.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                        self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
                conn.commit()
    def delete_data(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor_ = conn.cursor()
        self.SERIAL_NO = self.serial_lineEdit.text()
        self.DESCRIPTION_NO = self.description_lineEdit.text()
        self.VENDOR_ = self.vendor_lineEdit.text()
        self.DATE_ = self.received_dateEdit.text()
        self.PRICE_ = self.price_lineEdit.text()
        self.PROJECT_ = self.project_lineEdit.text()
        self.y = [self.SERIAL_NO, self.DESCRIPTION_NO, self.VENDOR_, self.DATE_, self.PRICE_, self.PROJECT_]
        x = re.findall("[a-z,A-Z]", self.SERIAL_NO or self.DESCRIPTION_NO or self.VENDOR_ or self.PROJECT_)
        y = re.findall("[0-9]", self.PRICE_)
        if x or y:
            c = (
                "SELECT count(*) FROM Sheet1 WHERE SERIAL_NUMBER=? or DESCRIPTION=? or VENDOR=? or DATE=? or PRICE=? or Project=?")
            cursor_.execute(c, self.y)
            resul = cursor_.fetchall()
            x_ = (resul[-1][-1])
            print(x_)

            if x_ == 0:
                QMessageBox.about(self, "Error", "No data Found")

            else:

                messageBox = QMessageBox.warning(
                    self,
                    "Warning!",
                    "Do you want to remove the selected contact?",
                    QMessageBox.Ok | QMessageBox.Cancel,
                )

                if messageBox == QMessageBox.Ok:
                    command = '''DELETE FROM Sheet1 WHERE SERIAL_NUMBER=?'''
                    cursor_.execute(command, self.SERIAL_NO)
                    conn.commit()
        else:
            QMessageBox.about(self, "Error", "Action Empty")

    def delete_USER_(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor_ = conn.cursor()
        self.serial_no = self.serial_lineEdit.text()
        self.description = self.description_lineEdit.text()
        self.user_name = self.user_lineEdit.text()
        self.issue_date = self.issue_dateEdit.text()
        self.location = self.location_lineEdit.text()
        self.project = self.project_lineEdit.text()
        self.list_ = [self.serial_no, self.description, self.user_name, self.issue_date, self.location, self.project]
        x = re.findall("[a-z,A-Z]",
                       self.serial_no or self.description or self.user_name or self.location or self.project)
        y = re.findall("[0-9]", self.issue_date)
        if x or y:
            c = ("SELECT count(*) FROM user_details WHERE SERIAL_NO=? or DESCRIPTION=? or USER_NAME=? or ISSUE_DATE=? or LOCATION=? or PROJECT=?")
            cursor_.execute(c, self.list_)
            resul = cursor_.fetchall()
            x_ = (resul[-1][-1])
            print(x_)
            if x_ == 0:
                QMessageBox.about(self, "Error", "No data Found")

            else:

                messageBox = QMessageBox.warning(
                    self,
                    "Warning!",
                    "Do you want to remove the selected contact?",
                    QMessageBox.Ok | QMessageBox.Cancel,
                )


                if messageBox == QMessageBox.Ok:
                    command = '''DELETE  FROM user_details WHERE  SERIAL_NO=?'''
                    cursor_.execute(command, self.serial_no)
                    conn.commit()
        else:
            QMessageBox.about(self, "Error", "Action Empty")


class MainWindow(QMainWindow, QWidget, query, events):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_assert.ui", self)
        self.actionSony_2.triggered.connect(self.assert_)
        self.actionSprite.triggered.connect(self.user_)
        self.actionExit.triggered.connect(self.closeEvent)
        self.cancel.clicked.connect(self.cancel_btn)
        self.search.clicked.connect(self.serial_search)
        self.data()
        self.query_s()
        widget.setFixedWidth(1060)
        widget.setFixedHeight(700)
        widget.setWindowTitle("IT Assert")
        widget.show

    def data(self):
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        cursor = conn.cursor()
        self.sqlquery = cursor.execute('SELECT * FROM Sheet1')

    def assert_(self):
        Sony = Assert_details()
        widget.addWidget(Sony)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def user_(self):
        user = user_details()
        widget.addWidget(user)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def cancel_btn(self):
        self.data()
        self.query_s()

    def gotomain_(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure do you want to close window',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            exits = sys.exit()
            event.accept()
            print(exits)


class Assert_details(QMainWindow, query, events):
    def __init__(self):
        super(Assert_details, self).__init__()
        loadUi("assert_details.ui", self)

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
        self.sqlquery = cursor.execute("SELECT * FROM Sheet1 ")

    def gotomain(self):
        self.loaddatas()
        self.query_s()

    def gotomain_(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class user_details(QMainWindow, query, events):
    def __init__(self):
        super(user_details, self).__init__()
        loadUi("user_details.ui", self)

        self.add.clicked.connect(self.add_user)
        self.search.clicked.connect(self.search_user)
        self.delete_2.clicked.connect(self.delete_USER_)
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
        self.sqlquery = cursor.execute("SELECT * FROM user_details ")

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


