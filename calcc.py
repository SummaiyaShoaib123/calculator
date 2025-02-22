


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(346, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.outputlabel = QtWidgets.QLabel(self.centralwidget)
        self.outputlabel.setGeometry(QtCore.QRect(10, 10, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.outputlabel.setFont(font)
        self.outputlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputlabel.setObjectName("outputlabel")
        self.percentbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("%"))
        self.percentbutton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.percentbutton.setFont(font)
        self.percentbutton.setObjectName("percentbutton")
        self.Cbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("C"))
        self.Cbutton.setGeometry(QtCore.QRect(90, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Cbutton.setFont(font)
        self.Cbutton.setObjectName("Cbutton")
        self.arrowbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("<<"))
        self.arrowbutton.setGeometry(QtCore.QRect(170, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.arrowbutton.setFont(font)
        self.arrowbutton.setObjectName("arrowbutton")
        self.dividebutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("/"))
        self.dividebutton.setGeometry(QtCore.QRect(250, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.dividebutton.setFont(font)
        self.dividebutton.setObjectName("dividebutton")
        self.sevenbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("7"))
        self.sevenbutton.setGeometry(QtCore.QRect(10, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.sevenbutton.setFont(font)
        self.sevenbutton.setObjectName("sevenbutton")
        self.fourbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("4"))
        self.fourbutton.setGeometry(QtCore.QRect(10, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.fourbutton.setFont(font)
        self.fourbutton.setObjectName("fourbutton")
        self.onebutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("1"))
        self.onebutton.setGeometry(QtCore.QRect(10, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.onebutton.setFont(font)
        self.onebutton.setObjectName("onebutton")
        self.plusminusbutton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda:self.press_it("+/-"))
        self.plusminusbutton.setGeometry(QtCore.QRect(10, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusminusbutton.setFont(font)
        self.plusminusbutton.setObjectName("plusminusbutton")
        self.eightbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("8"))
        self.eightbutton.setGeometry(QtCore.QRect(90, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.eightbutton.setFont(font)
        self.eightbutton.setObjectName("eightbutton")
        self.fivebutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("5"))
        self.fivebutton.setGeometry(QtCore.QRect(90, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.fivebutton.setFont(font)
        self.fivebutton.setObjectName("fivebutton")
        self.twobutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("2"))
        self.twobutton.setGeometry(QtCore.QRect(90, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.twobutton.setFont(font)
        self.twobutton.setObjectName("twobutton")
        self.zerobutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("0"))
        self.zerobutton.setGeometry(QtCore.QRect(90, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.zerobutton.setFont(font)
        self.zerobutton.setObjectName("zerobutton")
        self.ninebutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("9"))
        self.ninebutton.setGeometry(QtCore.QRect(170, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.ninebutton.setFont(font)
        self.ninebutton.setObjectName("ninebutton")
        self.sixbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("6"))
        self.sixbutton.setGeometry(QtCore.QRect(170, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.sixbutton.setFont(font)
        self.sixbutton.setObjectName("sixbutton")
        self.threebutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("3"))
        self.threebutton.setGeometry(QtCore.QRect(170, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.threebutton.setFont(font)
        self.threebutton.setObjectName("threebutton")
        self.decimalbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.dot_it())
        self.decimalbutton.setGeometry(QtCore.QRect(170, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.decimalbutton.setFont(font)
        self.decimalbutton.setObjectName("decimalbutton")
        self.multiplybutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("x"))
        self.multiplybutton.setGeometry(QtCore.QRect(250, 190, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.multiplybutton.setFont(font)
        self.multiplybutton.setObjectName("multiplybutton")
        self.minusbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("-"))
        self.minusbutton.setGeometry(QtCore.QRect(250, 270, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.minusbutton.setFont(font)
        self.minusbutton.setObjectName("minusbutton")
        self.plusbutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("+"))
        self.plusbutton.setGeometry(QtCore.QRect(250, 350, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.plusbutton.setFont(font)
        self.plusbutton.setObjectName("plusbutton")
        self.equaltobutton = QtWidgets.QPushButton(self.centralwidget,clicked = lambda:self.press_it("="))
        self.equaltobutton.setGeometry(QtCore.QRect(250, 430, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.equaltobutton.setFont(font)
        self.equaltobutton.setObjectName("equaltobutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 346, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def dot_it(self):
        screen = self.outputlabel.text()
        # Check if the last character is already a decimal point
        if '.' not in screen:
            
             self.outputlabel.setText(f'{screen}.')
    
    


    def press_it(self, pressed):
        if pressed == "C":
            self.outputlabel.setText("0")
        else:
            if self.outputlabel.text()=="0":
                self.outputlabel.setText("")
            self.outputlabel.setText(f'{self.outputlabel.text()}{pressed}')
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.outputlabel.setText(_translate("MainWindow", "0"))
        self.percentbutton.setText(_translate("MainWindow", "%"))
        self.Cbutton.setText(_translate("MainWindow", "C"))
        self.arrowbutton.setText(_translate("MainWindow", "<<"))
        self.dividebutton.setText(_translate("MainWindow", "/"))
        self.sevenbutton.setText(_translate("MainWindow", "7"))
        self.fourbutton.setText(_translate("MainWindow", "4"))
        self.onebutton.setText(_translate("MainWindow", "1"))
        self.plusminusbutton.setText(_translate("MainWindow", "+/-"))
        self.eightbutton.setText(_translate("MainWindow", "8"))
        self.fivebutton.setText(_translate("MainWindow", "5"))
        self.twobutton.setText(_translate("MainWindow", "2"))
        self.zerobutton.setText(_translate("MainWindow", "0"))
        self.ninebutton.setText(_translate("MainWindow", "9"))
        self.sixbutton.setText(_translate("MainWindow", "6"))
        self.threebutton.setText(_translate("MainWindow", "3"))
        self.decimalbutton.setText(_translate("MainWindow", "."))
        self.multiplybutton.setText(_translate("MainWindow", "x"))
        self.minusbutton.setText(_translate("MainWindow", "-"))
        self.plusbutton.setText(_translate("MainWindow", "+"))
        self.equaltobutton.setText(_translate("MainWindow", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
