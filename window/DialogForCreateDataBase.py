# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogForCreateDataBase.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(422, 353)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(480, 670, 379, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 20, 381, 317))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.input1 = QtWidgets.QLineEdit(self.widget)
        self.input1.setObjectName("input1")
        self.horizontalLayout_2.addWidget(self.input1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_12 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.input11 = QtWidgets.QLineEdit(self.widget)
        self.input11.setObjectName("input11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input11)
        self.label_15 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.input12 = QtWidgets.QLineEdit(self.widget)
        self.input12.setObjectName("input12")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input12)
        self.label_17 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.input13 = QtWidgets.QLineEdit(self.widget)
        self.input13.setObjectName("input13")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.input13)
        self.label_18 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.input14 = QtWidgets.QLineEdit(self.widget)
        self.input14.setObjectName("input14")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.input14)
        self.label_19 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.input15 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input15.sizePolicy().hasHeightForWidth())
        self.input15.setSizePolicy(sizePolicy)
        self.input15.setObjectName("input15")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.input15)
        self.label_20 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_20)
        self.horizontalLayout.addLayout(self.formLayout_3)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.input21 = QtWidgets.QLineEdit(self.widget)
        self.input21.setObjectName("input21")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input21)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.input22 = QtWidgets.QLineEdit(self.widget)
        self.input22.setObjectName("input22")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.input22)
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.input23 = QtWidgets.QLineEdit(self.widget)
        self.input23.setObjectName("input23")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.input23)
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.input24 = QtWidgets.QLineEdit(self.widget)
        self.input24.setObjectName("input24")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.input24)
        self.label_11 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.input25 = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input25.sizePolicy().hasHeightForWidth())
        self.input25.setSizePolicy(sizePolicy)
        self.input25.setObjectName("input25")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.input25)
        self.label_13 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_13)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.create_btn = QtWidgets.QPushButton(self.widget)
        self.create_btn.setObjectName("create_btn")
        self.verticalLayout.addWidget(self.create_btn)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_16.setText(_translate("Dialog", "(Введите название базы данных)"))
        self.label_14.setText(_translate("Dialog", "Create Data Base"))
        self.label_2.setText(_translate("Dialog", "(Введите название базы данных)"))
        self.label_12.setText(_translate("Dialog", "1:"))
        self.label_15.setText(_translate("Dialog", "2:"))
        self.label_17.setText(_translate("Dialog", "3:"))
        self.label_18.setText(_translate("Dialog", "4:"))
        self.label_19.setText(_translate("Dialog", "5:"))
        self.label_20.setText(_translate("Dialog", "Main table"))
        self.label_7.setText(_translate("Dialog", "1:"))
        self.label_8.setText(_translate("Dialog", "2:"))
        self.label_9.setText(_translate("Dialog", "3:"))
        self.label_10.setText(_translate("Dialog", "4:"))
        self.label_11.setText(_translate("Dialog", "5:"))
        self.label_13.setText(_translate("Dialog", "Additional table"))
        self.label.setText(_translate("Dialog", "(Введите название столбцов)"))
        self.create_btn.setText(_translate("Dialog", "Create"))
