"""
    NAME - SHUBHAJEET PRADHAN
    ROLL NUMBER- 2020IMT-097
    SUBJECT CODE - [ITIT-2206]
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from FCFS import Ui_FCFS_info
from SJF import Ui_SJF_preem_info
from SJF_non import Ui_SJF_non_info
from RR import Ui_RR_info
from priority import Ui_priority_preem_info
from priority_non import Ui_priority_non_info


# the following functions is called based on user choice for a scheduling type
class choice_popup(object):

    # each function will pop-up a new window to ask the user for further information depends on the scheduler type
    def open_FCFS_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FCFS_info()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_SJF_preem_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SJF_preem_info()
        self.ui.setupUi(self.window)
        # first.hide()
        self.window.show()

    def open_SJF_non_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SJF_non_info()
        self.ui.setupUi(self.window)
        # first.hide()
        self.window.show()

    def open_RR_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_RR_info()
        self.ui.setupUi(self.window)
        # first.hide()
        self.window.show()

    def open_Priority_preem_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_priority_preem_info()
        self.ui.setupUi(self.window)
        # first.hide()
        self.window.show()

    def open_Priority_non_info(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_priority_non_info()
        self.ui.setupUi(self.window)
        # first.hide()
        self.window.show()

    def setupUi(self, first):
        first.setObjectName("first")
        first.resize(520, 485)
        self.centralwidget = QtWidgets.QWidget(first)
        self.centralwidget.setObjectName("centralwidget")
        self.FCFS_but = QtWidgets.QPushButton(self.centralwidget)
        self.FCFS_but.setGeometry(QtCore.QRect(140, 50, 121, 31))
        self.FCFS_but.setObjectName("FCFS_but")

        self.FCFS_but.clicked.connect(self.open_FCFS_info)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 111, 41))
        self.label.setObjectName("label")
        self.SJFpreem_but = QtWidgets.QPushButton(self.centralwidget)
        self.SJFpreem_but.setGeometry(QtCore.QRect(140, 100, 121, 31))
        self.SJFpreem_but.setObjectName("SJFpreem_but")

        self.SJFpreem_but.clicked.connect(self.open_SJF_preem_info)

        self.SJFnon_but = QtWidgets.QPushButton(self.centralwidget)
        self.SJFnon_but.setGeometry(QtCore.QRect(140, 150, 121, 31))
        self.SJFnon_but.setObjectName("SJFnon_but")

        self.SJFnon_but.clicked.connect(self.open_SJF_non_info)

        self.RR_but = QtWidgets.QPushButton(self.centralwidget)
        self.RR_but.setGeometry(QtCore.QRect(140, 200, 121, 31))
        self.RR_but.setObjectName("RR_but")

        self.RR_but.clicked.connect(self.open_RR_info)

        self.Prioritypreem_but = QtWidgets.QPushButton(self.centralwidget)
        self.Prioritypreem_but.setGeometry(QtCore.QRect(140, 250, 121, 31))
        self.Prioritypreem_but.setObjectName("Prioritypreem_but")

        self.Prioritypreem_but.clicked.connect(self.open_Priority_preem_info)

        self.Prioritynon_but = QtWidgets.QPushButton(self.centralwidget)
        self.Prioritynon_but.setGeometry(QtCore.QRect(140, 300, 121, 31))
        self.Prioritynon_but.setObjectName("Prioritynon_but")

        self.Prioritynon_but.clicked.connect(self.open_Priority_non_info)

        first.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(first)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setObjectName("menubar")
        first.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(first)
        self.statusbar.setObjectName("statusbar")
        first.setStatusBar(self.statusbar)

        self.retranslateUi(first)
        QtCore.QMetaObject.connectSlotsByName(first)

    def retranslateUi(self, first):
        _translate = QtCore.QCoreApplication.translate
        first.setWindowTitle(_translate("first", "Shubhajeet Pradhan[2020IMT-097]"))
        self.FCFS_but.setText(_translate("first", "FCFS"))
        self.label.setText(_translate("first", "Scheduling type:"))
        self.SJFpreem_but.setText(_translate("first", "SJF(P)"))
        self.SJFnon_but.setText(_translate("first", "SJF(NP)"))
        self.RR_but.setText(_translate("first", "Round Robin"))
        self.Prioritypreem_but.setText(_translate("first", "Priority(P)"))
        self.Prioritynon_but.setText(_translate("first", "Priority(NP)"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    first = QtWidgets.QMainWindow()
    ui = choice_popup()
    ui.setupUi(first)
    first.show()
    sys.exit(app.exec_())
