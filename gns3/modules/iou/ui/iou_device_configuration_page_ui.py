# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iou_device_configuration_page.ui'
#
# Created: Wed May  6 14:31:56 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_iouDeviceConfigPageWidget(object):

    def setupUi(self, iouDeviceConfigPageWidget):
        iouDeviceConfigPageWidget.setObjectName("iouDeviceConfigPageWidget")
        iouDeviceConfigPageWidget.resize(392, 473)
        self.verticalLayout = QtWidgets.QVBoxLayout(iouDeviceConfigPageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiTabWidget = QtWidgets.QTabWidget(iouDeviceConfigPageWidget)
        self.uiTabWidget.setObjectName("uiTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiGeneralgroupBox = QtWidgets.QGroupBox(self.tab)
        self.uiGeneralgroupBox.setStyleSheet("")
        self.uiGeneralgroupBox.setObjectName("uiGeneralgroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiGeneralgroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiNameLabel = QtWidgets.QLabel(self.uiGeneralgroupBox)
        self.uiNameLabel.setObjectName("uiNameLabel")
        self.gridLayout.addWidget(self.uiNameLabel, 0, 0, 1, 1)
        self.uiNameLineEdit = QtWidgets.QLineEdit(self.uiGeneralgroupBox)
        self.uiNameLineEdit.setObjectName("uiNameLineEdit")
        self.gridLayout.addWidget(self.uiNameLineEdit, 0, 1, 1, 1)
        self.uiIOUImageLabel = QtWidgets.QLabel(self.uiGeneralgroupBox)
        self.uiIOUImageLabel.setObjectName("uiIOUImageLabel")
        self.gridLayout.addWidget(self.uiIOUImageLabel, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiIOUImageLineEdit = QtWidgets.QLineEdit(self.uiGeneralgroupBox)
        self.uiIOUImageLineEdit.setObjectName("uiIOUImageLineEdit")
        self.horizontalLayout_5.addWidget(self.uiIOUImageLineEdit)
        self.uiIOUImageToolButton = QtWidgets.QToolButton(self.uiGeneralgroupBox)
        self.uiIOUImageToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiIOUImageToolButton.setObjectName("uiIOUImageToolButton")
        self.horizontalLayout_5.addWidget(self.uiIOUImageToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 1, 1, 1)
        self.uiInitialConfigLabel = QtWidgets.QLabel(self.uiGeneralgroupBox)
        self.uiInitialConfigLabel.setObjectName("uiInitialConfigLabel")
        self.gridLayout.addWidget(self.uiInitialConfigLabel, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiInitialConfigLineEdit = QtWidgets.QLineEdit(self.uiGeneralgroupBox)
        self.uiInitialConfigLineEdit.setObjectName("uiInitialConfigLineEdit")
        self.horizontalLayout_4.addWidget(self.uiInitialConfigLineEdit)
        self.uiInitialConfigToolButton = QtWidgets.QToolButton(self.uiGeneralgroupBox)
        self.uiInitialConfigToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiInitialConfigToolButton.setObjectName("uiInitialConfigToolButton")
        self.horizontalLayout_4.addWidget(self.uiInitialConfigToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.uiConsolePortLabel = QtWidgets.QLabel(self.uiGeneralgroupBox)
        self.uiConsolePortLabel.setObjectName("uiConsolePortLabel")
        self.gridLayout.addWidget(self.uiConsolePortLabel, 3, 0, 1, 1)
        self.uiConsolePortSpinBox = QtWidgets.QSpinBox(self.uiGeneralgroupBox)
        self.uiConsolePortSpinBox.setMaximum(65535)
        self.uiConsolePortSpinBox.setObjectName("uiConsolePortSpinBox")
        self.gridLayout.addWidget(self.uiConsolePortSpinBox, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.uiGeneralgroupBox)
        self.uiOtherSettingsGroupBox = QtWidgets.QGroupBox(self.tab)
        self.uiOtherSettingsGroupBox.setObjectName("uiOtherSettingsGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiOtherSettingsGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiL1KeepalivesCheckBox = QtWidgets.QCheckBox(self.uiOtherSettingsGroupBox)
        self.uiL1KeepalivesCheckBox.setEnabled(True)
        self.uiL1KeepalivesCheckBox.setChecked(False)
        self.uiL1KeepalivesCheckBox.setObjectName("uiL1KeepalivesCheckBox")
        self.gridLayout_2.addWidget(self.uiL1KeepalivesCheckBox, 0, 0, 1, 2)
        self.uiDefaultValuesCheckBox = QtWidgets.QCheckBox(self.uiOtherSettingsGroupBox)
        self.uiDefaultValuesCheckBox.setChecked(True)
        self.uiDefaultValuesCheckBox.setObjectName("uiDefaultValuesCheckBox")
        self.gridLayout_2.addWidget(self.uiDefaultValuesCheckBox, 1, 0, 1, 2)
        self.uiRamLabel = QtWidgets.QLabel(self.uiOtherSettingsGroupBox)
        self.uiRamLabel.setObjectName("uiRamLabel")
        self.gridLayout_2.addWidget(self.uiRamLabel, 2, 0, 1, 1)
        self.uiRamSpinBox = QtWidgets.QSpinBox(self.uiOtherSettingsGroupBox)
        self.uiRamSpinBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRamSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRamSpinBox.setSizePolicy(sizePolicy)
        self.uiRamSpinBox.setMinimum(32)
        self.uiRamSpinBox.setMaximum(65535)
        self.uiRamSpinBox.setSingleStep(32)
        self.uiRamSpinBox.setProperty("value", 128)
        self.uiRamSpinBox.setObjectName("uiRamSpinBox")
        self.gridLayout_2.addWidget(self.uiRamSpinBox, 2, 1, 1, 1)
        self.uiNvramLabel = QtWidgets.QLabel(self.uiOtherSettingsGroupBox)
        self.uiNvramLabel.setObjectName("uiNvramLabel")
        self.gridLayout_2.addWidget(self.uiNvramLabel, 3, 0, 1, 1)
        self.uiNvramSpinBox = QtWidgets.QSpinBox(self.uiOtherSettingsGroupBox)
        self.uiNvramSpinBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiNvramSpinBox.sizePolicy().hasHeightForWidth())
        self.uiNvramSpinBox.setSizePolicy(sizePolicy)
        self.uiNvramSpinBox.setMinimum(32)
        self.uiNvramSpinBox.setMaximum(65535)
        self.uiNvramSpinBox.setSingleStep(32)
        self.uiNvramSpinBox.setProperty("value", 128)
        self.uiNvramSpinBox.setObjectName("uiNvramSpinBox")
        self.gridLayout_2.addWidget(self.uiNvramSpinBox, 3, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.uiOtherSettingsGroupBox)
        spacerItem = QtWidgets.QSpacerItem(260, 301, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.uiTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.uiEthernetAdaptersLabel = QtWidgets.QLabel(self.groupBox)
        self.uiEthernetAdaptersLabel.setObjectName("uiEthernetAdaptersLabel")
        self.gridLayout_3.addWidget(self.uiEthernetAdaptersLabel, 0, 0, 1, 1)
        self.uiEthernetAdaptersSpinBox = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiEthernetAdaptersSpinBox.sizePolicy().hasHeightForWidth())
        self.uiEthernetAdaptersSpinBox.setSizePolicy(sizePolicy)
        self.uiEthernetAdaptersSpinBox.setMaximum(16)
        self.uiEthernetAdaptersSpinBox.setSingleStep(2)
        self.uiEthernetAdaptersSpinBox.setObjectName("uiEthernetAdaptersSpinBox")
        self.gridLayout_3.addWidget(self.uiEthernetAdaptersSpinBox, 0, 1, 1, 1)
        self.uiSerialAdaptersLabel = QtWidgets.QLabel(self.groupBox)
        self.uiSerialAdaptersLabel.setObjectName("uiSerialAdaptersLabel")
        self.gridLayout_3.addWidget(self.uiSerialAdaptersLabel, 1, 0, 1, 1)
        self.uiSerialAdaptersSpinBox = QtWidgets.QSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiSerialAdaptersSpinBox.sizePolicy().hasHeightForWidth())
        self.uiSerialAdaptersSpinBox.setSizePolicy(sizePolicy)
        self.uiSerialAdaptersSpinBox.setMaximum(16)
        self.uiSerialAdaptersSpinBox.setSingleStep(2)
        self.uiSerialAdaptersSpinBox.setObjectName("uiSerialAdaptersSpinBox")
        self.gridLayout_3.addWidget(self.uiSerialAdaptersSpinBox, 1, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 347, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 1, 0, 1, 1)
        self.uiTabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.uiTabWidget)

        self.retranslateUi(iouDeviceConfigPageWidget)
        self.uiTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(iouDeviceConfigPageWidget)

    def retranslateUi(self, iouDeviceConfigPageWidget):
        _translate = gns3.qt.translate
        iouDeviceConfigPageWidget.setWindowTitle(_translate("iouDeviceConfigPageWidget", "IOU device configuration"))
        self.uiGeneralgroupBox.setTitle(_translate("iouDeviceConfigPageWidget", "General"))
        self.uiNameLabel.setText(_translate("iouDeviceConfigPageWidget", "Name:"))
        self.uiIOUImageLabel.setText(_translate("iouDeviceConfigPageWidget", "IOU image path:"))
        self.uiIOUImageToolButton.setText(_translate("iouDeviceConfigPageWidget", "&Browse..."))
        self.uiInitialConfigLabel.setText(_translate("iouDeviceConfigPageWidget", "Initial startup-config:"))
        self.uiInitialConfigToolButton.setText(_translate("iouDeviceConfigPageWidget", "&Browse..."))
        self.uiConsolePortLabel.setText(_translate("iouDeviceConfigPageWidget", "Console port:"))
        self.uiOtherSettingsGroupBox.setTitle(_translate("iouDeviceConfigPageWidget", "Other settings"))
        self.uiL1KeepalivesCheckBox.setText(_translate("iouDeviceConfigPageWidget", "Enable layer 1 keepalive messages (testing only)"))
        self.uiDefaultValuesCheckBox.setText(_translate("iouDeviceConfigPageWidget", "Use default IOU values for memories"))
        self.uiRamLabel.setText(_translate("iouDeviceConfigPageWidget", "RAM size:"))
        self.uiRamSpinBox.setSuffix(_translate("iouDeviceConfigPageWidget", " MB"))
        self.uiNvramLabel.setText(_translate("iouDeviceConfigPageWidget", "NVRAM size:"))
        self.uiNvramSpinBox.setSuffix(_translate("iouDeviceConfigPageWidget", " KB"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab), _translate("iouDeviceConfigPageWidget", "General settings"))
        self.groupBox.setTitle(_translate("iouDeviceConfigPageWidget", "Adapters"))
        self.uiEthernetAdaptersLabel.setText(_translate("iouDeviceConfigPageWidget", "Ethernet adapters:"))
        self.uiEthernetAdaptersSpinBox.setToolTip(_translate("iouDeviceConfigPageWidget", "1 adapter equals 4 Ethernet interfaces"))
        self.uiSerialAdaptersLabel.setText(_translate("iouDeviceConfigPageWidget", "Serial adapters:"))
        self.uiSerialAdaptersSpinBox.setToolTip(_translate("iouDeviceConfigPageWidget", "1 adapter equals 4 serial interfaces"))
        self.uiTabWidget.setTabText(self.uiTabWidget.indexOf(self.tab_2), _translate("iouDeviceConfigPageWidget", "Network"))
