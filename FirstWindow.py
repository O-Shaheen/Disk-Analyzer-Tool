from PyQt5 import QtCore, QtGui, QtWidgets
from OtherWindow import Ui_OtherWindow
import mmap
import getpass



username = getpass.getuser()
home_add = '@//home/' + username + '#'
disk1_add = '@/#'
disk2_add = '@//dev/sda1#'
disk3_add = '@//dev/nvme0n1p3#'

with open("dir.txt") as f:
    for num, line in enumerate(f, 1):
        if home_add in line:
            start = line.find(home_add) + len(home_add.encode())
            end = line.find("$")
            home_name = line[start:end]
            home_add_line = line

        if disk1_add in line:
            start = line.find(disk1_add) + len(disk1_add.encode())
            end = line.find("$")
            disk1_name = line[start:end]
            disk1_add_line = line

        if disk2_add in line:
            start = line.find(disk2_add) + len(disk2_add.encode())
            end = line.find("$")
            disk2_name = line[start:end]
            disk2_add_line = line

        if disk3_add in line:
            start = line.find(disk3_add) + len(disk3_add.encode())
            end = line.find("$")
            disk3_name = line[start:end]
            disk3_add_line = line

address = home_add
address_line = home_add_line

class Ui_MainWindow(object):
    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        address = home_add
        address_line = home_add_line
        l=5
        self.ui.setupUi(self.window, address, address_line, l)
        self.window.show()

    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        address = disk1_add
        address_line = disk1_add_line
        l=2
        self.ui.setupUi(self.window, address, address_line, l)
        self.window.show()

    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        address = disk2_add
        address_line = disk2_add_line
        l=1
        self.ui.setupUi(self.window, address, address_line, l)
        self.window.show()

    def openWindow4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        address = disk3_add
        address_line = disk3_add_line
        l=1
        self.ui.setupUi(self.window, address, address_line, l)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(996, 600)
        MainWindow.setAutoFillBackground(True)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 991, 31))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.label.setObjectName("label")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(140, 80, 711, 381))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")

        self.button1 = QtWidgets.QPushButton(self.groupBox)
        self.button1.setGeometry(QtCore.QRect(0, 20, 711, 91))
        self.button1.setObjectName("button1")
        self.button1.setIcon(QtGui.QIcon("disk.png"))
        self.button1.setIconSize(QtCore.QSize(60, 60))
        self.button1.clicked.connect(self.openWindow1)

        self.button2 = QtWidgets.QPushButton(self.groupBox)
        self.button2.setGeometry(QtCore.QRect(0, 110, 711, 91))
        self.button2.setObjectName("button2")
        self.button2.setIcon(QtGui.QIcon("disk.png"))
        self.button2.setIconSize(QtCore.QSize(60, 60))
        self.button2.clicked.connect(self.openWindow2)

        self.button3 = QtWidgets.QPushButton(self.groupBox)
        self.button3.setGeometry(QtCore.QRect(0, 200, 711, 91))
        self.button3.setObjectName("button3")
        self.button3.setIcon(QtGui.QIcon("disk.png"))
        self.button3.setIconSize(QtCore.QSize(60, 60))
        self.button3.clicked.connect(self.openWindow3)

        self.button4 = QtWidgets.QPushButton(self.groupBox)
        self.button4.setGeometry(QtCore.QRect(0, 290, 711, 91))
        self.button4.setObjectName("button4")
        self.button4.setIcon(QtGui.QIcon("disk.png"))
        self.button4.setIconSize(QtCore.QSize(60, 60))
        self.button4.clicked.connect(self.openWindow4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Available Disks</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "This Computer"))



        self.button1.setText(_translate("MainWindow", home_name))
        self.button2.setText(_translate("MainWindow", disk1_name))
        self.button3.setText(_translate("MainWindow", "DATA"))
        self.button4.setText(_translate("MainWindow", "Windows"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
