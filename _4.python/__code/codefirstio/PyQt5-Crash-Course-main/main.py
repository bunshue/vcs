import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("qtcrashcourse2.ui",self)

        # Button
        self.button.clicked.connect(self.buttonclicked)

        # Check Box
        self.checkBox.stateChanged.connect(self.checked)

        # Combo Box
        self.comboBox.setVisible(False)
        listocc=["engineer", "doctor", "manager"]
        for job in listocc:
            self.comboBox.addItem(job)
        self.comboBox.currentIndexChanged.connect(self.combochanged)

        # Spin Box
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(10)
        self.spinBox.valueChanged.connect(self.spinchanged)

    def buttonclicked(self):
        outputstr = self.fname.toPlainText()+ " " + self.lname.toPlainText()
        self.fname.setReadOnly(True)
        self.lname.setReadOnly(True)
        self.fname.setDisabled(True)
        self.lname.setDisabled(True)
        if self.checkBox.isChecked():
            outputstr=outputstr+" is employed"
        else:
            outputstr = outputstr + " is not employed"
        print(outputstr)

    def checked(self):
        if self.checkBox.isChecked():
            self.comboBox.setVisible(True)
        else:
            self.comboBox.setVisible(False)

    def combochanged(self):
        self.outputlabel.setText(self.comboBox.currentText()+" is selected")

    def spinchanged(self):
        print("current value" + str(self.spinBox.value()))




# main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(650)
widget.setFixedWidth(1050)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")