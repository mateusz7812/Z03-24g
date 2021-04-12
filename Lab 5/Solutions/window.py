# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(487, 482)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(487, 482))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(362, 482))
        self.centralwidget.setMaximumSize(QtCore.QSize(100000, 100000))
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setBaseSize(QtCore.QSize(362, 482))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.equation_label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.equation_label.sizePolicy().hasHeightForWidth())
        self.equation_label.setSizePolicy(sizePolicy)
        self.equation_label.setMinimumSize(QtCore.QSize(362, 0))
        self.equation_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.equation_label.setStyleSheet("background-color: rgb(247, 247, 247);\n"
"font: 12pt \"Arial\";")
        self.equation_label.setText("")
        self.equation_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.equation_label.setObjectName("equation_label")
        self.verticalLayout.addWidget(self.equation_label)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.divide_button = QtWidgets.QPushButton(self.centralwidget)
        self.divide_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.divide_button.sizePolicy().hasHeightForWidth())
        self.divide_button.setSizePolicy(sizePolicy)
        self.divide_button.setObjectName("divide_button")
        self.gridLayout_2.addWidget(self.divide_button, 4, 3, 1, 1)
        self.inversion_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inversion_button.sizePolicy().hasHeightForWidth())
        self.inversion_button.setSizePolicy(sizePolicy)
        self.inversion_button.setObjectName("inversion_button")
        self.gridLayout_2.addWidget(self.inversion_button, 2, 3, 1, 1)
        self.absolute_button = QtWidgets.QPushButton(self.centralwidget)
        self.absolute_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.absolute_button.sizePolicy().hasHeightForWidth())
        self.absolute_button.setSizePolicy(sizePolicy)
        self.absolute_button.setObjectName("absolute_button")
        self.gridLayout_2.addWidget(self.absolute_button, 9, 1, 1, 1)
        self.add_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        self.add_button.setObjectName("add_button")
        self.gridLayout_2.addWidget(self.add_button, 7, 2, 1, 1)
        self.modulo_f_button = QtWidgets.QPushButton(self.centralwidget)
        self.modulo_f_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modulo_f_button.sizePolicy().hasHeightForWidth())
        self.modulo_f_button.setSizePolicy(sizePolicy)
        self.modulo_f_button.setObjectName("modulo_f_button")
        self.gridLayout_2.addWidget(self.modulo_f_button, 7, 1, 1, 1)
        self.right_bracket_button = QtWidgets.QPushButton(self.centralwidget)
        self.right_bracket_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.right_bracket_button.sizePolicy().hasHeightForWidth())
        self.right_bracket_button.setSizePolicy(sizePolicy)
        self.right_bracket_button.setObjectName("right_bracket_button")
        self.gridLayout_2.addWidget(self.right_bracket_button, 9, 3, 1, 1)
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setObjectName("clear_button")
        self.gridLayout_2.addWidget(self.clear_button, 9, 4, 1, 1)
        self.number_5_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_5_button.sizePolicy().hasHeightForWidth())
        self.number_5_button.setSizePolicy(sizePolicy)
        self.number_5_button.setObjectName("number_5_button")
        self.gridLayout_2.addWidget(self.number_5_button, 2, 6, 1, 1)
        self.power_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power_button.sizePolicy().hasHeightForWidth())
        self.power_button.setSizePolicy(sizePolicy)
        self.power_button.setObjectName("power_button")
        self.gridLayout_2.addWidget(self.power_button, 0, 3, 1, 1)
        self.number_7_button = QtWidgets.QPushButton(self.centralwidget)
        self.number_7_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_7_button.sizePolicy().hasHeightForWidth())
        self.number_7_button.setSizePolicy(sizePolicy)
        self.number_7_button.setObjectName("number_7_button")
        self.gridLayout_2.addWidget(self.number_7_button, 0, 4, 1, 1)
        self.number_8_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_8_button.sizePolicy().hasHeightForWidth())
        self.number_8_button.setSizePolicy(sizePolicy)
        self.number_8_button.setObjectName("number_8_button")
        self.gridLayout_2.addWidget(self.number_8_button, 0, 6, 1, 1)
        self.undo_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undo_button.sizePolicy().hasHeightForWidth())
        self.undo_button.setSizePolicy(sizePolicy)
        self.undo_button.setObjectName("undo_button")
        self.gridLayout_2.addWidget(self.undo_button, 9, 6, 1, 1)
        self.number_0_button = QtWidgets.QPushButton(self.centralwidget)
        self.number_0_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_0_button.sizePolicy().hasHeightForWidth())
        self.number_0_button.setSizePolicy(sizePolicy)
        self.number_0_button.setObjectName("number_0_button")
        self.gridLayout_2.addWidget(self.number_0_button, 7, 6, 1, 1)
        self.comma_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comma_button.sizePolicy().hasHeightForWidth())
        self.comma_button.setSizePolicy(sizePolicy)
        self.comma_button.setObjectName("comma_button")
        self.gridLayout_2.addWidget(self.comma_button, 7, 8, 1, 1)
        self.calc_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calc_button.sizePolicy().hasHeightForWidth())
        self.calc_button.setSizePolicy(sizePolicy)
        self.calc_button.setObjectName("calc_button")
        self.gridLayout_2.addWidget(self.calc_button, 9, 8, 1, 1)
        self.square_power_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.square_power_button.sizePolicy().hasHeightForWidth())
        self.square_power_button.setSizePolicy(sizePolicy)
        self.square_power_button.setObjectName("square_power_button")
        self.gridLayout_2.addWidget(self.square_power_button, 2, 1, 1, 1)
        self.logarithm_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logarithm_button.sizePolicy().hasHeightForWidth())
        self.logarithm_button.setSizePolicy(sizePolicy)
        self.logarithm_button.setObjectName("logarithm_button")
        self.gridLayout_2.addWidget(self.logarithm_button, 4, 1, 1, 1)
        self.modulo_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.modulo_button.sizePolicy().hasHeightForWidth())
        self.modulo_button.setSizePolicy(sizePolicy)
        self.modulo_button.setObjectName("modulo_button")
        self.gridLayout_2.addWidget(self.modulo_button, 0, 2, 1, 1)
        self.square_root_button = QtWidgets.QPushButton(self.centralwidget)
        self.square_root_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.square_root_button.sizePolicy().hasHeightForWidth())
        self.square_root_button.setSizePolicy(sizePolicy)
        self.square_root_button.setObjectName("square_root_button")
        self.gridLayout_2.addWidget(self.square_root_button, 0, 1, 1, 1)
        self.multiply_button = QtWidgets.QPushButton(self.centralwidget)
        self.multiply_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.multiply_button.sizePolicy().hasHeightForWidth())
        self.multiply_button.setSizePolicy(sizePolicy)
        self.multiply_button.setObjectName("multiply_button")
        self.gridLayout_2.addWidget(self.multiply_button, 4, 2, 1, 1)
        self.factorial_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.factorial_button.sizePolicy().hasHeightForWidth())
        self.factorial_button.setSizePolicy(sizePolicy)
        self.factorial_button.setObjectName("factorial_button")
        self.gridLayout_2.addWidget(self.factorial_button, 2, 2, 1, 1)
        self.left_bracket_button = QtWidgets.QPushButton(self.centralwidget)
        self.left_bracket_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_bracket_button.sizePolicy().hasHeightForWidth())
        self.left_bracket_button.setSizePolicy(sizePolicy)
        self.left_bracket_button.setObjectName("left_bracket_button")
        self.gridLayout_2.addWidget(self.left_bracket_button, 9, 2, 1, 1)
        self.subtract_button = QtWidgets.QPushButton(self.centralwidget)
        self.subtract_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtract_button.sizePolicy().hasHeightForWidth())
        self.subtract_button.setSizePolicy(sizePolicy)
        self.subtract_button.setObjectName("subtract_button")
        self.gridLayout_2.addWidget(self.subtract_button, 7, 3, 1, 1)
        self.number_4_button = QtWidgets.QPushButton(self.centralwidget)
        self.number_4_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_4_button.sizePolicy().hasHeightForWidth())
        self.number_4_button.setSizePolicy(sizePolicy)
        self.number_4_button.setObjectName("number_4_button")
        self.gridLayout_2.addWidget(self.number_4_button, 2, 4, 1, 1)
        self.number_1_button = QtWidgets.QPushButton(self.centralwidget)
        self.number_1_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_1_button.sizePolicy().hasHeightForWidth())
        self.number_1_button.setSizePolicy(sizePolicy)
        self.number_1_button.setObjectName("number_1_button")
        self.gridLayout_2.addWidget(self.number_1_button, 4, 4, 1, 1)
        self.number_2_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_2_button.sizePolicy().hasHeightForWidth())
        self.number_2_button.setSizePolicy(sizePolicy)
        self.number_2_button.setObjectName("number_2_button")
        self.gridLayout_2.addWidget(self.number_2_button, 4, 6, 1, 1)
        self.brackets_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brackets_button.sizePolicy().hasHeightForWidth())
        self.brackets_button.setSizePolicy(sizePolicy)
        self.brackets_button.setObjectName("brackets_button")
        self.gridLayout_2.addWidget(self.brackets_button, 7, 4, 1, 1)
        self.number_9_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_9_button.sizePolicy().hasHeightForWidth())
        self.number_9_button.setSizePolicy(sizePolicy)
        self.number_9_button.setObjectName("number_9_button")
        self.gridLayout_2.addWidget(self.number_9_button, 0, 8, 1, 1)
        self.number_6_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_6_button.sizePolicy().hasHeightForWidth())
        self.number_6_button.setSizePolicy(sizePolicy)
        self.number_6_button.setObjectName("number_6_button")
        self.gridLayout_2.addWidget(self.number_6_button, 2, 8, 1, 1)
        self.number_3_button = QtWidgets.QPushButton(self.centralwidget)
        self.number_3_button.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number_3_button.sizePolicy().hasHeightForWidth())
        self.number_3_button.setSizePolicy(sizePolicy)
        self.number_3_button.setObjectName("number_3_button")
        self.gridLayout_2.addWidget(self.number_3_button, 4, 8, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.divide_button.setText(_translate("MainWindow", "/"))
        self.inversion_button.setText(_translate("MainWindow", "1/(x)"))
        self.absolute_button.setText(_translate("MainWindow", "|x|"))
        self.add_button.setText(_translate("MainWindow", "+"))
        self.modulo_f_button.setText(_translate("MainWindow", "mod(x)"))
        self.right_bracket_button.setText(_translate("MainWindow", ")"))
        self.clear_button.setText(_translate("MainWindow", "CE"))
        self.number_5_button.setText(_translate("MainWindow", "5"))
        self.power_button.setText(_translate("MainWindow", "^"))
        self.number_7_button.setText(_translate("MainWindow", "7"))
        self.number_8_button.setText(_translate("MainWindow", "8"))
        self.undo_button.setText(_translate("MainWindow", "C"))
        self.number_0_button.setText(_translate("MainWindow", "0"))
        self.comma_button.setText(_translate("MainWindow", "."))
        self.calc_button.setText(_translate("MainWindow", "="))
        self.square_power_button.setText(_translate("MainWindow", "(x)^2"))
        self.logarithm_button.setText(_translate("MainWindow", "log(x)"))
        self.modulo_button.setText(_translate("MainWindow", "%"))
        self.square_root_button.setText(_translate("MainWindow", "sqrt(x)"))
        self.multiply_button.setText(_translate("MainWindow", "*"))
        self.factorial_button.setText(_translate("MainWindow", "!"))
        self.left_bracket_button.setText(_translate("MainWindow", "("))
        self.subtract_button.setText(_translate("MainWindow", "-"))
        self.number_4_button.setText(_translate("MainWindow", "4"))
        self.number_1_button.setText(_translate("MainWindow", "1"))
        self.number_2_button.setText(_translate("MainWindow", "2"))
        self.brackets_button.setText(_translate("MainWindow", "(x)"))
        self.number_9_button.setText(_translate("MainWindow", "9"))
        self.number_6_button.setText(_translate("MainWindow", "6"))
        self.number_3_button.setText(_translate("MainWindow", "3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())