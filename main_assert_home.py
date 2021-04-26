import sys
import pyodbc
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow,QMessageBox,QWidget


class MainWindow(QMainWindow,QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_assert.ui",self)
        self.actionSONY.triggered.connect(self.gotosony)
        self.actionSPRITE.triggered.connect(self.gotosprite)
        self.loaddata()

    def loaddata(self):
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=DESKTOP-V5JQHLU;"
                              "Database=Assert;"
                              "Trusted_Connection=yes;")

        cursor = conn.cursor()
        sqlquery=cursor.execute('SELECT * FROM Sheet1')
        self.tableWidget.setRowCount(50)
        tablerow=0
        for row in sqlquery:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow+=1


    def gotosony(self):
        Sony = sony()
        widget.addWidget(Sony)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotosprite(self):
        Sprite = sprite()
        widget.addWidget(Sprite)
        widget.setCurrentIndex(widget.currentIndex()+1)

class sony(QDialog):
    def __init__(self):
        super(sony,self).__init__()
        loadUi("add_sony_data.ui",self)
        self.cancel.clicked.connect(self.gotomain)
        self.loaddata()

    def loaddata(self):
        conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                              "Server=DESKTOP-V5JQHLU;"
                              "Database=Assert;"
                              "Trusted_Connection=yes;")

        cursor = conn.cursor()
        sqlquery = cursor.execute("SELECT * FROM Sheet1 WHERE Project='Sony' ")
        self.tableWidget.setRowCount(50)
        tablerow = 0
        for row in sqlquery:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow += 1

    def gotomain(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)


class sprite(QDialog):
    def __init__(self):
        super(sprite,self).__init__()
        loadUi("add_sprite_data.ui",self)
        self.cancel.clicked.connect(self.gotomain)

    def gotomain(self):
        mainwindow = MainWindow()
        widget.addWidget(mainwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow = MainWindow()
widget.addWidget(mainwindow)
widget.show()

try:
    sys.exit(app.exec_())

except:
    print("Exiting")
