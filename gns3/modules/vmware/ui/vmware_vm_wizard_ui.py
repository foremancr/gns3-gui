# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vmware_vm_wizard.ui'
#
# Created: Wed May  6 14:31:58 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

import gns3.qt
from gns3.qt import QtCore, QtGui, QtWidgets


class Ui_VMwareVMWizard(object):

    def setupUi(self, VMwareVMWizard):
        VMwareVMWizard.setObjectName("VMwareVMWizard")
        VMwareVMWizard.resize(514, 367)
        VMwareVMWizard.setModal(True)
        self.uiServerWizardPage = QtWidgets.QWizardPage()
        self.uiServerWizardPage.setObjectName("uiServerWizardPage")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiServerWizardPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.uiServerTypeGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiServerTypeGroupBox.setObjectName("uiServerTypeGroupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.uiServerTypeGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiRemoteRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiRemoteRadioButton.setChecked(True)
        self.uiRemoteRadioButton.setObjectName("uiRemoteRadioButton")
        self.horizontalLayout.addWidget(self.uiRemoteRadioButton)
        self.uiCloudRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiCloudRadioButton.setObjectName("uiCloudRadioButton")
        self.horizontalLayout.addWidget(self.uiCloudRadioButton)
        self.uiLocalRadioButton = QtWidgets.QRadioButton(self.uiServerTypeGroupBox)
        self.uiLocalRadioButton.setObjectName("uiLocalRadioButton")
        self.horizontalLayout.addWidget(self.uiLocalRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_2.addWidget(self.uiServerTypeGroupBox, 0, 0, 1, 1)
        self.uiRemoteServersGroupBox = QtWidgets.QGroupBox(self.uiServerWizardPage)
        self.uiRemoteServersGroupBox.setObjectName("uiRemoteServersGroupBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.uiRemoteServersGroupBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.uiRemoteServersComboBox = QtWidgets.QComboBox(self.uiRemoteServersGroupBox)
        self.uiRemoteServersComboBox.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersComboBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersComboBox.setSizePolicy(sizePolicy)
        self.uiRemoteServersComboBox.setObjectName("uiRemoteServersComboBox")
        self.gridLayout_8.addWidget(self.uiRemoteServersComboBox, 0, 1, 1, 1)
        self.uiRemoteServersLabel = QtWidgets.QLabel(self.uiRemoteServersGroupBox)
        self.uiRemoteServersLabel.setObjectName("uiRemoteServersLabel")
        self.gridLayout_8.addWidget(self.uiRemoteServersLabel, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.uiRemoteServersGroupBox, 1, 0, 1, 1)
        VMwareVMWizard.addPage(self.uiServerWizardPage)
        self.uiVirtualBoxWizardPage = QtWidgets.QWizardPage()
        self.uiVirtualBoxWizardPage.setObjectName("uiVirtualBoxWizardPage")
        self.gridLayout = QtWidgets.QGridLayout(self.uiVirtualBoxWizardPage)
        self.gridLayout.setObjectName("gridLayout")
        self.uiVMListLabel = QtWidgets.QLabel(self.uiVirtualBoxWizardPage)
        self.uiVMListLabel.setObjectName("uiVMListLabel")
        self.gridLayout.addWidget(self.uiVMListLabel, 0, 0, 1, 1)
        self.uiVMListComboBox = QtWidgets.QComboBox(self.uiVirtualBoxWizardPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiVMListComboBox.sizePolicy().hasHeightForWidth())
        self.uiVMListComboBox.setSizePolicy(sizePolicy)
        self.uiVMListComboBox.setObjectName("uiVMListComboBox")
        self.gridLayout.addWidget(self.uiVMListComboBox, 0, 1, 1, 1)
        self.uiBaseVMCheckBox = QtWidgets.QCheckBox(self.uiVirtualBoxWizardPage)
        self.uiBaseVMCheckBox.setEnabled(True)
        self.uiBaseVMCheckBox.setObjectName("uiBaseVMCheckBox")
        self.gridLayout.addWidget(self.uiBaseVMCheckBox, 1, 0, 1, 2)
        VMwareVMWizard.addPage(self.uiVirtualBoxWizardPage)

        self.retranslateUi(VMwareVMWizard)
        QtCore.QMetaObject.connectSlotsByName(VMwareVMWizard)

    def retranslateUi(self, VMwareVMWizard):
        _translate = gns3.qt.translate
        VMwareVMWizard.setWindowTitle(_translate("VMwareVMWizard", "New VMware VM template"))
        self.uiServerWizardPage.setTitle(_translate("VMwareVMWizard", "Server"))
        self.uiServerWizardPage.setSubTitle(_translate("VMwareVMWizard", "Please choose a server type to run your new VMware VM."))
        self.uiServerTypeGroupBox.setTitle(_translate("VMwareVMWizard", "Server type"))
        self.uiRemoteRadioButton.setText(_translate("VMwareVMWizard", "Remote"))
        self.uiCloudRadioButton.setText(_translate("VMwareVMWizard", "Cloud"))
        self.uiLocalRadioButton.setText(_translate("VMwareVMWizard", "Local"))
        self.uiRemoteServersGroupBox.setTitle(_translate("VMwareVMWizard", "Remote servers"))
        self.uiRemoteServersLabel.setText(_translate("VMwareVMWizard", "Run on server:"))
        self.uiVirtualBoxWizardPage.setTitle(_translate("VMwareVMWizard", "VMware Virtual Machine"))
        self.uiVirtualBoxWizardPage.setSubTitle(_translate("VMwareVMWizard", "Please choose a VMware virtual machine from the list."))
        self.uiVMListLabel.setText(_translate("VMwareVMWizard", "VM list:"))
        self.uiBaseVMCheckBox.setText(_translate("VMwareVMWizard", "Use as a linked base VM (experimental)"))
