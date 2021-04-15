import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QDialogButtonBox



class Assert(QMainWindow):
    def __init__(self):
        
        super().__init__()

        self.setWindowTitle("IT Assert")
        self.setFixedSize(1420,900)
        self.generalLayout=QHBoxLayout()
        
        self._centralWidget=QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createDisplay()
        

    def _createDisplay(self):

        dlgLayout = QHBoxLayout()
        formLayout= QFormLayout()
        formLayout.addRow('Name:',QLineEdit())
        formLayout.addRow('Serial.No:',QLineEdit())
        formLayout.addRow('Date:',QLineEdit())
        formLayout.addRow('Vendor Name:',QLineEdit())
        dlgLayout.addLayout(formLayout)
        btns=QDialogButtonBox()
        btns.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)
        self.generalLayout.addLayout(dlgLayout)
        self.generalLayout.addLayout(formLayout)
        
        
        
        

       


def main():

    a=QApplication(sys.argv)
    view=Assert()
    view.show()
    sys.exit(a.exec_())

if __name__ == '__main__':
    main()
