# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame_relay_switch_configuration_page.ui'
#
# Created: Wed May  6 14:31:56 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_frameRelaySwitchConfigPageWidget(object):

    def setupUi(self, frameRelaySwitchConfigPageWidget):
        frameRelaySwitchConfigPageWidget.setObjectName("frameRelaySwitchConfigPageWidget")
        frameRelaySwitchConfigPageWidget.resize(499, 405)
        self.gridLayout_2 = QtWidgets.QGridLayout(frameRelaySwitchConfigPageWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiGeneralGroupBox = QtWidgets.QGroupBox(frameRelaySwitchConfigPageWidget)
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
        self.uiFrameRelayMappingGroupBox = QtWidgets.QGroupBox(frameRelaySwitchConfigPageWidget)
        self.uiFrameRelayMappingGroupBox.setObjectName("uiFrameRelayMappingGroupBox")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.uiFrameRelayMappingGroupBox)
        self.vboxlayout.setObjectName("vboxlayout")
        self.uiMappingTreeWidget = QtWidgets.QTreeWidget(self.uiFrameRelayMappingGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiMappingTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiMappingTreeWidget.setSizePolicy(sizePolicy)
        self.uiMappingTreeWidget.setRootIsDecorated(False)
        self.uiMappingTreeWidget.setObjectName("uiMappingTreeWidget")
        self.vboxlayout.addWidget(self.uiMappingTreeWidget)
        self.gridLayout_2.addWidget(self.uiFrameRelayMappingGroupBox, 0, 2, 4, 1)
        self.uiFrameRelaySourceGroupBox = QtWidgets.QGroupBox(frameRelaySwitchConfigPageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiFrameRelaySourceGroupBox.sizePolicy().hasHeightForWidth())
        self.uiFrameRelaySourceGroupBox.setSizePolicy(sizePolicy)
        self.uiFrameRelaySourceGroupBox.setObjectName("uiFrameRelaySourceGroupBox")
        self.gridlayout = QtWidgets.QGridLayout(self.uiFrameRelaySourceGroupBox)
        self.gridlayout.setObjectName("gridlayout")
        self.uiSourcePortLabel = QtWidgets.QLabel(self.uiFrameRelaySourceGroupBox)
        self.uiSourcePortLabel.setObjectName("uiSourcePortLabel")
        self.gridlayout.addWidget(self.uiSourcePortLabel, 0, 0, 1, 1)
        self.uiSourcePortSpinBox = QtWidgets.QSpinBox(self.uiFrameRelaySourceGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSourcePortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiSourcePortSpinBox.setSizePolicy(sizePolicy)
        self.uiSourcePortSpinBox.setMinimum(0)
        self.uiSourcePortSpinBox.setMaximum(65535)
        self.uiSourcePortSpinBox.setProperty("value", 1)
        self.uiSourcePortSpinBox.setObjectName("uiSourcePortSpinBox")
        self.gridlayout.addWidget(self.uiSourcePortSpinBox, 0, 1, 1, 1)
        self.uiSourceDLCILabel = QtWidgets.QLabel(self.uiFrameRelaySourceGroupBox)
        self.uiSourceDLCILabel.setObjectName("uiSourceDLCILabel")
        self.gridlayout.addWidget(self.uiSourceDLCILabel, 1, 0, 1, 1)
        self.uiSourceDLCISpinBox = QtWidgets.QSpinBox(self.uiFrameRelaySourceGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSourceDLCISpinBox.sizePolicy().hasHeightForWidth())
        self.uiSourceDLCISpinBox.setSizePolicy(sizePolicy)
        self.uiSourceDLCISpinBox.setMaximum(65535)
        self.uiSourceDLCISpinBox.setProperty("value", 101)
        self.uiSourceDLCISpinBox.setObjectName("uiSourceDLCISpinBox")
        self.gridlayout.addWidget(self.uiSourceDLCISpinBox, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.uiFrameRelaySourceGroupBox, 1, 0, 1, 2)
        self.uiFrameRelayDestinationGroupBox = QtWidgets.QGroupBox(frameRelaySwitchConfigPageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiFrameRelayDestinationGroupBox.sizePolicy().hasHeightForWidth())
        self.uiFrameRelayDestinationGroupBox.setSizePolicy(sizePolicy)
        self.uiFrameRelayDestinationGroupBox.setObjectName("uiFrameRelayDestinationGroupBox")
        self.gridlayout1 = QtWidgets.QGridLayout(self.uiFrameRelayDestinationGroupBox)
        self.gridlayout1.setObjectName("gridlayout1")
        self.uiDestinationPortLabel = QtWidgets.QLabel(self.uiFrameRelayDestinationGroupBox)
        self.uiDestinationPortLabel.setObjectName("uiDestinationPortLabel")
        self.gridlayout1.addWidget(self.uiDestinationPortLabel, 0, 0, 1, 1)
        self.uiDestinationPortSpinBox = QtWidgets.QSpinBox(self.uiFrameRelayDestinationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiDestinationPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiDestinationPortSpinBox.setSizePolicy(sizePolicy)
        self.uiDestinationPortSpinBox.setMinimum(0)
        self.uiDestinationPortSpinBox.setMaximum(65535)
        self.uiDestinationPortSpinBox.setProperty("value", 10)
        self.uiDestinationPortSpinBox.setObjectName("uiDestinationPortSpinBox")
        self.gridlayout1.addWidget(self.uiDestinationPortSpinBox, 0, 1, 1, 1)
        self.uiDestinationDLCILabel = QtWidgets.QLabel(self.uiFrameRelayDestinationGroupBox)
        self.uiDestinationDLCILabel.setObjectName("uiDestinationDLCILabel")
        self.gridlayout1.addWidget(self.uiDestinationDLCILabel, 1, 0, 1, 1)
        self.uiDestinationDLCISpinBox = QtWidgets.QSpinBox(self.uiFrameRelayDestinationGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiDestinationDLCISpinBox.sizePolicy().hasHeightForWidth())
        self.uiDestinationDLCISpinBox.setSizePolicy(sizePolicy)
        self.uiDestinationDLCISpinBox.setMaximum(65535)
        self.uiDestinationDLCISpinBox.setProperty("value", 202)
        self.uiDestinationDLCISpinBox.setObjectName("uiDestinationDLCISpinBox")
        self.gridlayout1.addWidget(self.uiDestinationDLCISpinBox, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.uiFrameRelayDestinationGroupBox, 2, 0, 1, 2)
        self.uiAddPushButton = QtWidgets.QPushButton(frameRelaySwitchConfigPageWidget)
        self.uiAddPushButton.setObjectName("uiAddPushButton")
        self.gridLayout_2.addWidget(self.uiAddPushButton, 3, 0, 1, 1)
        self.uiDeletePushButton = QtWidgets.QPushButton(frameRelaySwitchConfigPageWidget)
        self.uiDeletePushButton.setEnabled(False)
        self.uiDeletePushButton.setObjectName("uiDeletePushButton")
        self.gridLayout_2.addWidget(self.uiDeletePushButton, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 2, 1, 1)

        self.retranslateUi(frameRelaySwitchConfigPageWidget)
        QtCore.QMetaObject.connectSlotsByName(frameRelaySwitchConfigPageWidget)
        frameRelaySwitchConfigPageWidget.setTabOrder(self.uiSourcePortSpinBox, self.uiSourceDLCISpinBox)
        frameRelaySwitchConfigPageWidget.setTabOrder(self.uiSourceDLCISpinBox, self.uiDestinationPortSpinBox)
        frameRelaySwitchConfigPageWidget.setTabOrder(self.uiDestinationPortSpinBox, self.uiDestinationDLCISpinBox)
        frameRelaySwitchConfigPageWidget.setTabOrder(self.uiDestinationDLCISpinBox, self.uiAddPushButton)
        frameRelaySwitchConfigPageWidget.setTabOrder(self.uiAddPushButton, self.uiDeletePushButton)

    def retranslateUi(self, frameRelaySwitchConfigPageWidget):
        _translate = gns3.qt.translate
        frameRelaySwitchConfigPageWidget.setWindowTitle(_translate("frameRelaySwitchConfigPageWidget", "Frame Relay Switch"))
        self.uiGeneralGroupBox.setTitle(_translate("frameRelaySwitchConfigPageWidget", "General"))
        self.uiNameLabel.setText(_translate("frameRelaySwitchConfigPageWidget", "Name:"))
        self.uiFrameRelayMappingGroupBox.setTitle(_translate("frameRelaySwitchConfigPageWidget", "Mapping"))
        self.uiMappingTreeWidget.headerItem().setText(0, _translate("frameRelaySwitchConfigPageWidget", "Port:DLCI"))
        self.uiMappingTreeWidget.headerItem().setText(1, _translate("frameRelaySwitchConfigPageWidget", "Port:DLCI"))
        self.uiFrameRelaySourceGroupBox.setTitle(_translate("frameRelaySwitchConfigPageWidget", "Source"))
        self.uiSourcePortLabel.setText(_translate("frameRelaySwitchConfigPageWidget", "Port:"))
        self.uiSourceDLCILabel.setText(_translate("frameRelaySwitchConfigPageWidget", "DLCI:"))
        self.uiFrameRelayDestinationGroupBox.setTitle(_translate("frameRelaySwitchConfigPageWidget", "Destination"))
        self.uiDestinationPortLabel.setText(_translate("frameRelaySwitchConfigPageWidget", "Port:"))
        self.uiDestinationDLCILabel.setText(_translate("frameRelaySwitchConfigPageWidget", "DLCI:"))
        self.uiAddPushButton.setText(_translate("frameRelaySwitchConfigPageWidget", "&Add"))
        self.uiDeletePushButton.setText(_translate("frameRelaySwitchConfigPageWidget", "&Delete"))
