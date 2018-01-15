# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FunLogUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgFunLog(object):
    def setupUi(self, dlgFunLog):
        dlgFunLog.setObjectName("dlgFunLog")
        dlgFunLog.resize(554, 426)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dlgFunLog.sizePolicy().hasHeightForWidth())
        dlgFunLog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/WebSerTestIcon/browser_window_38.581560283688px_1204645_easyicon.net.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgFunLog.setWindowIcon(icon)
        self.gridLayout_5 = QtWidgets.QGridLayout(dlgFunLog)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.widget = QtWidgets.QWidget(dlgFunLog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.tableFunInfo = QtWidgets.QTableWidget(self.groupBox)
        self.tableFunInfo.setObjectName("tableFunInfo")
        self.tableFunInfo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableFunInfo.setAlternatingRowColors(True)
        self.tableFunInfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableFunInfo.setColumnCount(2)
        self.tableFunInfo.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch) # 将table的第一列设置为自适应
        self.tableFunInfo.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.tableFunInfo.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableFunInfo.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableFunInfo.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tableFunInfo, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(dlgFunLog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.editWebAddress = QtWidgets.QLineEdit(self.widget_2)
        self.editWebAddress.setObjectName("editWebAddress")
        self.editWebAddress.setReadOnly(True)
        self.horizontalLayout.addWidget(self.editWebAddress)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget_2)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabParamInfo = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabParamInfo.setObjectName("tabParamInfo")
        self.gridLayout_3.addWidget(self.tabParamInfo, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.widget_2, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.buttonCancel = QtWidgets.QPushButton(dlgFunLog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonCancel.sizePolicy().hasHeightForWidth())
        self.buttonCancel.setSizePolicy(sizePolicy)
        self.buttonCancel.setObjectName("buttonCancel")
        self.horizontalLayout_2.addWidget(self.buttonCancel)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.retranslateUi(dlgFunLog)
        self.tabParamInfo.setCurrentIndex(0)
        self.buttonCancel.clicked['bool'].connect(dlgFunLog.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgFunLog)

    def retranslateUi(self, dlgFunLog):
        _translate = QtCore.QCoreApplication.translate
        dlgFunLog.setWindowTitle(_translate("dlgFunLog", "函数调用日志信息"))
        self.groupBox.setTitle(_translate("dlgFunLog", "调用函数信息"))
        item = self.tableFunInfo.horizontalHeaderItem(0)
        item.setText(_translate("dlgFunLog", "函数名称"))
        item = self.tableFunInfo.horizontalHeaderItem(1)
        item.setText(_translate("dlgFunLog", "调用时间"))
        self.label.setText(_translate("dlgFunLog", "Web地址:"))
        self.groupBox_2.setTitle(_translate("dlgFunLog", "调用参数信息"))
        self.buttonCancel.setText(_translate("dlgFunLog", "关闭"))

import Resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dlg = QtWidgets.QDialog()
    ui = Ui_dlgFunLog()
    ui.setupUi(dlg)
    dlg.show()
    sys.exit(app.exec_())