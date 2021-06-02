# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import socket

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 731, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(120, 20, 91, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 60, 91, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(240, 20, 301, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 60, 301, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.toolButton = QtWidgets.QToolButton(self.groupBox)
        self.toolButton.setEnabled(True)
        self.toolButton.setGeometry(QtCore.QRect(240, 100, 81, 41))
        self.toolButton.setAutoRaise(False)
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_2.setGeometry(QtCore.QRect(350, 100, 81, 41))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_3.setGeometry(QtCore.QRect(460, 100, 81, 41))
        self.toolButton_3.setObjectName("toolButton_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(120, 160, 61, 20))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(240, 160, 61, 20))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(40, 230, 731, 301))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(110, 80, 591, 191))
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 30, 591, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 101, 31))
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        self.toolButton.clicked.connect(self.scan)
        self.toolButton_2.clicked.connect(self.connect)
        
        self.lineEdit_3.returnPressed.connect(self.submit)

    #============================================
    def connect(self):
        try:

            global s 
            s = socket.socket()

            ip = self.lineEdit.text()
            port = int(self.lineEdit_2.text())

            s.connect((ip,port))
            self.textEdit.append("Connection success!")
            
    
        except ConnectionRefusedError as e:
            self.textEdit.append("No connection!")
    def submit(self):
        msg = self.lineEdit_3.text()
        s.send(bytes(msg,"utf-8"))
        from_server = s.recv(2048)
        self.textEdit.append(from_server.decode())
        self.lineEdit_3.clear()
            
        # s.close()
        
        
    def scan(self):
        try:
            ip = self.lineEdit.text()
            port = int(self.lineEdit_2.text())

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((ip,port))
            if result == 0:
                self.label_5.setText("Open")
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(0, 255, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                self.label_5.setPalette(palette)
            else:
                self.label_5.setText("Close")
                palette = QtGui.QPalette()
                brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
                brush.setStyle(QtCore.Qt.SolidPattern)
                palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
                brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
                self.label_5.setPalette(palette)
            s.close()
        except ValueError as e:
            self.label_5.setText("None")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Connection"))
        self.label.setText(_translate("MainWindow", "IP address"))
        self.label_2.setText(_translate("MainWindow", "Port"))
        self.toolButton.setText(_translate("MainWindow", "Scan"))
        self.toolButton_2.setText(_translate("MainWindow", "Connect"))
        self.toolButton_3.setText(_translate("MainWindow", "Log out"))
        self.label_3.setText(_translate("MainWindow", "Status"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Command"))
        self.label_4.setText(_translate("MainWindow", "From Server"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
