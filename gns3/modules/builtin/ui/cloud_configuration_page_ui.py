# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cloud_configuration_page.ui'
#
# Created: Wed May  6 14:31:55 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_cloudConfigPageWidget(object):

    def setupUi(self, cloudConfigPageWidget):
        cloudConfigPageWidget.setObjectName("cloudConfigPageWidget")
        cloudConfigPageWidget.resize(542, 500)
        self.vboxlayout = QtWidgets.QVBoxLayout(cloudConfigPageWidget)
        self.vboxlayout.setObjectName("vboxlayout")
        self.tabWidget = QtWidgets.QTabWidget(cloudConfigPageWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.vboxlayout1 = QtWidgets.QVBoxLayout(self.tab)
        self.vboxlayout1.setObjectName("vboxlayout1")
        self.uiGenericEthernetGroupBox = QtWidgets.QGroupBox(self.tab)
        self.uiGenericEthernetGroupBox.setObjectName("uiGenericEthernetGroupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.uiGenericEthernetGroupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.uiGenericEthernetComboBox = QtWidgets.QComboBox(self.uiGenericEthernetGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiGenericEthernetComboBox.sizePolicy().hasHeightForWidth())
        self.uiGenericEthernetComboBox.setSizePolicy(sizePolicy)
        self.uiGenericEthernetComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.uiGenericEthernetComboBox.setObjectName("uiGenericEthernetComboBox")
        self.gridlayout.addWidget(self.uiGenericEthernetComboBox, 0, 0, 1, 3)
        self.uiGenericEthernetLineEdit = QtWidgets.QLineEdit(self.uiGenericEthernetGroupBox)
        self.uiGenericEthernetLineEdit.setObjectName("uiGenericEthernetLineEdit")
        self.gridlayout.addWidget(self.uiGenericEthernetLineEdit, 1, 0, 1, 1)
        self.uiAddGenericEthernetPushButton = QtWidgets.QPushButton(self.uiGenericEthernetGroupBox)
        self.uiAddGenericEthernetPushButton.setObjectName("uiAddGenericEthernetPushButton")
        self.gridlayout.addWidget(self.uiAddGenericEthernetPushButton, 1, 1, 1, 1)
        self.uiDeleteGenericEthernetPushButton = QtWidgets.QPushButton(self.uiGenericEthernetGroupBox)
        self.uiDeleteGenericEthernetPushButton.setEnabled(False)
        self.uiDeleteGenericEthernetPushButton.setObjectName("uiDeleteGenericEthernetPushButton")
        self.gridlayout.addWidget(self.uiDeleteGenericEthernetPushButton, 1, 2, 1, 1)
        self.uiGenericEthernetListWidget = QtWidgets.QListWidget(self.uiGenericEthernetGroupBox)
        self.uiGenericEthernetListWidget.setObjectName("uiGenericEthernetListWidget")
        self.gridlayout.addWidget(self.uiGenericEthernetListWidget, 2, 0, 1, 3)
        self.vboxlayout1.addWidget(self.uiGenericEthernetGroupBox)
        self.uiLinuxEthernetGroupBox = QtWidgets.QGroupBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLinuxEthernetGroupBox.sizePolicy().hasHeightForWidth())
        self.uiLinuxEthernetGroupBox.setSizePolicy(sizePolicy)
        self.uiLinuxEthernetGroupBox.setObjectName("uiLinuxEthernetGroupBox")
        self.gridlayout1 = QtWidgets.QGridLayout(self.uiLinuxEthernetGroupBox)
        self.gridlayout1.setObjectName("gridlayout1")
        self.uiLinuxEthernetComboBox = QtWidgets.QComboBox(self.uiLinuxEthernetGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLinuxEthernetComboBox.sizePolicy().hasHeightForWidth())
        self.uiLinuxEthernetComboBox.setSizePolicy(sizePolicy)
        self.uiLinuxEthernetComboBox.setObjectName("uiLinuxEthernetComboBox")
        self.gridlayout1.addWidget(self.uiLinuxEthernetComboBox, 0, 0, 1, 3)
        self.uiLinuxEthernetLineEdit = QtWidgets.QLineEdit(self.uiLinuxEthernetGroupBox)
        self.uiLinuxEthernetLineEdit.setObjectName("uiLinuxEthernetLineEdit")
        self.gridlayout1.addWidget(self.uiLinuxEthernetLineEdit, 1, 0, 1, 1)
        self.uiAddLinuxEthernetPushButton = QtWidgets.QPushButton(self.uiLinuxEthernetGroupBox)
        self.uiAddLinuxEthernetPushButton.setObjectName("uiAddLinuxEthernetPushButton")
        self.gridlayout1.addWidget(self.uiAddLinuxEthernetPushButton, 1, 1, 1, 1)
        self.uiDeleteLinuxEthernetPushButton = QtWidgets.QPushButton(self.uiLinuxEthernetGroupBox)
        self.uiDeleteLinuxEthernetPushButton.setEnabled(False)
        self.uiDeleteLinuxEthernetPushButton.setObjectName("uiDeleteLinuxEthernetPushButton")
        self.gridlayout1.addWidget(self.uiDeleteLinuxEthernetPushButton, 1, 2, 1, 1)
        self.uiLinuxEthernetListWidget = QtWidgets.QListWidget(self.uiLinuxEthernetGroupBox)
        self.uiLinuxEthernetListWidget.setObjectName("uiLinuxEthernetListWidget")
        self.gridlayout1.addWidget(self.uiLinuxEthernetListWidget, 2, 0, 1, 3)
        self.vboxlayout1.addWidget(self.uiLinuxEthernetGroupBox)
        spacerItem = QtWidgets.QSpacerItem(21, 16, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vboxlayout1.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridlayout2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridlayout2.setObjectName("gridlayout2")
        self.uiNIOUDPSettingsGroupBox = QtWidgets.QGroupBox(self.tab_2)
        self.uiNIOUDPSettingsGroupBox.setObjectName("uiNIOUDPSettingsGroupBox")
        self.gridlayout3 = QtWidgets.QGridLayout(self.uiNIOUDPSettingsGroupBox)
        self.gridlayout3.setObjectName("gridlayout3")
        self.uiLocalPortLabel = QtWidgets.QLabel(self.uiNIOUDPSettingsGroupBox)
        self.uiLocalPortLabel.setObjectName("uiLocalPortLabel")
        self.gridlayout3.addWidget(self.uiLocalPortLabel, 0, 0, 1, 1)
        self.uiLocalPortSpinBox = QtWidgets.QSpinBox(self.uiNIOUDPSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiLocalPortSpinBox.setSizePolicy(sizePolicy)
        self.uiLocalPortSpinBox.setMaximum(65535)
        self.uiLocalPortSpinBox.setProperty("value", 30000)
        self.uiLocalPortSpinBox.setObjectName("uiLocalPortSpinBox")
        self.gridlayout3.addWidget(self.uiLocalPortSpinBox, 0, 1, 1, 1)
        self.uiRemoteHostLabel = QtWidgets.QLabel(self.uiNIOUDPSettingsGroupBox)
        self.uiRemoteHostLabel.setObjectName("uiRemoteHostLabel")
        self.gridlayout3.addWidget(self.uiRemoteHostLabel, 1, 0, 1, 1)
        self.uiRemoteHostLineEdit = QtWidgets.QLineEdit(self.uiNIOUDPSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteHostLineEdit.sizePolicy().hasHeightForWidth())
        self.uiRemoteHostLineEdit.setSizePolicy(sizePolicy)
        self.uiRemoteHostLineEdit.setMinimumSize(QtCore.QSize(80, 0))
        self.uiRemoteHostLineEdit.setObjectName("uiRemoteHostLineEdit")
        self.gridlayout3.addWidget(self.uiRemoteHostLineEdit, 1, 1, 1, 1)
        self.uiRemotePortLabel = QtWidgets.QLabel(self.uiNIOUDPSettingsGroupBox)
        self.uiRemotePortLabel.setObjectName("uiRemotePortLabel")
        self.gridlayout3.addWidget(self.uiRemotePortLabel, 2, 0, 1, 1)
        self.uiRemotePortSpinBox = QtWidgets.QSpinBox(self.uiNIOUDPSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemotePortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRemotePortSpinBox.setSizePolicy(sizePolicy)
        self.uiRemotePortSpinBox.setMaximum(65535)
        self.uiRemotePortSpinBox.setProperty("value", 20000)
        self.uiRemotePortSpinBox.setObjectName("uiRemotePortSpinBox")
        self.gridlayout3.addWidget(self.uiRemotePortSpinBox, 2, 1, 1, 1)
        self.gridlayout2.addWidget(self.uiNIOUDPSettingsGroupBox, 0, 0, 1, 2)
        self.uiNIOUDPListGroupBox = QtWidgets.QGroupBox(self.tab_2)
        self.uiNIOUDPListGroupBox.setObjectName("uiNIOUDPListGroupBox")
        self.vboxlayout2 = QtWidgets.QVBoxLayout(self.uiNIOUDPListGroupBox)
        self.vboxlayout2.setObjectName("vboxlayout2")
        self.uiNIOUDPListWidget = QtWidgets.QListWidget(self.uiNIOUDPListGroupBox)
        self.uiNIOUDPListWidget.setObjectName("uiNIOUDPListWidget")
        self.vboxlayout2.addWidget(self.uiNIOUDPListWidget)
        self.gridlayout2.addWidget(self.uiNIOUDPListGroupBox, 0, 2, 2, 1)
        self.uiAddNIOUDPPushButton = QtWidgets.QPushButton(self.tab_2)
        self.uiAddNIOUDPPushButton.setObjectName("uiAddNIOUDPPushButton")
        self.gridlayout2.addWidget(self.uiAddNIOUDPPushButton, 1, 0, 1, 1)
        self.uiDeleteNIOUDPPushButton = QtWidgets.QPushButton(self.tab_2)
        self.uiDeleteNIOUDPPushButton.setEnabled(False)
        self.uiDeleteNIOUDPPushButton.setObjectName("uiDeleteNIOUDPPushButton")
        self.gridlayout2.addWidget(self.uiDeleteNIOUDPPushButton, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 211, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout2.addItem(spacerItem1, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.vboxlayout3 = QtWidgets.QVBoxLayout(self.tab_3)
        self.vboxlayout3.setObjectName("vboxlayout3")
        self.uiNIOTAPGroupBox = QtWidgets.QGroupBox(self.tab_3)
        self.uiNIOTAPGroupBox.setObjectName("uiNIOTAPGroupBox")
        self.gridlayout4 = QtWidgets.QGridLayout(self.uiNIOTAPGroupBox)
        self.gridlayout4.setObjectName("gridlayout4")
        self.uiNIOTAPLineEdit = QtWidgets.QLineEdit(self.uiNIOTAPGroupBox)
        self.uiNIOTAPLineEdit.setObjectName("uiNIOTAPLineEdit")
        self.gridlayout4.addWidget(self.uiNIOTAPLineEdit, 0, 0, 1, 1)
        self.uiAddNIOTAPPushButton = QtWidgets.QPushButton(self.uiNIOTAPGroupBox)
        self.uiAddNIOTAPPushButton.setObjectName("uiAddNIOTAPPushButton")
        self.gridlayout4.addWidget(self.uiAddNIOTAPPushButton, 0, 1, 1, 1)
        self.uiDeleteNIOTAPPushButton = QtWidgets.QPushButton(self.uiNIOTAPGroupBox)
        self.uiDeleteNIOTAPPushButton.setEnabled(False)
        self.uiDeleteNIOTAPPushButton.setObjectName("uiDeleteNIOTAPPushButton")
        self.gridlayout4.addWidget(self.uiDeleteNIOTAPPushButton, 0, 2, 1, 1)
        self.uiNIOTAPListWidget = QtWidgets.QListWidget(self.uiNIOTAPGroupBox)
        self.uiNIOTAPListWidget.setObjectName("uiNIOTAPListWidget")
        self.gridlayout4.addWidget(self.uiNIOTAPListWidget, 1, 0, 1, 3)
        self.vboxlayout3.addWidget(self.uiNIOTAPGroupBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 191, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridlayout5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridlayout5.setObjectName("gridlayout5")
        self.uiNIOUNIXSettingsGroupBox = QtWidgets.QGroupBox(self.tab_4)
        self.uiNIOUNIXSettingsGroupBox.setObjectName("uiNIOUNIXSettingsGroupBox")
        self.gridlayout6 = QtWidgets.QGridLayout(self.uiNIOUNIXSettingsGroupBox)
        self.gridlayout6.setObjectName("gridlayout6")
        self.gridlayout7 = QtWidgets.QGridLayout()
        self.gridlayout7.setObjectName("gridlayout7")
        self.uiLocalFileLabel = QtWidgets.QLabel(self.uiNIOUNIXSettingsGroupBox)
        self.uiLocalFileLabel.setObjectName("uiLocalFileLabel")
        self.gridlayout7.addWidget(self.uiLocalFileLabel, 0, 0, 1, 1)
        self.uiLocalFileLineEdit = QtWidgets.QLineEdit(self.uiNIOUNIXSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalFileLineEdit.sizePolicy().hasHeightForWidth())
        self.uiLocalFileLineEdit.setSizePolicy(sizePolicy)
        self.uiLocalFileLineEdit.setObjectName("uiLocalFileLineEdit")
        self.gridlayout7.addWidget(self.uiLocalFileLineEdit, 1, 0, 1, 1)
        self.gridlayout6.addLayout(self.gridlayout7, 0, 0, 1, 1)
        self.gridlayout8 = QtWidgets.QGridLayout()
        self.gridlayout8.setObjectName("gridlayout8")
        self.uiRemoteFileLabel = QtWidgets.QLabel(self.uiNIOUNIXSettingsGroupBox)
        self.uiRemoteFileLabel.setObjectName("uiRemoteFileLabel")
        self.gridlayout8.addWidget(self.uiRemoteFileLabel, 0, 0, 1, 1)
        self.uiRemoteFileLineEdit = QtWidgets.QLineEdit(self.uiNIOUNIXSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteFileLineEdit.sizePolicy().hasHeightForWidth())
        self.uiRemoteFileLineEdit.setSizePolicy(sizePolicy)
        self.uiRemoteFileLineEdit.setObjectName("uiRemoteFileLineEdit")
        self.gridlayout8.addWidget(self.uiRemoteFileLineEdit, 1, 0, 1, 1)
        self.gridlayout6.addLayout(self.gridlayout8, 1, 0, 1, 1)
        self.gridlayout5.addWidget(self.uiNIOUNIXSettingsGroupBox, 0, 0, 1, 2)
        self.uiNIOUNIXListGroupBox = QtWidgets.QGroupBox(self.tab_4)
        self.uiNIOUNIXListGroupBox.setObjectName("uiNIOUNIXListGroupBox")
        self.vboxlayout4 = QtWidgets.QVBoxLayout(self.uiNIOUNIXListGroupBox)
        self.vboxlayout4.setObjectName("vboxlayout4")
        self.uiNIOUNIXListWidget = QtWidgets.QListWidget(self.uiNIOUNIXListGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNIOUNIXListWidget.sizePolicy().hasHeightForWidth())
        self.uiNIOUNIXListWidget.setSizePolicy(sizePolicy)
        self.uiNIOUNIXListWidget.setObjectName("uiNIOUNIXListWidget")
        self.vboxlayout4.addWidget(self.uiNIOUNIXListWidget)
        self.gridlayout5.addWidget(self.uiNIOUNIXListGroupBox, 0, 2, 3, 1)
        self.uiAddNIOUNIXPushButton = QtWidgets.QPushButton(self.tab_4)
        self.uiAddNIOUNIXPushButton.setObjectName("uiAddNIOUNIXPushButton")
        self.gridlayout5.addWidget(self.uiAddNIOUNIXPushButton, 1, 0, 1, 1)
        self.uiDeleteNIOUNIXPushButton = QtWidgets.QPushButton(self.tab_4)
        self.uiDeleteNIOUNIXPushButton.setEnabled(False)
        self.uiDeleteNIOUNIXPushButton.setObjectName("uiDeleteNIOUNIXPushButton")
        self.gridlayout5.addWidget(self.uiDeleteNIOUNIXPushButton, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(160, 190, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridlayout5.addItem(spacerItem3, 2, 0, 2, 2)
        spacerItem4 = QtWidgets.QSpacerItem(196, 132, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout5.addItem(spacerItem4, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridlayout9 = QtWidgets.QGridLayout(self.tab_5)
        self.gridlayout9.setObjectName("gridlayout9")
        self.uiNIOVDESettingsGroupBox = QtWidgets.QGroupBox(self.tab_5)
        self.uiNIOVDESettingsGroupBox.setObjectName("uiNIOVDESettingsGroupBox")
        self.gridlayout10 = QtWidgets.QGridLayout(self.uiNIOVDESettingsGroupBox)
        self.gridlayout10.setObjectName("gridlayout10")
        self.gridlayout11 = QtWidgets.QGridLayout()
        self.gridlayout11.setObjectName("gridlayout11")
        self.uiVDEControlFileLabel = QtWidgets.QLabel(self.uiNIOVDESettingsGroupBox)
        self.uiVDEControlFileLabel.setObjectName("uiVDEControlFileLabel")
        self.gridlayout11.addWidget(self.uiVDEControlFileLabel, 0, 0, 1, 1)
        self.uiVDEControlFileLineEdit = QtWidgets.QLineEdit(self.uiNIOVDESettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVDEControlFileLineEdit.sizePolicy().hasHeightForWidth())
        self.uiVDEControlFileLineEdit.setSizePolicy(sizePolicy)
        self.uiVDEControlFileLineEdit.setObjectName("uiVDEControlFileLineEdit")
        self.gridlayout11.addWidget(self.uiVDEControlFileLineEdit, 1, 0, 1, 1)
        self.gridlayout10.addLayout(self.gridlayout11, 0, 0, 1, 1)
        self.gridlayout12 = QtWidgets.QGridLayout()
        self.gridlayout12.setObjectName("gridlayout12")
        self.uiVDELocalFileLabel = QtWidgets.QLabel(self.uiNIOVDESettingsGroupBox)
        self.uiVDELocalFileLabel.setObjectName("uiVDELocalFileLabel")
        self.gridlayout12.addWidget(self.uiVDELocalFileLabel, 0, 0, 1, 1)
        self.uiVDELocalFileLineEdit = QtWidgets.QLineEdit(self.uiNIOVDESettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVDELocalFileLineEdit.sizePolicy().hasHeightForWidth())
        self.uiVDELocalFileLineEdit.setSizePolicy(sizePolicy)
        self.uiVDELocalFileLineEdit.setObjectName("uiVDELocalFileLineEdit")
        self.gridlayout12.addWidget(self.uiVDELocalFileLineEdit, 1, 0, 1, 1)
        self.gridlayout10.addLayout(self.gridlayout12, 1, 0, 1, 1)
        self.gridlayout9.addWidget(self.uiNIOVDESettingsGroupBox, 0, 0, 1, 2)
        self.uiNIOVDEListGroupBox = QtWidgets.QGroupBox(self.tab_5)
        self.uiNIOVDEListGroupBox.setObjectName("uiNIOVDEListGroupBox")
        self.vboxlayout5 = QtWidgets.QVBoxLayout(self.uiNIOVDEListGroupBox)
        self.vboxlayout5.setObjectName("vboxlayout5")
        self.uiNIOVDEListWidget = QtWidgets.QListWidget(self.uiNIOVDEListGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNIOVDEListWidget.sizePolicy().hasHeightForWidth())
        self.uiNIOVDEListWidget.setSizePolicy(sizePolicy)
        self.uiNIOVDEListWidget.setObjectName("uiNIOVDEListWidget")
        self.vboxlayout5.addWidget(self.uiNIOVDEListWidget)
        self.gridlayout9.addWidget(self.uiNIOVDEListGroupBox, 0, 2, 3, 1)
        self.uiAddNIOVDEPushButton = QtWidgets.QPushButton(self.tab_5)
        self.uiAddNIOVDEPushButton.setObjectName("uiAddNIOVDEPushButton")
        self.gridlayout9.addWidget(self.uiAddNIOVDEPushButton, 1, 0, 1, 1)
        self.uiDeleteNIOVDEPushButton = QtWidgets.QPushButton(self.tab_5)
        self.uiDeleteNIOVDEPushButton.setEnabled(False)
        self.uiDeleteNIOVDEPushButton.setObjectName("uiDeleteNIOVDEPushButton")
        self.gridlayout9.addWidget(self.uiDeleteNIOVDEPushButton, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(161, 201, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridlayout9.addItem(spacerItem5, 2, 0, 2, 2)
        spacerItem6 = QtWidgets.QSpacerItem(196, 132, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout9.addItem(spacerItem6, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridlayout13 = QtWidgets.QGridLayout(self.tab_6)
        self.gridlayout13.setObjectName("gridlayout13")
        self.uiNIONullSettingsGroupBox = QtWidgets.QGroupBox(self.tab_6)
        self.uiNIONullSettingsGroupBox.setObjectName("uiNIONullSettingsGroupBox")
        self.gridlayout14 = QtWidgets.QGridLayout(self.uiNIONullSettingsGroupBox)
        self.gridlayout14.setObjectName("gridlayout14")
        self.label_9 = QtWidgets.QLabel(self.uiNIONullSettingsGroupBox)
        self.label_9.setObjectName("label_9")
        self.gridlayout14.addWidget(self.label_9, 0, 0, 1, 1)
        self.uiNIONullIdentiferLineEdit = QtWidgets.QLineEdit(self.uiNIONullSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNIONullIdentiferLineEdit.sizePolicy().hasHeightForWidth())
        self.uiNIONullIdentiferLineEdit.setSizePolicy(sizePolicy)
        self.uiNIONullIdentiferLineEdit.setObjectName("uiNIONullIdentiferLineEdit")
        self.gridlayout14.addWidget(self.uiNIONullIdentiferLineEdit, 1, 0, 1, 1)
        self.gridlayout13.addWidget(self.uiNIONullSettingsGroupBox, 0, 0, 1, 2)
        self.uiNIONullListGroupBox = QtWidgets.QGroupBox(self.tab_6)
        self.uiNIONullListGroupBox.setObjectName("uiNIONullListGroupBox")
        self.vboxlayout6 = QtWidgets.QVBoxLayout(self.uiNIONullListGroupBox)
        self.vboxlayout6.setObjectName("vboxlayout6")
        self.uiNIONullListWidget = QtWidgets.QListWidget(self.uiNIONullListGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNIONullListWidget.sizePolicy().hasHeightForWidth())
        self.uiNIONullListWidget.setSizePolicy(sizePolicy)
        self.uiNIONullListWidget.setObjectName("uiNIONullListWidget")
        self.vboxlayout6.addWidget(self.uiNIONullListWidget)
        self.gridlayout13.addWidget(self.uiNIONullListGroupBox, 0, 2, 3, 1)
        self.uiAddNIONullPushButton = QtWidgets.QPushButton(self.tab_6)
        self.uiAddNIONullPushButton.setObjectName("uiAddNIONullPushButton")
        self.gridlayout13.addWidget(self.uiAddNIONullPushButton, 1, 0, 1, 1)
        self.uiDeleteNIONullPushButton = QtWidgets.QPushButton(self.tab_6)
        self.uiDeleteNIONullPushButton.setEnabled(False)
        self.uiDeleteNIONullPushButton.setObjectName("uiDeleteNIONullPushButton")
        self.gridlayout13.addWidget(self.uiDeleteNIONullPushButton, 1, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 261, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout13.addItem(spacerItem7, 2, 0, 2, 2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 181, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout13.addItem(spacerItem8, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.tab_7)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.tab_7)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 399, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 1, 1, 1, 1)
        self.tabWidget.addTab(self.tab_7, "")
        self.vboxlayout.addWidget(self.tabWidget)

        self.retranslateUi(cloudConfigPageWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(cloudConfigPageWidget)

    def retranslateUi(self, cloudConfigPageWidget):
        _translate = gns3.qt.translate
        cloudConfigPageWidget.setWindowTitle(_translate("cloudConfigPageWidget", "Cloud configuration"))
        self.uiGenericEthernetGroupBox.setTitle(_translate("cloudConfigPageWidget", "Generic Ethernet NIO (Administrator or root access required)"))
        self.uiAddGenericEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Add"))
        self.uiDeleteGenericEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Delete"))
        self.uiLinuxEthernetGroupBox.setTitle(_translate("cloudConfigPageWidget", "Linux Ethernet NIO (Linux only, root access required)"))
        self.uiAddLinuxEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Add"))
        self.uiDeleteLinuxEthernetPushButton.setText(_translate("cloudConfigPageWidget", "&Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("cloudConfigPageWidget", "NIO Ethernet"))
        self.uiNIOUDPSettingsGroupBox.setTitle(_translate("cloudConfigPageWidget", "Settings"))
        self.uiLocalPortLabel.setText(_translate("cloudConfigPageWidget", "Local port:"))
        self.uiRemoteHostLabel.setText(_translate("cloudConfigPageWidget", "Remote host:"))
        self.uiRemoteHostLineEdit.setText(_translate("cloudConfigPageWidget", "127.0.0.1"))
        self.uiRemotePortLabel.setText(_translate("cloudConfigPageWidget", "Remote port:"))
        self.uiNIOUDPListGroupBox.setTitle(_translate("cloudConfigPageWidget", "NIOs"))
        self.uiAddNIOUDPPushButton.setText(_translate("cloudConfigPageWidget", "&Add"))
        self.uiDeleteNIOUDPPushButton.setText(_translate("cloudConfigPageWidget", "&Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("cloudConfigPageWidget", "NIO UDP"))
        self.uiNIOTAPGroupBox.setTitle(_translate("cloudConfigPageWidget", "TAP interface (require root access)"))
        self.uiAddNIOTAPPushButton.setText(_translate("cloudConfigPageWidget", "&Add"))
        self.uiDeleteNIOTAPPushButton.setText(_translate("cloudConfigPageWidget", "&Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("cloudConfigPageWidget", "NIO TAP"))
        self.uiNIOUNIXSettingsGroupBox.setTitle(_translate("cloudConfigPageWidget", "Settings"))
        self.uiLocalFileLabel.setText(_translate("cloudConfigPageWidget", "Local file:"))
        self.uiRemoteFileLabel.setText(_translate("cloudConfigPageWidget", "Remote file:"))
        self.uiNIOUNIXListGroupBox.setTitle(_translate("cloudConfigPageWidget", "NIOs"))
        self.uiAddNIOUNIXPushButton.setText(_translate("cloudConfigPageWidget", "&Add"))
        self.uiDeleteNIOUNIXPushButton.setText(_translate("cloudConfigPageWidget", "&Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("cloudConfigPageWidget", "NIO UNIX"))
        self.uiNIOVDESettingsGroupBox.setTitle(_translate("cloudConfigPageWidget", "Settings"))
        self.uiVDEControlFileLabel.setText(_translate("cloudConfigPageWidget", "Control file:"))
        self.uiVDELocalFileLabel.setText(_translate("cloudConfigPageWidget", "Local file:"))
        self.uiNIOVDEListGroupBox.setTitle(_translate("cloudConfigPageWidget", "NIOs"))
        self.uiAddNIOVDEPushButton.setText(_translate("cloudConfigPageWidget", "&Add"))
        self.uiDeleteNIOVDEPushButton.setText(_translate("cloudConfigPageWidget", "&Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("cloudConfigPageWidget", "NIO VDE"))
        self.uiNIONullSettingsGroupBox.setTitle(_translate("cloudConfigPageWidget", "Settings"))
        self.label_9.setText(_translate("cloudConfigPageWidget", "Identifier:"))
        self.uiNIONullListGroupBox.setTitle(_translate("cloudConfigPageWidget", "NIOs"))
        self.uiAddNIONullPushButton.setText(_translate("cloudConfigPageWidget", "&Add"))
        self.uiDeleteNIONullPushButton.setText(_translate("cloudConfigPageWidget", "&Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("cloudConfigPageWidget", "NIO NULL"))
        self.uiNameLabel.setText(_translate("cloudConfigPageWidget", "Name:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("cloudConfigPageWidget", "Misc."))
