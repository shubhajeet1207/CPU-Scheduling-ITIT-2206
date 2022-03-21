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


# creating SRTF interface
class Ui_SJF_preem_info(object):
    def setupUi(self, SJF_preem_info):
        SJF_preem_info.setObjectName("SJF_preem_info")
        SJF_preem_info.resize(726, 536)
        self.centralwidget = QtWidgets.QWidget(SJF_preem_info)
        self.centralwidget.setObjectName("centralwidget")
        self.proc_num = QtWidgets.QLineEdit(self.centralwidget)
        self.proc_num.setGeometry(QtCore.QRect(210, 140, 131, 31))
        self.proc_num.setObjectName("proc_num")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 200, 111, 31))
        self.label_3.setObjectName("label_3")
        self.arrival_time = QtWidgets.QLineEdit(self.centralwidget)
        self.arrival_time.setGeometry(QtCore.QRect(210, 270, 141, 31))
        self.arrival_time.setObjectName("arrival_time")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 270, 81, 31))
        self.label_4.setObjectName("label_4")
        self.burst_time = QtWidgets.QLineEdit(self.centralwidget)
        self.burst_time.setGeometry(QtCore.QRect(210, 210, 131, 31))
        self.burst_time.setObjectName("burst_time")
        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(230, 350, 101, 41))
        self.Generate.setObjectName("Generate")

        self.Generate.clicked.connect(self.add_SJF_preem)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 60, 131, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 131, 41))
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(380, 0, 20, 501))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(420, 210, 141, 51))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(442, 129, 191, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(440, 270, 191, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(420, 80, 121, 51))
        self.label_5.setObjectName("label_5")
        SJF_preem_info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SJF_preem_info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 726, 21))
        self.menubar.setObjectName("menubar")
        SJF_preem_info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SJF_preem_info)
        self.statusbar.setObjectName("statusbar")
        SJF_preem_info.setStatusBar(self.statusbar)

        self.retranslateUi(SJF_preem_info)
        QtCore.QMetaObject.connectSlotsByName(SJF_preem_info)

    # re-creating UI for user input
    def retranslateUi(self, SJF_preem_info):
        _translate = QtCore.QCoreApplication.translate
        SJF_preem_info.setWindowTitle(_translate("SJF_preem_info", "Shubhajeet Pradhan[2020IMT-097]"))
        self.label_3.setText(_translate("SJF_preem_info", "Burst times:"))
        self.label_4.setText(_translate("SJF_preem_info", "Arrival times:"))
        self.Generate.setText(_translate("SJF_preem_info", "Generate"))
        self.label.setText(_translate("SJF_preem_info", "SJF Preemptive"))
        self.label_2.setText(_translate("SJF_preem_info", "Number of processes:"))
        self.label_6.setText(_translate("SJF_preem_info", "Average turn around time:"))
        self.label_5.setText(_translate("SJF_preem_info", "Average waiting time:"))

    # taking user input
    def add_SJF_preem(self):
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
            ATT, AWT = SJFpreem(n, bt, at)
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
    SJF_preem_info = QtWidgets.QMainWindow()
    ui = Ui_SJF_preem_info()
    ui.setupUi(SJF_preem_info)
    # calling display function
    SJF_preem_info.show()
    sys.exit(app.exec_())
