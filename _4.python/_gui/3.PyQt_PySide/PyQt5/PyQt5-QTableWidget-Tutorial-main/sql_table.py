import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("tabletutorial.ui",self)
        self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setHorizontalHeaderLabels(["City","Country","Subcountry"])
        self.loaddata()

    def loaddata(self):
        self.tableWidget.setRowCount(10)#設定Table一頁的長度
        
        tablerow = 0
        data1, data2, data3 = "aaaa0", "bbb0", "ccc0"
        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(data1))
        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(data2))
        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(data3))

        tablerow = 1
        data1, data2, data3 = "aaaa1", "bbb1", "ccc1"
        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(data1))
        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(data2))
        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(data3))

        tablerow = 2
        data1, data2, data3 = "aaaa2", "bbb2", "ccc2"
        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(data1))
        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(data2))
        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(data3))

        tablerow = 3
        data1, data2, data3 = "aaaa3", "bbb3", "ccc3"
        self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(data1))
        self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(data2))
        self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(data3))

# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
