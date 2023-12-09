from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 263)

        # Create QMainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Create a QMenuBar
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menuBar)

        # Add a menu to the menuBar
        self.menuPrograms = QtWidgets.QMenu(self.menuBar)
        self.menuPrograms.setObjectName("menuPrograms")
        self.menuBar.addAction(self.menuPrograms.menuAction())

        # Add actions to the menu
        self.actionAddGoodProgram = QtWidgets.QAction(MainWindow)
        self.actionAddGoodProgram.setObjectName("lisaheaprogramm")

        self.actionAddBadProgram = QtWidgets.QAction(MainWindow)
        self.actionAddBadProgram.setObjectName("lisahalbprogramm")
        self.actionAddBadProgram.triggered.connect(self.halb_valitud)

        # Add actions to the menuPrograms menu
        self.menuPrograms.addAction(self.actionAddGoodProgram)
        self.menuPrograms.addAction(self.actionAddBadProgram)

        self.actionAddGoodProgram.triggered.connect(self.hea_valitud)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 60, 71, 81))
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 170, 71, 81))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 60, 71, 81))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 170, 71, 81))
        self.pushButton_5.setObjectName("pushButton_5")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 40, 111, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 150, 121, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Distracto"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "+"))
        self.pushButton_4.setText(_translate("MainWindow", "+"))
        self.pushButton_5.setText(_translate("MainWindow", "+"))
        self.label.setText(_translate("MainWindow", "Head programmid"))
        self.label_2.setText(_translate("MainWindow", "Halvad programmid"))
        self.menuPrograms.setTitle(_translate("MainWindow", "Lisa"))
        self.actionAddGoodProgram.setText(_translate("MainWindow", "Lisa hea programm"))
        self.actionAddBadProgram.setText(_translate("MainWindow", "Lisa halb programm"))

    def hea_valitud(self):
        if not hasattr(self, 'hea_valitud_count'):
            self.hea_valitud_count = 0

        if self.hea_valitud_count < 3:
            if hasattr(self, 'last_added_hea_button'):
                new_button = QtWidgets.QPushButton("+", self.centralwidget)
                new_button.setGeometry(self.last_added_hea_button.geometry().translated(80, 0))
            else:
                new_button = QtWidgets.QPushButton("+", self.centralwidget)
                new_button.setGeometry(self.pushButton_4.geometry().translated(80, 0))

            new_button.show()
            self.last_added_hea_button = new_button
            self.hea_valitud_count += 1
        else:
            print("Hea_valitud can't be used more than 3 times.")

    def halb_valitud(self):
        if not hasattr(self, 'halb_valitud_count'):
            self.halb_valitud_count = 0

        if self.halb_valitud_count < 3:
            if hasattr(self, 'last_added_halb_button'):
                new_button = QtWidgets.QPushButton("+", self.centralwidget)
                new_button.setGeometry(self.last_added_halb_button.geometry().translated(80, 0))
            else:
                new_button = QtWidgets.QPushButton("+", self.centralwidget)
                new_button.setGeometry(self.pushButton_5.geometry().translated(80, 0))

            new_button.show()
            self.last_added_halb_button = new_button
            self.halb_valitud_count += 1
        else:
            print("Halb_valitud can't be used more than 3 times.")

def start_ui():   
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start_ui()
