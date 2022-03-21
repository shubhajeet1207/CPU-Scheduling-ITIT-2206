"""
    NAME - SHUBHAJEET PRADHAN
    ROLL NUMBER- 2020IMT-097
    SUBJECT CODE - [ITIT-2206]
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys
from algorithms import *

# initialising arrival time and burst time
n = 0
at = []
bt = []


# creating FCFS interface
class Ui_FCFS_info(object):
    def setupUi(self, FCFS_info):
        FCFS_info.setObjectName("FCFS_info")
        FCFS_info.resize(755, 524)
        self.centralwidget = QtWidgets.QWidget(FCFS_info)
        self.centralwidget.setObjectName("centralwidget")
        self.proc_num = QtWidgets.QLineEdit(self.centralwidget)
        self.proc_num.setGeometry(QtCore.QRect(180, 90, 131, 31))
        self.proc_num.setObjectName("proc_num")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 10, 131, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 131, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 111, 31))
        self.label_3.setObjectName("label_3")
        self.arrival_time = QtWidgets.QLineEdit(self.centralwidget)
        self.arrival_time.setGeometry(QtCore.QRect(180, 220, 141, 31))
        self.arrival_time.setObjectName("arrival_time")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 220, 81, 31))
        self.label_4.setObjectName("label_4")
        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(200, 300, 101, 41))
        self.Generate.setObjectName("Generate")

        self.Generate.clicked.connect(self.add_FCFS)

        self.burst_time = QtWidgets.QLineEdit(self.centralwidget)
        self.burst_time.setGeometry(QtCore.QRect(180, 160, 131, 31))
        self.burst_time.setObjectName("burst_time")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 190, 141, 51))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(442, 109, 191, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 250, 191, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 60, 121, 51))
        self.label_5.setObjectName("label_5")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(360, 0, 20, 491))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        FCFS_info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FCFS_info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 755, 21))
        self.menubar.setObjectName("menubar")
        FCFS_info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FCFS_info)
        self.statusbar.setObjectName("statusbar")
        FCFS_info.setStatusBar(self.statusbar)

        self.retranslateUi(FCFS_info)
        QtCore.QMetaObject.connectSlotsByName(FCFS_info)

    # re-creating UI for user input
    def retranslateUi(self, FCFS_info):
        _translate = QtCore.QCoreApplication.translate
        FCFS_info.setWindowTitle(_translate("FCFS_info", "Shubhajeet Pradhan[2020IMT-097]"))
        self.label.setText(_translate("FCFS_info", "FCFS"))
        self.label_2.setText(_translate("FCFS_info", "Number of processes:"))
        self.label_3.setText(_translate("FCFS_info", "Burst times:"))
        self.label_4.setText(_translate("FCFS_info", "Arrival times:"))
        self.Generate.setText(_translate("FCFS_info", "Generate"))
        self.label_6.setText(_translate("FCFS_info", "Average turn around time:"))
        self.label_5.setText(_translate("FCFS_info", "Average waiting time:"))

    # taking user input
    def add_FCFS(self):
        n = int(self.proc_num.text())
        x = self.arrival_time.text()
        y = self.burst_time.text()

        c = x.split(' ')
        b = y.split(' ')

        for j in c:
            at.append(float(j))
        for i in b:
            bt.append(float(i))
        if (len(at) == n) and (len(bt) == n):
            ATT, AWT = FCFS(n, at, bt)
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
    FCFS_info = QtWidgets.QMainWindow()
    ui = Ui_FCFS_info()
    ui.setupUi(FCFS_info)
    # calling display function
    FCFS_info.show()
    sys.exit(app.exec_())
