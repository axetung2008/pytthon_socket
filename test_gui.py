from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
def __init__(self, inMsg=' Loading...', inMaxStep=1):
        """
        """
        # Save reference to the QGIS interface
        # initialize progressBar
        # QApplication.processEvents() # Help to keep UI alive
        self.iface = iface

        widget = iface.messageBar().createMessage('Please wait  ', inMsg)

        prgBar = QProgressBar()
        self.prgBar = prgBar

        widget.layout().addWidget(self.prgBar)
        iface.messageBar().pushWidget(widget)
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

        # if Max 0 and value 0, no progressBar, only cursor loading
        # default is set to 0
        prgBar.setValue(1)
        # set Maximum for progressBar
        prgBar.setMaximum(inMaxStep) 