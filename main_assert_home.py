import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 679)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.v_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.v_lineEdit.setGeometry(QtCore.QRect(340, 30, 181, 20))
        self.v_lineEdit.setStyleSheet("font: 9pt \"Calibri\";")
        self.v_lineEdit.setObjectName("v_lineEdit")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(600, 70, 75, 23))
        self.cancel.setStyleSheet("font: 75 10pt \"Clarendon Condensed\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.cancel.setObjectName("cancel")
        self.d_dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.d_dateEdit.setGeometry(QtCore.QRect(570, 30, 110, 22))
        self.d_dateEdit.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.d_dateEdit.setObjectName("d_dateEdit")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 741, 551))
        self.tableWidget.setMinimumSize(QtCore.QSize(591, 0))
        self.tableWidget.setStyleSheet("font: 75 12pt \"Cambria\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.vendor = QtWidgets.QLabel(self.centralwidget)
        self.vendor.setGeometry(QtCore.QRect(290, 30, 41, 20))
        self.vendor.setStyleSheet("font: 75 10pt \"Clarendon Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.vendor.setObjectName("vendor")
        self.date = QtWidgets.QLabel(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(530, 30, 31, 20))
        self.date.setStyleSheet("font: 75 10pt \"Clarendon Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.date.setObjectName("date")
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setGeometry(QtCore.QRect(500, 70, 75, 23))
        self.search.setStyleSheet("font: 75 10pt \"Clarendon Condensed\";\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);")
        self.search.setObjectName("search")
        self.description = QtWidgets.QLabel(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(10, 30, 71, 20))
        self.description.setStyleSheet("font: 75 10pt \"Clarendon Condensed\";\n"
"color: rgb(0, 0, 127);")
        self.description.setObjectName("description")
        self.d_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.d_lineEdit.setGeometry(QtCore.QRect(90, 30, 191, 20))
        self.d_lineEdit.setStyleSheet("font: 9pt \"Calibri\";")
        self.d_lineEdit.setObjectName("d_lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(690, 30, 71, 22))
        self.comboBox.setStyleSheet("font: 75 10pt \"Calibri\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 21))
        self.menubar.setObjectName("menubar")
        self.menuADD = QtWidgets.QMenu(self.menubar)
        self.menuADD.setObjectName("menuADD")
        self.menuADD_2 = QtWidgets.QMenu(self.menuADD)
        self.menuADD_2.setObjectName("menuADD_2")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionFile = QtWidgets.QAction(MainWindow)
        self.actionFile.setObjectName("actionFile")
        self.actionSONY = QtWidgets.QAction(MainWindow)
        self.actionSONY.setObjectName("actionSONY")
        self.actionSPRITE = QtWidgets.QAction(MainWindow)
        self.actionSPRITE.setObjectName("actionSPRITE")
        self.menuADD_2.addAction(self.actionSONY)
        self.menuADD_2.addSeparator()
        self.menuADD_2.addAction(self.actionSPRITE)
        self.menuADD.addAction(self.menuADD_2.menuAction())
        self.menubar.addAction(self.menuADD.menuAction())

        self.retranslateUi(MainWindow)
        self.cancel.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DESCRIPTION"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "VENDOR"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DATE"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PRICE"))
        self.vendor.setText(_translate("MainWindow", "Vendor "))
        self.date.setText(_translate("MainWindow", "Date"))
        self.search.setText(_translate("MainWindow", "Search"))
        self.description.setText(_translate("MainWindow", "Description"))
        self.comboBox.setItemText(0, _translate("MainWindow", "SONY"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SPRITE"))
        self.menuADD.setTitle(_translate("MainWindow", "Menu"))
        self.menuADD_2.setTitle(_translate("MainWindow", "ADD"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionFile.setText(_translate("MainWindow", "New"))
        self.actionSONY.setText(_translate("MainWindow", "SONY"))
        self.actionSPRITE.setText(_translate("MainWindow", "SPRITE"))
        self.actionSony_2.clicked.connect(self.gotosony_data)

    def gotosony_data(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

class sony_data(QDialog):
     def __init__(self):
        super(sony_data,self).__init__()
        loadUi("add_sony_data.ui",self)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

widget=QtWidgets.QStackedWidget()
mainwindow=Ui_MainWindow()
sony=sony_data()
widget.addWidget(mainwindow)
widget.addWidget(sony)
widget.show()
