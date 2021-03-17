
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog


class Ui_FinalYearProject(object):
    def setupUi(self, FinalYearProject):
        FinalYearProject.setObjectName("FinalYearProject")
        FinalYearProject.resize(638, 595)
        FinalYearProject.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        FinalYearProject.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(FinalYearProject)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabE = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        self.tabE.setFont(font)
        self.tabE.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabE.setAutoFillBackground(False)
        self.tabE.setStyleSheet("")
        self.tabE.setUsesScrollButtons(True)
        self.tabE.setDocumentMode(False)
        self.tabE.setTabsClosable(False)
        self.tabE.setMovable(False)
        self.tabE.setObjectName("tabE")
        self.Encryption = QtWidgets.QWidget()
        self.Encryption.setObjectName("Encryption")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.Encryption)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.textEncrypt = QtWidgets.QPlainTextEdit(self.Encryption)
        font = QtGui.QFont()
        font.setFamily("Neue Haas Grotesk Text Pro Medi")
        font.setPointSize(10)
        self.textEncrypt.setFont(font)
        self.textEncrypt.setObjectName("textEncrypt")
        self.gridLayout_3.addWidget(self.textEncrypt, 0, 0, 1, 1)
        self.buttonEncrpyt = QtWidgets.QPushButton(self.Encryption)
        self.buttonEncrpyt.setObjectName("buttonEncrpyt")
        self.gridLayout_3.addWidget(self.buttonEncrpyt, 1, 0, 1, 1)
        self.tabE.addTab(self.Encryption, "")
        self.Decryption = QtWidgets.QWidget()
        self.Decryption.setObjectName("Decryption")
        self.gridLayout = QtWidgets.QGridLayout(self.Decryption)
        self.gridLayout.setObjectName("gridLayout")


        self.browseBtn = QtWidgets.QPushButton(self.Decryption)
        self.browseBtn.setObjectName("browseBtn")
        self.gridLayout.addWidget(self.browseBtn, 0, 1, 1, 1)
        

        self.buttonDecrypt = QtWidgets.QPushButton(self.Decryption)
        self.buttonDecrypt.setObjectName("buttonDecrypt")
        self.gridLayout.addWidget(self.buttonDecrypt, 2, 0, 1, 2)
        self.fileName = QtWidgets.QLineEdit(self.Decryption)
        self.fileName.setObjectName("fileName")
        self.gridLayout.addWidget(self.fileName, 0, 0, 1, 1)
        self.textDecrypt = QtWidgets.QPlainTextEdit(self.Decryption)
        self.textDecrypt.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textDecrypt.setFont(font)
        self.textDecrypt.setMouseTracking(False)
        self.textDecrypt.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textDecrypt.setObjectName("textDecrypt")
        self.gridLayout.addWidget(self.textDecrypt, 1, 0, 1, 2)
        self.tabE.addTab(self.Decryption, "")
        self.gridLayout_2.addWidget(self.tabE, 0, 0, 1, 1)
        FinalYearProject.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FinalYearProject)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        FinalYearProject.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FinalYearProject)
        self.statusbar.setObjectName("statusbar")
        FinalYearProject.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(FinalYearProject)
        self.tabE.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(FinalYearProject)

    def retranslateUi(self, FinalYearProject):
        _translate = QtCore.QCoreApplication.translate
        FinalYearProject.setWindowTitle(_translate("FinalYearProject", "FinalYearProject"))
        self.buttonEncrpyt.setText(_translate("FinalYearProject", "Begin Encryption"))
        self.tabE.setTabText(self.tabE.indexOf(self.Encryption), _translate("FinalYearProject", "Encryption"))
        self.browseBtn.setText(_translate("FinalYearProject", "Browse"))
        self.buttonDecrypt.setText(_translate("FinalYearProject", "Begin Decryption"))
        self.tabE.setTabText(self.tabE.indexOf(self.Decryption), _translate("FinalYearProject", "Decryption"))
        self.menuFile.setTitle(_translate("FinalYearProject", "File"))
        self.browseBtn.clicked.connect(self.browsefiles)

    def browsefiles(self):
        
        filename = QFileDialog.getOpenFileName(None,"Open Key File" , '.', "secret file (*.din)")
        path = filename[0]
        self.fileName.setText(path)

        with open(path, "r") as f:
            word = f.readline()
            

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FinalYearProject = QtWidgets.QMainWindow()
    ui = Ui_FinalYearProject()
    ui.setupUi(FinalYearProject)
    FinalYearProject.show()
    sys.exit(app.exec_())
