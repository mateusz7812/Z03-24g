# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'message_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MessageWidget(object):
    def setupUi(self, MessageWidget):
        MessageWidget.setObjectName("MessageWidget")
        MessageWidget.resize(526, 78)
        self.horizontalLayout = QtWidgets.QHBoxLayout(MessageWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.message_label = QtWidgets.QLabel(MessageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message_label.sizePolicy().hasHeightForWidth())
        self.message_label.setSizePolicy(sizePolicy)
        self.message_label.setStyleSheet("background: white; border-radius: 10px; padding:10px; border: 1px solid lightgray;")
        self.message_label.setWordWrap(True)
        self.message_label.setObjectName("message_label")
        self.horizontalLayout.addWidget(self.message_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(MessageWidget)
        QtCore.QMetaObject.connectSlotsByName(MessageWidget)

    def retranslateUi(self, MessageWidget):
        _translate = QtCore.QCoreApplication.translate
        MessageWidget.setWindowTitle(_translate("MessageWidget", "Form"))
        self.message_label.setText(_translate("MessageWidget", "dklafjlkdaj;ljkdf"))
