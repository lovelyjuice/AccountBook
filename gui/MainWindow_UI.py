# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_UI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(786, 588)
        Form.setMaximumSize(QtCore.QSize(65535, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mbrCBox = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mbrCBox.sizePolicy().hasHeightForWidth())
        self.mbrCBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.mbrCBox.setFont(font)
        self.mbrCBox.setEditable(False)
        self.mbrCBox.setCurrentText("")
        self.mbrCBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.mbrCBox.setObjectName("mbrCBox")
        self.verticalLayout_2.addWidget(self.mbrCBox)
        self.typeCBox = QtWidgets.QComboBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeCBox.sizePolicy().hasHeightForWidth())
        self.typeCBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.typeCBox.setFont(font)
        self.typeCBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.typeCBox.setObjectName("typeCBox")
        self.verticalLayout_2.addWidget(self.typeCBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.startDateEdt = QtWidgets.QDateEdit(self.groupBox)
        self.startDateEdt.setCalendarPopup(True)
        self.startDateEdt.setObjectName("startDateEdt")
        self.verticalLayout_4.addWidget(self.startDateEdt)
        self.endDateEdt = QtWidgets.QDateEdit(self.groupBox)
        self.endDateEdt.setCalendarPopup(True)
        self.endDateEdt.setObjectName("endDateEdt")
        self.verticalLayout_4.addWidget(self.endDateEdt)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.filtrateBtn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filtrateBtn.sizePolicy().hasHeightForWidth())
        self.filtrateBtn.setSizePolicy(sizePolicy)
        self.filtrateBtn.setObjectName("filtrateBtn")
        self.verticalLayout_5.addWidget(self.filtrateBtn)
        self.revertBtn = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.revertBtn.sizePolicy().hasHeightForWidth())
        self.revertBtn.setSizePolicy(sizePolicy)
        self.revertBtn.setObjectName("revertBtn")
        self.verticalLayout_5.addWidget(self.revertBtn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(355, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.searchEdit = QtWidgets.QLineEdit(self.groupBox)
        self.searchEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.searchEdit.setClearButtonEnabled(True)
        self.searchEdit.setObjectName("searchEdit")
        self.horizontalLayout_2.addWidget(self.searchEdit)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chargeTable = QtWidgets.QTableWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chargeTable.sizePolicy().hasHeightForWidth())
        self.chargeTable.setSizePolicy(sizePolicy)
        self.chargeTable.setMaximumSize(QtCore.QSize(65535, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.chargeTable.setFont(font)
        self.chargeTable.setDragEnabled(False)
        self.chargeTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.chargeTable.setColumnCount(6)
        self.chargeTable.setObjectName("chargeTable")
        self.chargeTable.setRowCount(0)
        self.chargeTable.horizontalHeader().setCascadingSectionResizes(True)
        self.chargeTable.horizontalHeader().setStretchLastSection(True)
        self.chargeTable.verticalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.chargeTable)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.chargeBtn = QtWidgets.QPushButton(Form)
        self.chargeBtn.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.chargeBtn.setFont(font)
        self.chargeBtn.setAutoFillBackground(False)
        self.chargeBtn.setCheckable(False)
        self.chargeBtn.setObjectName("chargeBtn")
        self.verticalLayout_6.addWidget(self.chargeBtn)
        self.delChargeBtn = QtWidgets.QPushButton(Form)
        self.delChargeBtn.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.delChargeBtn.setFont(font)
        self.delChargeBtn.setAutoFillBackground(False)
        self.delChargeBtn.setCheckable(False)
        self.delChargeBtn.setObjectName("delChargeBtn")
        self.verticalLayout_6.addWidget(self.delChargeBtn)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.membersTab = QtWidgets.QWidget()
        self.membersTab.setObjectName("membersTab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.membersTab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.membersTab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.memberTable = QtWidgets.QTableWidget(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.memberTable.sizePolicy().hasHeightForWidth())
        self.memberTable.setSizePolicy(sizePolicy)
        self.memberTable.setMinimumSize(QtCore.QSize(200, 0))
        self.memberTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.memberTable.setShowGrid(True)
        self.memberTable.setGridStyle(QtCore.Qt.SolidLine)
        self.memberTable.setRowCount(0)
        self.memberTable.setColumnCount(3)
        self.memberTable.setObjectName("memberTable")
        self.memberTable.horizontalHeader().setStretchLastSection(True)
        self.memberTable.verticalHeader().setVisible(False)
        self.horizontalLayout_5.addWidget(self.memberTable)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.addMbrBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.addMbrBtn.setObjectName("addMbrBtn")
        self.verticalLayout_7.addWidget(self.addMbrBtn)
        self.delMbrBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.delMbrBtn.setObjectName("delMbrBtn")
        self.verticalLayout_7.addWidget(self.delMbrBtn)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.membersTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.typeList = QtWidgets.QListWidget(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typeList.sizePolicy().hasHeightForWidth())
        self.typeList.setSizePolicy(sizePolicy)
        self.typeList.setMaximumSize(QtCore.QSize(100, 16777215))
        self.typeList.setObjectName("typeList")
        self.horizontalLayout_4.addWidget(self.typeList)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.addTypeBtn = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTypeBtn.sizePolicy().hasHeightForWidth())
        self.addTypeBtn.setSizePolicy(sizePolicy)
        self.addTypeBtn.setObjectName("addTypeBtn")
        self.verticalLayout_8.addWidget(self.addTypeBtn)
        self.delTypeBtn = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delTypeBtn.sizePolicy().hasHeightForWidth())
        self.delTypeBtn.setSizePolicy(sizePolicy)
        self.delTypeBtn.setObjectName("delTypeBtn")
        self.verticalLayout_8.addWidget(self.delTypeBtn)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_8)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        spacerItem7 = QtWidgets.QSpacerItem(435, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.tabWidget.addTab(self.membersTab, "")
        self.statisticsTab = QtWidgets.QWidget()
        self.statisticsTab.setObjectName("statisticsTab")
        self.pushButton = QtWidgets.QPushButton(self.statisticsTab)
        self.pushButton.setGeometry(QtCore.QRect(9, 47, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.statisticsTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.verticalLayout.setStretch(1, 8)
        self.verticalLayout.setStretch(2, 5)
        self.label_5.setBuddy(self.mbrCBox)
        self.label_6.setBuddy(self.typeCBox)
        self.label_3.setBuddy(self.startDateEdt)
        self.label_4.setBuddy(self.endDateEdt)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "过滤器"))
        self.label_5.setText(_translate("Form", "成员："))
        self.label_6.setText(_translate("Form", "类型："))
        self.label_3.setText(_translate("Form", "起始时间"))
        self.label_4.setText(_translate("Form", "结束时间"))
        self.filtrateBtn.setText(_translate("Form", "筛选"))
        self.revertBtn.setText(_translate("Form", "重置"))
        self.searchEdit.setPlaceholderText(_translate("Form", "搜索备注里的内容"))
        self.chargeTable.setSortingEnabled(True)
        self.chargeBtn.setText(_translate("Form", "+"))
        self.delChargeBtn.setText(_translate("Form", "-"))
        self.groupBox_3.setTitle(_translate("Form", "成员"))
        self.memberTable.setSortingEnabled(True)
        self.addMbrBtn.setText(_translate("Form", "添加"))
        self.delMbrBtn.setText(_translate("Form", "删除"))
        self.groupBox_2.setTitle(_translate("Form", "类型"))
        self.typeList.setSortingEnabled(True)
        self.addTypeBtn.setText(_translate("Form", "添加"))
        self.delTypeBtn.setText(_translate("Form", "删除"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.membersTab), _translate("Form", "管理"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statisticsTab), _translate("Form", "统计信息"))

