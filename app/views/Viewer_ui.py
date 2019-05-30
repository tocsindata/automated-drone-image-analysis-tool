# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\xampp7\htdocs\ADIAT\resources/views\Viewer.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Viewer(object):
    def setupUi(self, Viewer):
        Viewer.setObjectName("Viewer")
        Viewer.resize(1040, 774)
        self.centralwidget = QtWidgets.QWidget(Viewer)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.fileNameLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.fileNameLabel.setFont(font)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.verticalLayout.addWidget(self.fileNameLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.placeholderImage = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.placeholderImage.sizePolicy().hasHeightForWidth())
        self.placeholderImage.setSizePolicy(sizePolicy)
        self.placeholderImage.setMinimumSize(QtCore.QSize(0, 650))
        self.placeholderImage.setObjectName("placeholderImage")
        self.horizontalLayout.addWidget(self.placeholderImage)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(250, 0))
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 248, 648))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.previousImageButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.previousImageButton.setFont(font)
        self.previousImageButton.setObjectName("previousImageButton")
        self.horizontalLayout_2.addWidget(self.previousImageButton)
        self.nextImageButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nextImageButton.setFont(font)
        self.nextImageButton.setObjectName("nextImageButton")
        self.horizontalLayout_2.addWidget(self.nextImageButton)
        spacerItem1 = QtWidgets.QSpacerItem(250, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        Viewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Viewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1040, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        Viewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Viewer)
        self.statusbar.setObjectName("statusbar")
        Viewer.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(Viewer)
        self.actionOpen.setObjectName("actionOpen")
        self.menuFile.addAction(self.actionOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(Viewer)
        QtCore.QMetaObject.connectSlotsByName(Viewer)

    def retranslateUi(self, Viewer):
        _translate = QtCore.QCoreApplication.translate
        Viewer.setWindowTitle(_translate("Viewer", "Automated Drone Image Analysis Tool :: Viewer - Sponsored by TEXSAR"))
        self.fileNameLabel.setText(_translate("Viewer", "TextLabel"))
        self.previousImageButton.setText(_translate("Viewer", "Previous Image"))
        self.nextImageButton.setText(_translate("Viewer", "Next Image"))
        self.menuFile.setTitle(_translate("Viewer", "File"))
        self.actionOpen.setText(_translate("Viewer", "Open"))


