# WORk from line 420
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QMessageBox
import os
import socket
import sys
import time
import datetime
import geocoder

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
        self.tabE.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FinalYearProject)

    def retranslateUi(self, FinalYearProject):
        _translate = QtCore.QCoreApplication.translate
        FinalYearProject.setWindowTitle(_translate("FinalYearProject", "FinalYearProject"))
        self.buttonEncrpyt.setText(_translate("FinalYearProject", "Begin Encryption"))
        self.tabE.setTabText(self.tabE.indexOf(self.Encryption), _translate("FinalYearProject", "Encryption"))
        self.browseBtn.setText(_translate("FinalYearProject", "Browse"))
        self.buttonDecrypt.setText(_translate("FinalYearProject", "Begin Decryption"))
        self.tabE.setTabText(self.tabE.indexOf(self.Decryption), _translate("FinalYearProject", "Decryption"))
        self.browseBtn.clicked.connect(self.browsefiles)
        self.buttonEncrpyt.clicked.connect(self.beginEncryptTrigger)
        self.buttonDecrypt.clicked.connect(self.beginDecryptTrigger)

    def is_connected(self,hostname):
        try:
            host = socket.gethostbyname(hostname)
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except:
           pass
        return False
    
    def browsefiles(self):
        filename = QFileDialog.getOpenFileName(None,"Open Key File" , '.', "LDT file (*.ldt)")
        path = filename[0]
        self.fileName.setText(path)
        
    def toString(self, val):
        val = str(val)
        return val.replace('.','')   

    def genKeys(self,ts, g, ip):
        keyA = int(ts) % 126
        keyB = int(g) % 126
        keyC = int(ip)  % 126
        if(keyA == 0 or keyA == 126):
            keyA = (int(ts)*3) % 126
        if(keyB == 0  or keyB == 126):
            keyB = (int(ts)*3) % 126
        if(keyC == 0 or keyC == 126):
            keyC = (int(ts)*3) % 126 
        return [keyA, keyB, keyC]
    
    def rotate(self, val, shift):
        x = shift % len(val)
        temp  = []
        final_r = ''
        for i in val:
            temp.append(i)
        test_list = temp[x:] + temp[:x]
        for i in test_list:
            final_r += i
        return final_r

    def revRotate(self, val, shift):
        x = shift % len(val)
        temp  = []
        final_r = ''
        for i in val:
            temp.append(i)
        test_list = temp[-x:] + temp[:-x]
        for i in test_list:
            final_r += i
        return final_r
   
    def dirAloc(self, val):
        name = ''
        val = val[::-1]
        for i in val:
            if i in '/':
                break
            else:
                name += i
                val = val[1:]
        return [val[::-1],name[::-1]]

    def keySeperator(self,x,y):
        newKey = x
        c1 = ''
        c2 = ''
        ca = ''
        cb = ''
        cx = []
        cy = []
        newKey = newKey.replace(y,'')
        
        if 'nul' in newKey:
            return (cx,cy)
        else:
            for index,i in enumerate(newKey):
                if 'y' in i:
                    c2 = newKey
                    break
                else:
                    c1 += i
                    newKey = newKey[1:]
            
            if len(c1) > 0:
                c1 = c1[1:]
                c1 += 'x' 
                for i in c1:
                    if 'x' in i:
                        cx.append(int(ca))
                        ca = ''
                    else:
                        ca += i 

            if len(c2) > 0:
                c2 = c2[1:]
                c2 += 'y'
                for i in c2:
                    if 'y' in i:
                        cy.append(int(cb))
                        cb = ''
                    else:
                        cb += i
            return [cx,cy]

    def mainKeySeperator(self,string):
        x = string+'|'
        temp = ''
        ts = ''
        ip = ''
        g = ''
        glong = ''

        for i in x:
            if '?' in i:
                ts = temp
                temp = ''
            elif '@' in i:
                ip = temp
                temp = ''
            elif '!' in i:
                g = temp
                temp = ''
            elif '|' in i:
                glong = temp
                temp =''
            else:
                temp += i
            
        return [ts,ip,g,glong]

    def beginDecipher(self,string):
        checkA = False
        checkB = False
        checkC = False
        temp = ''
        key = string
        final = 0
        final_2 = 0
        segregrater = ''
        segre_A = ''
        segre_B = ''
        segre_C = ''

        for elem in key:
            if "--250102--" in key:
                checkA = True
            if "--100512--" in key:
                checkB = True
            if "--999998" in key:
                checkC = True
        
        if checkA and checkB and checkC:
            for index, i in enumerate(key):
                if '*' in i:
                    final = index + 1
                elif '|' in i:
                    final_2 = index
                
                
            segregrater = key[0:final]
            segregrater = segregrater.replace('**','-')

            
            for i in segregrater:
                if '-' in i:
                    if len(segre_A) <= 0:
                        segre_A = temp
                        temp = ''
                        segregrater = segregrater[1:]
                    elif len(segre_B) <= 0:
                        segre_B = temp
                        temp = '' 
                        segregrater = segregrater[1:]
                    else:
                        segre_C = temp
                else:
                    temp += segregrater[0]
                    segregrater = segregrater[1:]

            key = key[final:final_2]
            key2 =string[final_2+1:]

            temp  = int(segre_A)
            segre_A = key[:int(segre_A)]
            segre_A = segre_A.replace('ax','x')
            segre_A = segre_A.replace('ay','y')
            key = key[temp:]

            temp  = int(segre_B)
            segre_B = key[:int(segre_B)]
            segre_B = segre_B.replace('bx','x')
            segre_B = segre_B.replace('by','y')
            key = key[temp:]

            temp  = int(segre_C)
            segre_C = key[:int(segre_C)]
            segre_C = segre_C.replace('cx','x')
            segre_C = segre_C.replace('cy','y')
            key = key[temp:]

            segre_A = self.keySeperator(segre_A,'--250102--')
            segre_B = self.keySeperator(segre_B,'--100512--')
            segre_C = self.keySeperator(segre_C,'--999998')
            key2 = self.mainKeySeperator(key2)

            return [segre_A[0],segre_A[1],segre_B[0],segre_B[1],segre_C[0],segre_C[1],key2[0],key2[1],key2[2],key2[3]]
            

        
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Key Invalid")
            x = msg.exec_()
            sys.exit(app.exec_())

    def decrypt(self,ch, key, l94, l126):
        dec_final = ''
        for index, i in enumerate(ch):
            val = ord(i) - key
            if index in l94:
                val = val + 94
            elif index in l126:
                val = val + 126
            dec_final += chr(val)
        return(dec_final)       
    
    def encrypt(self, ch, key):
        enc_final = ''
        edit94 = []
        edit126 = []
        #print('Key',key)
        for index, i in enumerate(ch):
            val  = ord(i) +  key
            if (val > 126):
                #print('Change',val)
                val = val - 126
                if val < 32:
                    val += 32
                    edit94.append(index)
                else:
                    edit126.append(index)
            listA.append(chr(val))  
            enc_final += chr(val)  
            #print(index,':',i,':', val , ':', chr(val))
        return [edit126, edit94, enc_final]

    def popup_clicked(self, i):
        #print(i.text())
        if i.text() == 'Retry':
            return self.beginEncryptTrigger()
        else:
            sys.exit(app.exec_())
    
    def popupOk_clicked(self,i):
        if i.text() == 'Ok':
            self.textEncrypt.setPlainText('')
        return None
    
    def beginEncryptTrigger(self):
        #Checks for internet conenection
        REMOTE_SERVER = "one.one.one.one"
        internetVerifier = self.is_connected(REMOTE_SERVER)
        if internetVerifier:
            #print('Connection Sucess')
            g = geocoder.ip('me').latlng
            g_lat = g[0]
            g_lon = g[1]
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Internet Connection Unavailable")
            msg.setInformativeText("Please check your internet connection")
            msg.setStandardButtons(QMessageBox.Retry | QMessageBox.Abort)
            msg.setDefaultButton(QMessageBox.Retry)
            msg.buttonClicked.connect(self.popup_clicked)
            x = msg.exec_()



        #initializers Values for Encryption
        ch = self.textEncrypt.toPlainText()
        ts = time.time()
        ip = socket.gethostbyname(socket.gethostname())
        ts = self.toString(ts)
        ip = self.toString(ip)
        g = self.toString(g_lat)

        
        if len(ch) <1:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Missing Message")
            msg.setInformativeText("Please insert the message to encrypt")
            msg.buttonClicked.connect(self.popupOk_clicked)
            x = msg.exec_()
        elif ch == '':
            return None
        
        else:
        #KEYS GENERATION
            myKeys = self.genKeys(ts, g, ip)
            keyA = myKeys[0] 
            keyB = myKeys[1]
            keyC = myKeys[2]
            finalKey = ''
            tcp= ''
            saveFname = ''
            saveFdir = ''
            tval = 0

            ciph1 = self.encrypt(ch, keyA)
            edit126_A = ciph1[0]
            edit94_A = ciph1[1]
            finalA = ciph1[2]
            ciph1_r = self.rotate(finalA, int(g_lon))

            ciph2 = self.encrypt(ciph1_r, keyB)
            edit126_B = ciph2[0]
            edit94_B = ciph2[1]
            finalB = ciph2[2]
            ciph2_r = self.rotate(finalB, int(g_lon))

            ciph3 = self.encrypt(ciph2_r, keyC)
            edit126_C = ciph3[0]
            edit94_C = ciph3[1]
            finalC = ciph3[2]
            ciph3_r = self.rotate(finalC, int(g_lon))

            #print to PlainTextArea
            self.textEncrypt.setPlainText(ciph3_r)

            #Createing Key File Here
            if len(edit126_A) > 0 or len(edit94_A) > 0:
                for i in edit126_A:
                    finalKey += 'ax'+str(i)

                for i in edit94_A:
                    finalKey += 'ay'+str(i)
            else:
                finalKey += 'nul'
            finalKey += '--250102--'

            tval = len(finalKey)
            tcp += str(tval)+'**'



            if len(edit126_B) > 0 or len(edit94_B) > 0:
                for i in edit126_B:
                    finalKey += 'bx'+str(i)

                for i in edit94_B:
                    finalKey += 'by'+str(i)
            else:
                finalKey += 'nul'
            finalKey += '--100512--'

            tval =  len(finalKey)-tval
            tcp += str(tval)+'**'
            tval = len(finalKey)


            if len(edit126_C) > 0 or len(edit94_C) > 0:
                for i in edit126_C:
                    finalKey += 'cx'+str(i)

                for i in edit94_C:
                    finalKey += 'cy'+str(i)
            else:
                finalKey += 'nul'
            finalKey += '--999998'

            tval = len(finalKey) - tval
            tcp += str(tval)+'**'

            #print(edit126_A, edit94_A)
            #print(edit126_B, edit94_B)
            #print(edit126_C, edit94_C)
            finalKey = tcp + finalKey + '|' + ts +'?' +  ip + '@' + g + '!' + str(int(g_lon))
            #print(finalKey)

            sfilename = QFileDialog.getSaveFileName(None, 'Save Encryption Key','', "LDT file (*.ldt)")
            while len(sfilename[0]) <1 :
                msg = QMessageBox()
                msg.setWindowTitle("Warning")
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Select Diretory")
                msg.setInformativeText("Please include Save Location")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                x = msg.exec_()

                if x == QMessageBox.Ok:
                    sfilename = QFileDialog.getSaveFileName(None, 'Save Encryption Key','', "LDT file (*.ldt)")
                elif x == QMessageBox.Cancel:
                    sys.exit(app.exec_())
            else:
                saveFdir = self.dirAloc(sfilename[0])
                sfilename = saveFdir[1]
                saveFdir = saveFdir[0]
    
                completeName = os.path.join(saveFdir, sfilename)
                #print(sfilename,saveFdir)
    
                fileFinal = open(completeName, "w")
                fileFinal.write(finalKey)
                fileFinal.close
                
    def beginDecryptTrigger(self):

        filePath = self.fileName.text()
        ch  = self.textDecrypt.toPlainText()
        key = ''

        while len(filePath) <1 :
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Select Diretory")
            msg.setInformativeText("Please insert key file")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            x = msg.exec_()
            if x == QMessageBox.Ok:
                self.browsefiles()
            elif x == QMessageBox.Cancel:
                sys.exit(app.exec_())

        if len(ch) <1:
            msg = QMessageBox()
            msg.setWindowTitle("Warning")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Missing Cipher")
            msg.setInformativeText("Please insert the message to decrypt")
            x = msg.exec_()
            if x == QMessageBox.Ok:
                self.textDecrypt.setPlainText('')
        elif ch == '':
            return None

        else:
            with open(filePath, "r") as f:
                key = f.readline()
            if len(key) <= 0:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText("Key Invalid")
                x = msg.exec_()
                sys.exit(app.exec_())
            
            deciph = self.beginDecipher(key)
            #print('Trigger',deciph)  #WORK FROM HERE
            g_lon = int(deciph[9])
            myKeys = self.genKeys(int(deciph[6]), int(deciph[8]), int(deciph[7]))
            keyA = myKeys[0] 
            keyB = myKeys[1]
            keyC = myKeys[2]
            edit94_C = deciph[5]
            edit126_C = deciph[4]
            edit94_B = deciph[3]
            edit126_B = deciph[2]
            edit94_A = deciph[1]
            edit126_A = deciph[0]

            revCiph3_r = self.revRotate(ch,int(g_lon))
            revCiph3 = self.decrypt(revCiph3_r, keyC, edit94_C, edit126_C)

            revCiph2_r = self.revRotate(revCiph3,int(g_lon))
            revCiph2 = self.decrypt(revCiph2_r, keyB, edit94_B, edit126_B)

            revCiph1_r = self.revRotate(revCiph2,int(g_lon))
            revCiph1 = self.decrypt(revCiph1_r, keyA, edit94_A, edit126_A)

            self.textDecrypt.setPlainText(revCiph1)
        

if __name__ == "__main__":


    #Values for Keys change
    
    listA = []
    edit126_A = []
    edit94_A = []
    edit126_B = []
    edit94_B = []
    edit126_C = []
    edit94_C = []

    app = QtWidgets.QApplication(sys.argv)
    FinalYearProject = QtWidgets.QMainWindow()
    ui = Ui_FinalYearProject()
    ui.setupUi(FinalYearProject)
    FinalYearProject.show()
    sys.exit(app.exec_())