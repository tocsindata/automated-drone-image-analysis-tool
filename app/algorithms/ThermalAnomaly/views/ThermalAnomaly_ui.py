# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charl\source\repos\crgrove\automated-drone-image-analysis-tool\resources/views/algorithms/ThermalAnomaly.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ThermalAnomaly(object):
    def setupUi(self, ThermalAnomaly):
        ThermalAnomaly.setObjectName("ThermalAnomaly")
        ThermalAnomaly.resize(674, 94)
        self.verticalLayout = QtWidgets.QVBoxLayout(ThermalAnomaly)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.typeLabel = QtWidgets.QLabel(ThermalAnomaly)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.typeLabel.setFont(font)
        self.typeLabel.setObjectName("typeLabel")
        self.horizontalLayout_3.addWidget(self.typeLabel)
        self.anomalyTypeComboBox = QtWidgets.QComboBox(ThermalAnomaly)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.anomalyTypeComboBox.setFont(font)
        self.anomalyTypeComboBox.setObjectName("anomalyTypeComboBox")
        self.anomalyTypeComboBox.addItem("")
        self.anomalyTypeComboBox.addItem("")
        self.anomalyTypeComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.anomalyTypeComboBox)
        self.thersholdLabel = QtWidgets.QLabel(ThermalAnomaly)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.thersholdLabel.setFont(font)
        self.thersholdLabel.setObjectName("thersholdLabel")
        self.horizontalLayout_3.addWidget(self.thersholdLabel)
        self.anomalySpinBox = QtWidgets.QSpinBox(ThermalAnomaly)
        self.anomalySpinBox.setMaximum(7)
        self.anomalySpinBox.setProperty("value", 4)
        self.anomalySpinBox.setObjectName("anomalySpinBox")
        self.horizontalLayout_3.addWidget(self.anomalySpinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.colorMapLabel = QtWidgets.QLabel(ThermalAnomaly)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.colorMapLabel.setFont(font)
        self.colorMapLabel.setObjectName("colorMapLabel")
        self.horizontalLayout_3.addWidget(self.colorMapLabel)
        self.colorMapComboBox = QtWidgets.QComboBox(ThermalAnomaly)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.colorMapComboBox.setFont(font)
        self.colorMapComboBox.setObjectName("colorMapComboBox")
        self.colorMapComboBox.addItem("")
        self.colorMapComboBox.addItem("")
        self.colorMapComboBox.addItem("")
        self.colorMapComboBox.addItem("")
        self.colorMapComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.colorMapComboBox)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(ThermalAnomaly)
        QtCore.QMetaObject.connectSlotsByName(ThermalAnomaly)

    def retranslateUi(self, ThermalAnomaly):
        _translate = QtCore.QCoreApplication.translate
        ThermalAnomaly.setWindowTitle(_translate("ThermalAnomaly", "Form"))
        self.typeLabel.setText(_translate("ThermalAnomaly", "Anomaly Type:"))
        self.anomalyTypeComboBox.setItemText(0, _translate("ThermalAnomaly", "Above or Below Mean"))
        self.anomalyTypeComboBox.setItemText(1, _translate("ThermalAnomaly", "Above Mean"))
        self.anomalyTypeComboBox.setItemText(2, _translate("ThermalAnomaly", "Below Mean"))
        self.thersholdLabel.setText(_translate("ThermalAnomaly", "Anomaly Threshold:"))
        self.colorMapLabel.setText(_translate("ThermalAnomaly", "Color Map: "))
        self.colorMapComboBox.setItemText(0, _translate("ThermalAnomaly", "White Hot"))
        self.colorMapComboBox.setItemText(1, _translate("ThermalAnomaly", "Black Hot"))
        self.colorMapComboBox.setItemText(2, _translate("ThermalAnomaly", "Inferno (Iron Red)"))
        self.colorMapComboBox.setItemText(3, _translate("ThermalAnomaly", "Hot (Fulgurite)"))
        self.colorMapComboBox.setItemText(4, _translate("ThermalAnomaly", "Jet (Rainbow2)"))
