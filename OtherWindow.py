from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import re
import os
import getpass


largest_6_sizes = [0,0,0,0,0,0]
largest_6_names = ['','','','','','']

def get_subitems(parent_path, n, pyqt_child, l):

    start = parent_path.find("!") +1
    end = parent_path.find("@")
    parent_lvl = parent_path[start:end]

    if int(parent_lvl) > l:
        return

    child_lvl = str(int(parent_lvl) + 1)
    child_path = parent_path.replace('!' + parent_lvl + '@', '!' + child_lvl + '@')

    print (child_path)

    found = False
    with open("dir.txt") as f:
        for line in f:
            if child_path in line:
                found = True

                start = line.find("#") +1
                end = line.find("$")
                subitem_name = line[start:end]

                start = line.find("$") +1
                end = line.find("^")
                subitem_size = line[start:end]
                if int(subitem_size) < 0:
                    subitem_size = str(int(subitem_size)*-1)
                subitem_size = str(float(subitem_size)/1024)

                l2_child = QtWidgets.QTreeWidgetItem([str(subitem_name), str(subitem_size)])
                pyqt_child.addChild(l2_child)

                start = line.find("!")
                end = line.find("#")
                sub_child_path = line[start:end]


                get_subitems(sub_child_path, n, l2_child, l)

        if not found:
            return

class Ui_OtherWindow(object):
    def setupUi(self, MainWindow, address, address_line, l):
        MainWindow.setObjectName("Disk Info")
        MainWindow.resize(996, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 551))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.treeWidget = QtWidgets.QTreeWidget(self.horizontalLayoutWidget)
        self.treeWidget.setObjectName("treeWidget")



        self.horizontalLayout_3.addWidget(self.treeWidget)

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(490, 0, 501, 551))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 996, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(MainWindow, address, address_line, l)
        self.create_piechart()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, address, address_line, l):

        pattern = '!(.*)@'
        coming_lvl = re.search(pattern, address_line).group(1)

        coming_lvl = str(int(coming_lvl) + 1)
        first_lvl_path = '!' + coming_lvl + address.rstrip('#')


        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("Disk Info", "Disk Info"))


        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Item"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Size in KB"))

        __sortingEnabled = self.treeWidget.isSortingEnabled()

        self.treeWidget.setSortingEnabled(False)

        n=-1

        with open("dir.txt") as f:
            contents = f.read()
            number_of_items = contents.count(first_lvl_path)


        self.total_size = 1.0
        with open("dir.txt") as f:
            for line in f:
                if address in line:
                    start = line.find("$") +1
                    end = line.find("^")
                    self.total_size = line[start:end]
                    self.total_size = str(int(self.total_size)/-1024)


                if first_lvl_path in line:
                    start = line.find("#") +1
                    end = line.find("$")
                    item_name = line[start:end]

                    start = line.find("$") +1
                    end = line.find("^")
                    item_size = line[start:end]
                    if int(item_size) < 0:
                        item_size = str(int(item_size)*-1)
                    item_size = str(int(item_size)/1024)

                    for i in range(0, 6):
                        if  float(item_size) == largest_6_sizes[i]:
                            break
                        if  float(item_size) > largest_6_sizes[i]:
                            largest_6_sizes[i] = float(item_size)
                            largest_6_names[i] = item_name
                            break


                    n = n + 1
                    item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
                    self.treeWidget.topLevelItem(n).setText(0, _translate("MainWindow", item_name))
                    self.treeWidget.topLevelItem(n).setText(1, _translate("MainWindow", item_size))

                    start = line.find("!")
                    end = line.find("#")
                    item_path = line[start:end]

                    get_subitems(item_path, n, self.treeWidget.topLevelItem(n), l)

        self.treeWidget.setSortingEnabled(__sortingEnabled)


    def create_piechart(self):

        series = QPieSeries()

        if float(self.total_size) == -0.0:
            self.total_size = 1

        for x in range(3):
            series.append(largest_6_names[x], largest_6_sizes[x]/float(self.total_size))

        others_size = float(self.total_size) - (largest_6_sizes[0] + largest_6_sizes[1] + largest_6_sizes[2])
        series.append("Others", others_size/float(self.total_size))

        #adding slice
        slice = QPieSlice()
        slice = series.slices()[2]
        slice.setExploded(True)
        slice.setLabelVisible(True)
        slice.setPen(QPen(Qt.darkGreen, 2))
        slice.setBrush(Qt.green)

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Disk Pie Chart")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.gridLayout.addWidget(chartview)

if __name__ == "__main__":
    import sys



    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()

    username = getpass.getuser()
    home_add = '@//home/' + username + '#'
    disk_add = '@/#'

    with open("dir.txt") as f:
        for num, line in enumerate(f, 1):
            if home_add in line:
                start = line.find(home_add) + len(home_add.encode())
                end = line.find("$")
                disk1_name = line[start:end]
                home_add_line = line

    l=5
    ui.setupUi(MainWindow, home_add, home_add_line, l)
    MainWindow.show()
    ui.create_piechart()
    sys.exit(app.exec_())
