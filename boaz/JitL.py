# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'JitLibrary.ui'
#
# Created: Sun Jun 06 11:41:08 2021
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainlabwindow(object):
    def setupUi(self, mainlabwindow):
        mainlabwindow.setObjectName(_fromUtf8("mainlabwindow"))
        mainlabwindow.resize(1601, 814)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(18)
        mainlabwindow.setFont(font)
        mainlabwindow.setStyleSheet(_fromUtf8("background:rgb(200, 170, 255)"))
        self.centralwidget = QtGui.QWidget(mainlabwindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(5)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setItalic(True)
        self.frame_2.setFont(font)
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet(_fromUtf8("background:rgb(175, 175, 175)"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setMidLineWidth(-6)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setHorizontalSpacing(7)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)
        self.cameraopen = QtGui.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.cameraopen.setFont(font)
        self.cameraopen.setStyleSheet(_fromUtf8("background:rgb(61, 61, 61)"))
        self.cameraopen.setText(_fromUtf8(""))
        self.cameraopen.setAlignment(QtCore.Qt.AlignCenter)
        self.cameraopen.setObjectName(_fromUtf8("cameraopen"))
        self.gridLayout_2.addWidget(self.cameraopen, 1, 0, 1, 4)
        self.btncamerastart = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btncamerastart.sizePolicy().hasHeightForWidth())
        self.btncamerastart.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btncamerastart.setFont(font)
        self.btncamerastart.setObjectName(_fromUtf8("btncamerastart"))
        self.gridLayout_2.addWidget(self.btncamerastart, 2, 2, 1, 1)
        self.cameraindex = QtGui.QComboBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cameraindex.sizePolicy().hasHeightForWidth())
        self.cameraindex.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.cameraindex.setFont(font)
        self.cameraindex.setObjectName(_fromUtf8("cameraindex"))
        self.cameraindex.addItem(_fromUtf8(""))
        self.cameraindex.addItem(_fromUtf8(""))
        self.cameraindex.addItem(_fromUtf8(""))
        self.cameraindex.addItem(_fromUtf8(""))
        self.cameraindex.addItem(_fromUtf8(""))
        self.cameraindex.addItem(_fromUtf8(""))
        self.cameraindex.addItem(_fromUtf8(""))
        self.cameraindex.addItem(_fromUtf8(""))
        self.cameraindex.addItem(_fromUtf8(""))
        self.cameraindex.addItem(_fromUtf8(""))
        self.cameraindex.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.cameraindex, 2, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.frame_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 2)
        self.btntakepicture = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btntakepicture.sizePolicy().hasHeightForWidth())
        self.btntakepicture.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btntakepicture.setFont(font)
        self.btntakepicture.setObjectName(_fromUtf8("btntakepicture"))
        self.gridLayout_2.addWidget(self.btntakepicture, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(11)
        self.frame.setFont(font)
        self.frame.setStyleSheet(_fromUtf8("Background:rgb(125, 0, 0)"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame)
        self.gridLayout_3.setMargin(5)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame_5 = QtGui.QFrame(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet(_fromUtf8("background:rgb(68, 160, 168)"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.gridLayout_4 = QtGui.QGridLayout(self.frame_5)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setHorizontalSpacing(4)
        self.gridLayout_4.setVerticalSpacing(10)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.frame_6 = QtGui.QFrame(self.frame_5)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.frame_6.setFont(font)
        self.frame_6.setStyleSheet(_fromUtf8("background:rgb(15, 170, 212)"))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.gridLayout_6 = QtGui.QGridLayout(self.frame_6)
        self.gridLayout_6.setContentsMargins(3, 3, 10, 3)
        self.gridLayout_6.setHorizontalSpacing(7)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.label_4 = QtGui.QLabel(self.frame_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_6.addWidget(self.label_4, 0, 3, 1, 2)
        self.label_6 = QtGui.QLabel(self.frame_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_6.addWidget(self.label_6, 4, 0, 1, 2)
        self.pushButton_9 = QtGui.QPushButton(self.frame_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.gridLayout_6.addWidget(self.pushButton_9, 1, 2, 1, 1)
        self.gridLayout_4.addWidget(self.frame_6, 1, 0, 1, 1)
        self.frame_4 = QtGui.QFrame(self.frame_5)
        self.frame_4.setStyleSheet(_fromUtf8("background:rgb(103, 208, 154)"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.gridLayout_7 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_7.setContentsMargins(8, 8, 0, 6)
        self.gridLayout_7.setHorizontalSpacing(3)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.frame_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.gridLayout_7.addWidget(self.dateTimeEdit, 0, 3, 1, 1)
        self.nameoftheinstitute = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(12)
        self.nameoftheinstitute.setFont(font)
        self.nameoftheinstitute.setText(_fromUtf8(""))
        self.nameoftheinstitute.setObjectName(_fromUtf8("nameoftheinstitute"))
        self.gridLayout_7.addWidget(self.nameoftheinstitute, 3, 1, 1, 3)
        self.presult = QtGui.QTextEdit(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.presult.sizePolicy().hasHeightForWidth())
        self.presult.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(120)
        font.setBold(True)
        font.setWeight(75)
        self.presult.setFont(font)
        self.presult.setStyleSheet(_fromUtf8("background:rgb(212, 212, 212)"))
        self.presult.setFrameShape(QtGui.QFrame.Panel)
        self.presult.setFrameShadow(QtGui.QFrame.Sunken)
        self.presult.setLineWidth(4)
        self.presult.setObjectName(_fromUtf8("presult"))
        self.gridLayout_7.addWidget(self.presult, 4, 0, 1, 4)
        self.label_7 = QtGui.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Times New Roman"))
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_7.addWidget(self.label_7, 2, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_5, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        mainlabwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainlabwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1601, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        mainlabwindow.setMenuBar(self.menubar)
        self.actionsave = QtGui.QAction(mainlabwindow)
        self.actionsave.setObjectName(_fromUtf8("actionsave"))
        self.actionAbout_us = QtGui.QAction(mainlabwindow)
        self.actionAbout_us.setObjectName(_fromUtf8("actionAbout_us"))
        self.actionHelp = QtGui.QAction(mainlabwindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionChange_color = QtGui.QAction(mainlabwindow)
        self.actionChange_color.setObjectName(_fromUtf8("actionChange_color"))
        self.actionclose = QtGui.QAction(mainlabwindow)
        self.actionclose.setObjectName(_fromUtf8("actionclose"))
        self.actionExit = QtGui.QAction(mainlabwindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionsave)
        self.menuFile.addAction(self.actionclose)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout_us)
        self.menuHelp.addAction(self.actionHelp)
        self.menuEdit.addAction(self.actionChange_color)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainlabwindow)
        QtCore.QMetaObject.connectSlotsByName(mainlabwindow)

    def retranslateUi(self, mainlabwindow):
        mainlabwindow.setWindowTitle(_translate("mainlabwindow", "main laboratory bench", None))
        self.label.setText(_translate("mainlabwindow", "Select camera", None))
        self.btncamerastart.setText(_translate("mainlabwindow", "Start", None))
        self.cameraindex.setItemText(0, _translate("mainlabwindow", "0", None))
        self.cameraindex.setItemText(1, _translate("mainlabwindow", "1", None))
        self.cameraindex.setItemText(2, _translate("mainlabwindow", "2", None))
        self.cameraindex.setItemText(3, _translate("mainlabwindow", "3", None))
        self.cameraindex.setItemText(4, _translate("mainlabwindow", "4", None))
        self.cameraindex.setItemText(5, _translate("mainlabwindow", "5", None))
        self.cameraindex.setItemText(6, _translate("mainlabwindow", "6", None))
        self.cameraindex.setItemText(7, _translate("mainlabwindow", "7", None))
        self.cameraindex.setItemText(8, _translate("mainlabwindow", "8", None))
        self.cameraindex.setItemText(9, _translate("mainlabwindow", "9", None))
        self.cameraindex.setItemText(10, _translate("mainlabwindow", "10", None))
        self.pushButton.setText(_translate("mainlabwindow", "Maximize", None))
        self.label_2.setText(_translate("mainlabwindow", "Press M to Maximize and N to Minimize", None))
        self.btntakepicture.setText(_translate("mainlabwindow", "Take a picture", None))
        self.label_6.setText(_translate("mainlabwindow", "Developed by JiT Library AI and VR Club", None))
        self.pushButton_9.setText(_translate("mainlabwindow", "Reset", None))
        self.label_7.setText(_translate("mainlabwindow", "Total Studnet inside Library", None))
        self.menuFile.setTitle(_translate("mainlabwindow", "File", None))
        self.menuHelp.setTitle(_translate("mainlabwindow", "Help", None))
        self.menuEdit.setTitle(_translate("mainlabwindow", "Edit", None))
        self.actionsave.setText(_translate("mainlabwindow", "Save", None))
        self.actionAbout_us.setText(_translate("mainlabwindow", "About us", None))
        self.actionHelp.setText(_translate("mainlabwindow", "Help", None))
        self.actionChange_color.setText(_translate("mainlabwindow", "Change color", None))
        self.actionclose.setText(_translate("mainlabwindow", "Open", None))
        self.actionExit.setText(_translate("mainlabwindow", "Exit", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    mainlabwindow = QtGui.QMainWindow()
    ui = Ui_mainlabwindow()
    ui.setupUi(mainlabwindow)
    mainlabwindow.show()
    sys.exit(app.exec_())

