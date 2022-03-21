"""
    NAME - SHUBHAJEET PRADHAN
    ROLL NUMBER- 2020IMT-097
    SUBJECT CODE - [ITIT-2206]
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import sys
from algorithms import *

# initialising arrival time and burst time and priority
n = 0
at = []
bt = []
pr = []


# creating Priority(Preemptive) interface
class Ui_priority_preem_info(object):
    def setupUi(self, priority_preem_info):
        priority_preem_info.setObjectName("priority_preem_info")
        priority_preem_info.resize(772, 494)
        self.centralwidget = QtWidgets.QWidget(priority_preem_info)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 40, 131, 41))
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 250, 81, 31))
        self.label_4.setObjectName("label_4")
        self.burst_time = QtWidgets.QLineEdit(self.centralwidget)
        self.burst_time.setGeometry(QtCore.QRect(180, 190, 131, 31))
        self.burst_time.setObjectName("burst_time")
        self.proc_num = QtWidgets.QLineEdit(self.centralwidget)
        self.proc_num.setGeometry(QtCore.QRect(180, 120, 131, 31))
        self.proc_num.setObjectName("proc_num")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 111, 31))
        self.label_3.setObjectName("label_3")
        self.arrival_time = QtWidgets.QLineEdit(self.centralwidget)
        self.arrival_time.setGeometry(QtCore.QRect(180, 250, 141, 31))
        self.arrival_time.setObjectName("arrival_time")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 120, 131, 41))
        self.label_2.setObjectName("label_2")
        self.Generate = QtWidgets.QPushButton(self.centralwidget)
        self.Generate.setGeometry(QtCore.QRect(200, 380, 101, 41))
        self.Generate.setObjectName("Generate")
        self.Generate.clicked.connect(self.add_priority_preem)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 310, 91, 31))
        self.label_5.setObjectName("label_5")
        self.priority = QtWidgets.QLineEdit(self.centralwidget)
        self.priority.setGeometry(QtCore.QRect(180, 310, 141, 31))
        self.priority.setObjectName("priority")
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
        self.line.setGeometry(QtCore.QRect(380, 10, 20, 451))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        priority_preem_info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(priority_preem_info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 772, 21))
        self.menubar.setObjectName("menubar")
        priority_preem_info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(priority_preem_info)
        self.statusbar.setObjectName("statusbar")
        priority_preem_info.setStatusBar(self.statusbar)
        self.retranslateUi(priority_preem_info)
        QtCore.QMetaObject.connectSlotsByName(priority_preem_info)

    # re-creating UI for user input
    def retranslateUi(self, priority_preem_info):
        _translate = QtCore.QCoreApplication.translate
        priority_preem_info.setWindowTitle(_translate("priority_preem_info", "Shubhajeet Pradhan[2020IMT-097]"))
        self.label.setText(_translate("priority_preem_info", "Priority Preemptive"))
        self.label_4.setText(_translate("priority_preem_info", "Arrival times:"))
        self.label_3.setText(_translate("priority_preem_info", "Burst times:"))
        self.label_2.setText(_translate("priority_preem_info", "Number of processes:"))
        self.Generate.setText(_translate("priority_preem_info", "Generate"))
        self.label_5.setText(_translate("priority_preem_info", "Priority numbers:"))
        self.label_6.setText(_translate("priority_preem_info", "Average turn around time:"))
        self.label_7.setText(_translate("priority_preem_info", "Average waiting time:"))

    # taking user input
    def add_priority_preem(self):
        n = int(self.proc_num.text())
        x = self.arrival_time.text()
        y = self.burst_time.text()
        z = self.priority.text()
        c = x.split(' ')
        b = y.split(' ')
        p = z.split(' ')
        for j in c:
            at.append(float(j))
        for i in b:
            bt.append(float(i))
        for i in p:
            pr.append(float(i))
        if (len(at) == n) and (len(bt) == n) and (len(pr) == n):
            AWT, ATT = priority_preem(n, bt, at, pr)
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
    priority_preem_info = QtWidgets.QMainWindow()
    ui = Ui_priority_preem_info()
    ui.setupUi(priority_preem_info)
    # calling display function
    priority_preem_info.show()
    sys.exit(app.exec_())
