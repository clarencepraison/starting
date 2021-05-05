import sys
import pyodbc
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QSizePolicy, QApplication, QMainWindow, QMessageBox, QWidget,QSizeGrip, QTableWidgetItem,QLineEdit, QTableWidget,QHeaderView, QVBoxLayout
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtCore import Qt
from PyQt5.QtSql import *
from PyQt5.QtSql import QSqlTableModel

'''class query:
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
            tablerow += 1'''

class query:
    def query_s(self):
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(self.sqlquery):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))

class events:

    def add_data(self):
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=DESKTOP-V5JQHLU;"
                              "Database=Assert;"
                              "Trusted_Connection=yes;")

        cursor = conn.cursor()
        SERIAL_NO=self.serial_lineEdit.text()
        DESCRIPTION=self.description_lineEdit.text()
        VENDOR=self.vendor_lineEdit.text()
        PROJECT=self.project_lineEdit.text()
        DATE = str(self.d_dateEdit.text())
        PRICE = str(self.price_lineEdit.text())

        list=(SERIAL_NO,DESCRIPTION,VENDOR,PROJECT,DATE,PRICE)
        query='''INSERT INTO Sheet1(Serial_no,Descriptions,Vendor,Project,Invoice_Date,Price) VALUES (?,?,?,?,?,?) '''
        QMessageBox.about(self,"SUCESS","Data Added Sucessfully!")
        cursor.execute(query, list)
        conn.commit()




    def delete_data(self):
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=DESKTOP-V5JQHLU;"
                              "Database=Assert;"
                              "Trusted_Connection=yes;")

        cursor = conn.cursor()
        SERIAL_NO = self.serial_lineEdit.text()
        command = '''DELETE FROM Sheet1 WHERE Serial_no=?'''
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            print(command)


        cursor.execute(command,SERIAL_NO)
        conn.commit()

    def serial_search(self):
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=DESKTOP-V5JQHLU;"
                              "Database=Assert;"
                              "Trusted_Connection=yes;")
        cursor = conn.cursor()
        command = '''SELECT * FROM Sheet1 WHERE  Serial_no=? or Descriptions=? '''

        SERIAL_NO = self.d_lineEdit.text()
        DESCRIPTION=self.v_lineEdit.text()

        result = cursor.execute(command,SERIAL_NO, DESCRIPTION)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        conn.commit()
class MainWindow(QMainWindow, QWidget, query,events):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_assert.ui", self)
        self.actionSONY.triggered.connect(self.gotosony)
        self.actionSPRITE.triggered.connect(self.gotosprite)
        #self.actionUsers.triggered.connect(self.user)
        self.actionExit.triggered.connect(self.closeEvent)
        self.search.clicked.connect(self.serial_search)
        self.cancel.clicked.connect(self.cancel_)
        self.data()
        self.query_s()
        widget.setGeometry(100,100,1000,700)
        widget.setWindowTitle("Assert Details")
        widget.show

    def data(self):
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                  "Server=DESKTOP-V5JQHLU;"
                                  "Database=Assert;"
                                  "Trusted_Connection=yes;")

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

    def user(self):
        User=user_details()
        widget.addWidget(User)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def cancel_(self):
        self.data()
        self.query_s()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Window Close', 'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
            print('Window closed')
        else:
            event.ignore()

class user_details(QDialog):
    def __init__(self):
        super(user_details,self).__init__()
        loadUi("add_data.ui",self)
        widget.setGeometry(100, 100, 1000, 700)
        vbox=QVBoxLayout()
        sizegrip = QSizeGrip(self)
        vbox.addWidget(sizegrip)
        widget.setLayout(vbox)
        widget.show()


class sony(QDialog, query,events):
    def __init__(self):
        super(sony, self).__init__()
        loadUi("add_sony_data.ui", self)
        self.cancel.clicked.connect(self.gotomain)
        self.add.clicked.connect(self.add_data)
        self.delete_2.clicked.connect(self.delete_data)
        self.loaddatas()
        self.query_s()
        widget.setGeometry(100,100,1000,700)
        widget.show

    def loaddatas(self):
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                  "Server=DESKTOP-V5JQHLU;"
                                  "Database=Assert;"
                                  "Trusted_Connection=yes;")

        cursor = conn.cursor()
        self.sqlquery = cursor.execute("SELECT * FROM Sheet1 WHERE Project='Sony' ")

    def gotomain(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class sprite(QDialog, query):
    def __init__(self):
        super(sprite, self).__init__()
        loadUi("add_sprite_data.ui", self)
        self.cancel.clicked.connect(self.gotomain)
        self.loaddata_s()
        self.query_s()
        widget.setGeometry(100,100,1200,700)

        widget.show

    def loaddata_s(self):
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                  "Server=DESKTOP-V5JQHLU;"
                                  "Database=Assert;"
                                  "Trusted_Connection=yes;")

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





