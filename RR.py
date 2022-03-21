"""
    NAME - SHUBHAJEET PRADHAN
    ROLL NUMBER- 2020IMT-097
    SUBJECT CODE - [ITIT-2206]
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys
from algorithms import *

# initialising arrival time and burst time and quantum time
n = 0
at = []
bt = []
q = 0


# creating Round Robin interface
class Ui_RR_info(object):
    def setupUi(self, RR_info):
        RR_info.setObjectName("RR_info")
        RR_info.resize(761, 495)
        self.centralwidget = QtWidgets.QWidget(RR_info)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 30, 131, 41))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 240, 81, 31))
        self.label_4.setObjectName("label_4")
        self.burst_time = QtWidgets.QLineEdit(self.centralwidget)
        self.burst_time.setGeometry(QtCore.QRect(210, 180, 131, 31))
        self.burst_time.setObjectName("burst_time")
        self.proc_num = QtWidgets.QLineEdit(self.centralwidget)
        self.proc_num.setGeometry(QtCore.QRect(210, 110, 131, 31))
        self.proc_num.setObjectName("proc_num")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 170, 111, 31))
        self.label_3.setObjectName("label_3")
        self.arrival_time = QtWidgets.QLineEdit(self.centralwidget)
        self.arrival_time.setGeometry(QtCore.QRect(210, 240, 141, 31))
        self.arrival_time.setObjectName("arrival_time")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 131, 41))
        self.label_2.setObjectName("label_2")
        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(230, 390, 101, 41))
        self.Generate.setObjectName("Generate")

        self.Generate.clicked.connect(self.add_RR)

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 320, 71, 31))
        self.label_5.setObjectName("label_5")
        self.quantum = QtWidgets.QLineEdit(self.centralwidget)
        self.quantum.setGeometry(QtCore.QRect(210, 320, 141, 31))
        self.quantum.setObjectName("quantum")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(460, 230, 141, 51))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(482, 149, 191, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(480, 290, 191, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 100, 121, 51))
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 0, 20, 461))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        RR_info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(RR_info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 761, 21))
        self.menubar.setObjectName("menubar")
        RR_info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(RR_info)
        self.statusbar.setObjectName("statusbar")
        RR_info.setStatusBar(self.statusbar)

        self.retranslateUi(RR_info)
        QtCore.QMetaObject.connectSlotsByName(RR_info)

    # re-creating UI for user input
    def retranslateUi(self, RR_info):
        _translate = QtCore.QCoreApplication.translate
        RR_info.setWindowTitle(_translate("RR_info", "Shubhajeet Pradhan[2020IMT-097]"))
        self.label.setText(_translate("RR_info", "Round Robin"))
        self.label_4.setText(_translate("RR_info", "Arrival times:"))
        self.label_3.setText(_translate("RR_info", "Burst times:"))
        self.label_2.setText(_translate("RR_info", "Number of processes:"))
        self.Generate.setText(_translate("RR_info", "Generate"))
        self.label_5.setText(_translate("RR_info", "Quantum:"))
        self.label_6.setText(_translate("RR_info", "Average turn around time:"))
        self.label_7.setText(_translate("RR_info", "Average waiting time:"))

    # taking user input
    def add_RR(self):
        n = int(self.proc_num.text())
        x = self.arrival_time.text()
        y = self.burst_time.text()
        q = int(self.quantum.text())
        c = x.split(' ')
        b = y.split(' ')

        for j in c:
            at.append(float(j))
        for i in b:
            bt.append(float(i))

        if (len(at) == n) and (len(bt) == n):
            AWT, ATT = RR(n, bt, at, q)
            self.lineEdit_2.setText(str(ATT))
            self.lineEdit.setText(str(AWT))
        else:
            msg = QMessageBox()
            msg.setIcon(2)
            msg.setText("Invalid Input")
            msg.setInformativeText("Please enter arrival and burst times same number as processes")
            msg.setWindowTitle("Error")
            msg.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    RR_info = QtWidgets.QMainWindow()
    ui = Ui_RR_info()
    ui.setupUi(RR_info)
    # calling display function
    RR_info.show()
    sys.exit(app.exec_())
