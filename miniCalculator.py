# -*- coding: utf-8 -*-
# Python 3.8.7

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont

displayValue = ''

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(241, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 70, 241, 301))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.dot = QtWidgets.QPushButton(self.frame)
        self.dot.setGeometry(QtCore.QRect(120, 240, 61, 61))
        self.dot.setObjectName("dot")
        self.zero = QtWidgets.QPushButton(self.frame)
        self.zero.setGeometry(QtCore.QRect(0, 240, 121, 61))
        self.zero.setObjectName("zero")
        self.enter = QtWidgets.QPushButton(self.frame)
        self.enter.setGeometry(QtCore.QRect(180, 180, 61, 121))
        self.enter.setObjectName("Enter")
        self.divide = QtWidgets.QPushButton(self.frame)
        self.divide.setGeometry(QtCore.QRect(60, 0, 61, 61))
        self.divide.setObjectName("divide")
        self.multiply = QtWidgets.QPushButton(self.frame)
        self.multiply.setGeometry(QtCore.QRect(120, 0, 61, 61))
        self.multiply.setObjectName("multiply")
        self.minus = QtWidgets.QPushButton(self.frame)
        self.minus.setGeometry(QtCore.QRect(180, 0, 61, 61))
        self.minus.setObjectName("minus")
        self.seven = QtWidgets.QPushButton(self.frame)
        self.seven.setGeometry(QtCore.QRect(0, 60, 61, 61))
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.frame)
        self.eight.setGeometry(QtCore.QRect(60, 60, 61, 61))
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.frame)
        self.nine.setGeometry(QtCore.QRect(120, 60, 61, 61))
        self.nine.setObjectName("nine")
        self.plus = QtWidgets.QPushButton(self.frame)
        self.plus.setGeometry(QtCore.QRect(180, 60, 61, 121))
        self.plus.setObjectName("plus")
        self.four = QtWidgets.QPushButton(self.frame)
        self.four.setGeometry(QtCore.QRect(0, 120, 61, 61))
        self.four.setObjectName("four")
        self.five = QtWidgets.QPushButton(self.frame)
        self.five.setGeometry(QtCore.QRect(60, 120, 61, 61))
        self.five.setObjectName("five")
        self.one = QtWidgets.QPushButton(self.frame)
        self.one.setGeometry(QtCore.QRect(0, 180, 61, 61))
        self.one.setObjectName("one")
        self.two = QtWidgets.QPushButton(self.frame)
        self.two.setGeometry(QtCore.QRect(60, 180, 61, 61))
        self.two.setObjectName("two")
        self.three = QtWidgets.QPushButton(self.frame)
        self.three.setGeometry(QtCore.QRect(120, 180, 61, 61))
        self.three.setObjectName("three")
        self.six = QtWidgets.QPushButton(self.frame)
        self.six.setGeometry(QtCore.QRect(120, 120, 61, 61))
        self.six.setObjectName("six")
        self.clear = QtWidgets.QPushButton(self.frame)
        self.clear.setGeometry(QtCore.QRect(0, 0, 61, 61))
        self.clear.setObjectName("clear")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 241, 71))
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter) # Align H Right, V Center
        self.label.setFont(QFont('Times', 32))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # clicking all numbers
        self.zero.clicked.connect(lambda: self.clicked(0))
        self.one.clicked.connect(lambda: self.clicked(1))
        self.two.clicked.connect(lambda: self.clicked(2))
        self.three.clicked.connect(lambda: self.clicked(3))
        self.four.clicked.connect(lambda: self.clicked(4))
        self.five.clicked.connect(lambda: self.clicked(5))
        self.six.clicked.connect(lambda: self.clicked(6))
        self.seven.clicked.connect(lambda: self.clicked(7))
        self.eight.clicked.connect(lambda: self.clicked(8))
        self.nine.clicked.connect(lambda: self.clicked(9))
        
        # all other buttons
        self.plus.clicked.connect(lambda: self.clicked('+'))
        self.minus.clicked.connect(lambda: self.clicked('-'))
        self.multiply.clicked.connect(lambda: self.clicked('*'))
        self.divide.clicked.connect(lambda: self.clicked('/'))
        self.dot.clicked.connect(lambda: self.clicked('.'))
        self.clear.clicked.connect(lambda: self.clicked('clear'))
        self.enter.clicked.connect(lambda: self.clicked('enter'))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.dot.setText(_translate("MainWindow", "."))
        self.dot.setShortcut(_translate("MainWindow", "."))
        self.zero.setText(_translate("MainWindow", "0"))
        self.zero.setShortcut(_translate("MainWindow", "0"))
        self.enter.setText(_translate("MainWindow", "Enter"))
        self.enter.setShortcut(_translate("MainWindow", "Return"))
        self.divide.setText(_translate("MainWindow", "/"))
        self.divide.setShortcut(_translate("MainWindow", "/"))
        self.multiply.setText(_translate("MainWindow", "*"))
        self.multiply.setShortcut(_translate("MainWindow", "*"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.minus.setShortcut(_translate("MainWindow", "-"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.seven.setShortcut(_translate("MainWindow", "7"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.eight.setShortcut(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.nine.setShortcut(_translate("MainWindow", "9"))
        self.plus.setText(_translate("MainWindow", "+"))
        self.plus.setShortcut(_translate("MainWindow", "+"))
        self.four.setText(_translate("MainWindow", "4"))
        self.four.setShortcut(_translate("MainWindow", "4"))
        self.five.setText(_translate("MainWindow", "5"))
        self.five.setShortcut(_translate("MainWindow", "5"))
        self.one.setText(_translate("MainWindow", "1"))
        self.one.setShortcut(_translate("MainWindow", "1"))
        self.two.setText(_translate("MainWindow", "2"))
        self.two.setShortcut(_translate("MainWindow", "2"))
        self.three.setText(_translate("MainWindow", "3"))
        self.three.setShortcut(_translate("MainWindow", "3"))
        self.six.setText(_translate("MainWindow", "6"))
        self.six.setShortcut(_translate("MainWindow", "6"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.clear.setShortcut(_translate("MainWindow", "Backspace"))

    def clicked(self, i):

        global displayValue

        # if i == clear, clear.
        if i == 'clear':
            displayValue = ''
        
        elif i == 'enter':
            if displayValue.endswith('+') or displayValue.endswith('-') or displayValue.endswith('*') or displayValue.endswith('/'):
                return
            dvsum = eval(displayValue)
            displayValue = str(dvsum)

        else:
            displayValue += str(i)

        # show it on screen, and if it's too long, make it shorter
        if len(displayValue) >= 10:
            print(len(displayValue))
            displayValue = displayValue[0:10]
        self.label.setText(displayValue)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
