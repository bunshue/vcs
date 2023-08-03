import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("addimagetutorial.ui",self)
        self.button.clicked.connect(self.addimage)


    def addimage(self):
        #Add the image
        qpixmap = QPixmap('pythonlogo.png')
        self.imglabel.setPixmap(qpixmap)


# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(430)
widget.setFixedWidth(765)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
