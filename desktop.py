from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,500,500)
        self.setWindowTitle('FirstTime')
        self.initUI()    

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText('First Text box')
        self.label.move(250,250)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Encrypt')
        self.b1.clicked.connect(self.encrypy)

        self.b2 = QtWidgets.QPushButton(self)
        self.b2.setText('Decrypt')
        self.b2.clicked.connect(self.decrypt)
        self.b2.move(100,0)

    def encrypy(self):
        self.label.setText('Clicked Box to Encrypt')
        self.update()
    
    def decrypt(self):
        self.label.setText('Clicked Box to Decrypt') 
        self.update()
    
    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    

    win.show()
    sys.exit(app.exec_())

window()