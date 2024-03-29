# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_list_ip.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
import os
import socket

class Ui_Table(QDialog):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 587)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 60, 651, 401))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.toolButton_3 = QtWidgets.QToolButton(Form)
        self.toolButton_3.setGeometry(QtCore.QRect(170, 480, 81, 41))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(Form)
        self.toolButton_4.setGeometry(QtCore.QRect(320, 480, 81, 41))
        self.toolButton_4.setObjectName("toolButton_4")
        self.toolButton_5 = QtWidgets.QToolButton(Form)
        self.toolButton_5.setGeometry(QtCore.QRect(470, 480, 81, 41))
        self.toolButton_5.setObjectName("toolButton_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.toolButton_4.clicked.connect(self.browsefiles)
        self.toolButton_3.clicked.connect(self.scan)
    def browsefiles(self):
        try:
            fname=QFileDialog.getOpenFileName(self, 
                'Open file', 
                'D:\\', 
                'All files (*)')
            global dump

            with open(fname[0]) as file:
                dump = file.read()
                dump = dump.splitlines()
            # print(dump)
            self.tableWidget.setRowCount(len(dump))
            row = 0
            for ip in dump:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(ip))
                row = row + 1

        except FileNotFoundError as e:
            pass
    def scan(self):
        s = socket.socket()
        try:
            listport = [25,43,80]
            global dump
            row = 0
            for i in dump:
                ip = i.split()[0]
                print(ip)
                res = os.popen(f"ping {ip} -n 2").read()
                if "Request timed out" in res:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem("Down"))
                    # print("down")
                elif "Destination host unreachable" in res:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem("Down"))
                    # print("down")
                else:
                    self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem("Up"))
                    # print("up")
                col = 2
                for p in listport:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = s.connect_ex((ip,p))
                    print(ip)
                    if result == 0:
                        self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem("Open"))
                        # print("Open")
                    else:
                        self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem("Close"))
                        # print("Close")
                    col = col + 1
                    s.close()
                row = row + 1
        except NameError as e:
            pass
        
        # print(dump)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Host"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Status"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "25"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "43"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "80"))
        self.toolButton_3.setText(_translate("Form", "Scan"))
        self.toolButton_4.setText(_translate("Form", "Choose file"))
        self.toolButton_5.setText(_translate("Form", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Table()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
