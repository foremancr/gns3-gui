# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ethernet_switch_configuration_page.ui'
#
# Created: Wed May  6 14:31:55 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_ethernetSwitchConfigPageWidget(object):

    def setupUi(self, ethernetSwitchConfigPageWidget):
        ethernetSwitchConfigPageWidget.setObjectName("ethernetSwitchConfigPageWidget")
        ethernetSwitchConfigPageWidget.resize(397, 315)
        self.gridLayout_2 = QtWidgets.QGridLayout(ethernetSwitchConfigPageWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiGeneralGroupBox = QtWidgets.QGroupBox(ethernetSwitchConfigPageWidget)
        self.uiGeneralGroupBox.setObjectName("uiGeneralGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiGeneralGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.uiGeneralGroupBox)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.uiGeneralGroupBox)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.uiGeneralGroupBox, 0, 0, 1, 2)
        self.uiEthernetSwitchPortsGroupBox = QtWidgets.QGroupBox(ethernetSwitchConfigPageWidget)
        self.uiEthernetSwitchPortsGroupBox.setObjectName("uiEthernetSwitchPortsGroupBox")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.uiEthernetSwitchPortsGroupBox)
        self.vboxlayout.setObjectName("vboxlayout")
        self.uiPortsTreeWidget = QtWidgets.QTreeWidget(self.uiEthernetSwitchPortsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiPortsTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiPortsTreeWidget.setSizePolicy(sizePolicy)
        self.uiPortsTreeWidget.setRootIsDecorated(False)
        self.uiPortsTreeWidget.setObjectName("uiPortsTreeWidget")
        self.vboxlayout.addWidget(self.uiPortsTreeWidget)
        self.gridLayout_2.addWidget(self.uiEthernetSwitchPortsGroupBox, 0, 2, 3, 1)
        self.uiEthernetSwitchSettingsGroupBox = QtWidgets.QGroupBox(ethernetSwitchConfigPageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiEthernetSwitchSettingsGroupBox.sizePolicy().hasHeightForWidth())
        self.uiEthernetSwitchSettingsGroupBox.setSizePolicy(sizePolicy)
        self.uiEthernetSwitchSettingsGroupBox.setObjectName("uiEthernetSwitchSettingsGroupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.uiEthernetSwitchSettingsGroupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(self.uiEthernetSwitchSettingsGroupBox)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.uiPortSpinBox = QtWidgets.QSpinBox(self.uiEthernetSwitchSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiPortSpinBox.setSizePolicy(sizePolicy)
        self.uiPortSpinBox.setMinimum(1)
        self.uiPortSpinBox.setMaximum(65535)
        self.uiPortSpinBox.setProperty("value", 1)
        self.uiPortSpinBox.setObjectName("uiPortSpinBox")
        self.gridlayout.addWidget(self.uiPortSpinBox, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.uiEthernetSwitchSettingsGroupBox)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.uiVlanSpinBox = QtWidgets.QSpinBox(self.uiEthernetSwitchSettingsGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVlanSpinBox.sizePolicy().hasHeightForWidth())
        self.uiVlanSpinBox.setSizePolicy(sizePolicy)
        self.uiVlanSpinBox.setMinimum(1)
        self.uiVlanSpinBox.setMaximum(65535)
        self.uiVlanSpinBox.setProperty("value", 1)
        self.uiVlanSpinBox.setObjectName("uiVlanSpinBox")
        self.gridlayout.addWidget(self.uiVlanSpinBox, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.uiEthernetSwitchSettingsGroupBox)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.uiPortTypeComboBox = QtWidgets.QComboBox(self.uiEthernetSwitchSettingsGroupBox)
        self.uiPortTypeComboBox.setObjectName("uiPortTypeComboBox")
        self.uiPortTypeComboBox.addItem("")
        self.uiPortTypeComboBox.addItem("")
        self.uiPortTypeComboBox.addItem("")
        self.gridlayout.addWidget(self.uiPortTypeComboBox, 2, 1, 1, 1)
        self.gridLayout_2.addWidget(self.uiEthernetSwitchSettingsGroupBox, 1, 0, 1, 2)
        self.uiAddPushButton = QtWidgets.QPushButton(ethernetSwitchConfigPageWidget)
        self.uiAddPushButton.setObjectName("uiAddPushButton")
        self.gridLayout_2.addWidget(self.uiAddPushButton, 2, 0, 1, 1)
        self.uiDeletePushButton = QtWidgets.QPushButton(ethernetSwitchConfigPageWidget)
        self.uiDeletePushButton.setEnabled(False)
        self.uiDeletePushButton.setObjectName("uiDeletePushButton")
        self.gridLayout_2.addWidget(self.uiDeletePushButton, 2, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 71, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)

        self.retranslateUi(ethernetSwitchConfigPageWidget)
        QtCore.QMetaObject.connectSlotsByName(ethernetSwitchConfigPageWidget)
        ethernetSwitchConfigPageWidget.setTabOrder(self.uiPortSpinBox, self.uiVlanSpinBox)
        ethernetSwitchConfigPageWidget.setTabOrder(self.uiVlanSpinBox, self.uiPortTypeComboBox)
        ethernetSwitchConfigPageWidget.setTabOrder(self.uiPortTypeComboBox, self.uiAddPushButton)
        ethernetSwitchConfigPageWidget.setTabOrder(self.uiAddPushButton, self.uiDeletePushButton)
        ethernetSwitchConfigPageWidget.setTabOrder(self.uiDeletePushButton, self.uiPortsTreeWidget)

    def retranslateUi(self, ethernetSwitchConfigPageWidget):
        _translate = gns3.qt.translate
        ethernetSwitchConfigPageWidget.setWindowTitle(_translate("ethernetSwitchConfigPageWidget", "Ethernet switch configuration"))
        self.uiGeneralGroupBox.setTitle(_translate("ethernetSwitchConfigPageWidget", "General"))
        self.uiNameLabel.setText(_translate("ethernetSwitchConfigPageWidget", "Name:"))
        self.uiEthernetSwitchPortsGroupBox.setTitle(_translate("ethernetSwitchConfigPageWidget", "Ports"))
        self.uiPortsTreeWidget.headerItem().setText(0, _translate("ethernetSwitchConfigPageWidget", "Port"))
        self.uiPortsTreeWidget.headerItem().setText(1, _translate("ethernetSwitchConfigPageWidget", "VLAN"))
        self.uiPortsTreeWidget.headerItem().setText(2, _translate("ethernetSwitchConfigPageWidget", "Type"))
        self.uiEthernetSwitchSettingsGroupBox.setTitle(_translate("ethernetSwitchConfigPageWidget", "Settings"))
        self.label.setText(_translate("ethernetSwitchConfigPageWidget", "Port:"))
        self.label_3.setText(_translate("ethernetSwitchConfigPageWidget", "VLAN:"))
        self.label_2.setText(_translate("ethernetSwitchConfigPageWidget", "Type:"))
        self.uiPortTypeComboBox.setItemText(0, _translate("ethernetSwitchConfigPageWidget", "access"))
        self.uiPortTypeComboBox.setItemText(1, _translate("ethernetSwitchConfigPageWidget", "dot1q"))
        self.uiPortTypeComboBox.setItemText(2, _translate("ethernetSwitchConfigPageWidget", "qinq"))
        self.uiAddPushButton.setText(_translate("ethernetSwitchConfigPageWidget", "&Add"))
        self.uiDeletePushButton.setText(_translate("ethernetSwitchConfigPageWidget", "&Delete"))
