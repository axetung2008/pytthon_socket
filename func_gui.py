

168.138.53.103
80



#on setupui===============================
self.toolButton.clicked.connect(self.scan)
        self.toolButton_2.clicked.connect(self.connect)
        
        self.lineEdit_3.returnPressed.connect(self.submit)
        self.toolButton_3.clicked.connect(self.disconnect)

    #============================================

    def connect(self):
        try:

            global s 
            s = socket.socket()

            ip = self.lineEdit.text()
            port = int(self.lineEdit_2.text())

            s.connect((ip,port))
            self.lineEdit_3.setEnabled(True)
            self.toolButton_3.setEnabled(True)
            self.textEdit.append("Connection success!")
            self.toolButton_2.setEnabled(False)
            
        except ConnectionRefusedError as e:
            self.textEdit.append("No connection!")
        except ValueError as e:
            self.textEdit.append("Please type IP address and port!")

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

    def disconnect(self):
        s.send(bytes("disconnect","utf-8"))
        from_server = s.recv(2048)
        self.textEdit.append(from_server.decode())
        s.close()
        self.lineEdit_3.setEnabled(False)
        self.toolButton_3.setEnabled(False)
        self.toolButton_2.setEnabled(True)
        pass