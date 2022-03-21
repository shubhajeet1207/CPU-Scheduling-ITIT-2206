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


# creating SJF interface
class Ui_SJF_non_info(object):

    def setupUi(self, SJF_non):
        SJF_non.setObjectName("SJF_non")
        SJF_non.resize(724, 549)
        self.centralwidget = QtWidgets.QWidget(SJF_non)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 100, 131, 41))
        self.label_2.setObjectName("label_2")
        self.proc_num = QtWidgets.QLineEdit(self.centralwidget)
        self.proc_num.setGeometry(QtCore.QRect(190, 100, 131, 31))
        self.proc_num.setObjectName("proc_num")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 230, 81, 31))
        self.label_4.setObjectName("label_4")
        self.arrival_time = QtWidgets.QLineEdit(self.centralwidget)
        self.arrival_time.setGeometry(QtCore.QRect(190, 230, 141, 31))
        self.arrival_time.setObjectName("arrival_time")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 160, 111, 31))
        self.label_3.setObjectName("label_3")
        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(210, 310, 101, 41))
        self.Generate.setObjectName("Generate")

        self.Generate.clicked.connect(self.add_SJF_non)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 131, 41))
        self.label.setObjectName("label")
        self.burst_time = QtWidgets.QLineEdit(self.centralwidget)
        self.burst_time.setGeometry(QtCore.QRect(190, 170, 131, 31))
        self.burst_time.setObjectName("burst_time")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(350, 0, 20, 521))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 80, 121, 51))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(400, 210, 141, 51))
        self.label_6.setObjectName("label_6")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(422, 129, 191, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 270, 191, 51))
        self.lineEdit_2.setObjectName("lineEdit_2")
        SJF_non.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SJF_non)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 724, 21))
        self.menubar.setObjectName("menubar")
        SJF_non.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SJF_non)
        self.statusbar.setObjectName("statusbar")
        SJF_non.setStatusBar(self.statusbar)

        self.recreateUI(SJF_non)
        QtCore.QMetaObject.connectSlotsByName(SJF_non)

    # re-creating UI for user input
    def recreateUI(self, SJF_non):
        _translate = QtCore.QCoreApplication.translate
        SJF_non.setWindowTitle(_translate("SJF_non", "Shubhajeet Pradhan[2020IMT-097]"))
        self.label_2.setText(_translate("SJF_non", "Number of processes:"))
        self.label_4.setText(_translate("SJF_non", "Arrival times:"))
        self.label_3.setText(_translate("SJF_non", "Burst times:"))
        self.Generate.setText(_translate("SJF_non", "Generate"))
        self.label.setText(_translate("SJF_non", "SJF Non Preemptive"))
        self.label_5.setText(_translate("SJF_non", "Average waiting time:"))
        self.label_6.setText(_translate("SJF_non", "Average turn around time:"))

    # taking user input
    def add_SJF_non(self):
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
            ATT, AWT = SJF_nonpreem(n, bt, at)
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
    SJF_non = QtWidgets.QMainWindow()
    ui = Ui_SJF_non_info()
    ui.setupUi(SJF_non)
    # calling display function
    SJF_non.show()
    sys.exit(app.exec_())
