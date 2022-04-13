#!/usr/bin/env python3

### IMPORT STATEMENTS ###
from genericpath import exists
import subprocess,re,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#global variables so that when autocomplete function is called does not reset containers
src_ip = []
dst_ip = []
src_port = []
dst_port = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1405, 881)
        MainWindow.setStyleSheet("font: 13pt \"Roboto Slab\";\n""background-color: rgb(87, 109, 130);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RuleChain = QtWidgets.QComboBox(self.centralwidget)
        self.RuleChain.setGeometry(QtCore.QRect(100, 620, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RuleChain.setFont(font)
        self.RuleChain.setStyleSheet("")
        self.RuleChain.setPlaceholderText("")
        self.RuleChain.setObjectName("RuleChain")
        self.RuleChain.addItem("")
        self.RuleChain.setItemText(0, "Rule Chain")
        self.RuleChain.addItem("")
        self.RuleChain.addItem("")
        self.RuleChain.addItem("")
        self.TrafficType = QtWidgets.QComboBox(self.centralwidget)
        self.TrafficType.setGeometry(QtCore.QRect(270, 620, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.TrafficType.setFont(font)
        self.TrafficType.setStyleSheet("")
        self.TrafficType.setObjectName("TrafficType")
        self.TrafficType.addItem("")
        self.TrafficType.setItemText(0, "Traffic Type")
        self.TrafficType.addItem("")
        self.TrafficType.addItem("")
        self.TrafficType.addItem("")
        self.TrafficType.addItem("")
        self.Action = QtWidgets.QComboBox(self.centralwidget)
        self.Action.setGeometry(QtCore.QRect(440, 620, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Action.setFont(font)
        self.Action.setPlaceholderText("")
        self.Action.setFrame(True)
        self.Action.setObjectName("Action")
        self.Action.addItem("")
        self.Action.addItem("")
        self.Action.addItem("")
        self.Action.addItem("")
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setGeometry(QtCore.QRect(1280, 630, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear")
        self.AddRule = QtWidgets.QPushButton(self.centralwidget)
        self.AddRule.setGeometry(QtCore.QRect(590, 720, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AddRule.setFont(font)
        self.AddRule.setObjectName("AddRule")
        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(1270, 780, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Reset.setFont(font)
        self.Reset.setObjectName("Reset")
        self.UpdateRule = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateRule.setGeometry(QtCore.QRect(590, 720, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.UpdateRule.setFont(font)
        self.UpdateRule.setObjectName("UpdateRule")
        #another button for Update Confirmation, choosing which rule and chain
        self.UpdateConfirm = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateConfirm.setGeometry(QtCore.QRect(590, 720, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.UpdateConfirm.setFont(font)
        self.UpdateConfirm.setObjectName("UpdateConfirm")
        self.RuleView = QtWidgets.QScrollArea(self.centralwidget)
        self.RuleView.setGeometry(QtCore.QRect(10, 0, 1381, 591))
        self.RuleView.setStyleSheet("background-color: rgb(151, 172, 194);\n""color: rgb(41, 56, 71);")
        self.RuleView.setWidgetResizable(True)
        self.RuleView.setObjectName("RuleView")
        self.RuleArea = QtWidgets.QWidget()
        self.RuleArea.setGeometry(QtCore.QRect(0, 0, 1379, 589))
        self.RuleArea.setObjectName("RuleArea")
        self.Input = QtWidgets.QLabel(self.RuleArea)
        self.Input.setGeometry(QtCore.QRect(210, 0, 251, 19))
        self.Input.setObjectName("Input")
        self.tableWidget = QtWidgets.QTableWidget(self.RuleArea)
        self.tableWidget.setEnabled(True)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 661, 561))
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 5, item)
        self.Forward = QtWidgets.QLabel(self.RuleArea)
        self.Forward.setGeometry(QtCore.QRect(920, 0, 291, 19))
        self.Forward.setObjectName("Forward")
        self.Output = QtWidgets.QLabel(self.RuleArea)
        self.Output.setGeometry(QtCore.QRect(920, 300, 281, 19))
        self.Output.setObjectName("Output")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.RuleArea)
        self.tableWidget_2.setEnabled(True)
        self.tableWidget_2.setGeometry(QtCore.QRect(690, 20, 671, 261))
        self.tableWidget_2.setStyleSheet("")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_2.setItem(0, 5, item)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.RuleArea)
        self.tableWidget_3.setEnabled(True)
        self.tableWidget_3.setGeometry(QtCore.QRect(690, 320, 671, 261))
        self.tableWidget_3.setStyleSheet("")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget_3.setItem(0, 5, item)
        self.RuleView.setWidget(self.RuleArea)
        self.SourceLabel = QtWidgets.QLabel(self.centralwidget)
        self.SourceLabel.setGeometry(QtCore.QRect(680, 600, 81, 19))
        self.SourceLabel.setObjectName("SourceLabel")
        self.SrcPortLabel = QtWidgets.QLabel(self.centralwidget)
        self.SrcPortLabel.setGeometry(QtCore.QRect(850, 600, 71, 19))
        self.SrcPortLabel.setObjectName("SrcPortLabel")
        self.DestinationLabel = QtWidgets.QLabel(self.centralwidget)
        self.DestinationLabel.setGeometry(QtCore.QRect(990, 600, 121, 19))
        self.DestinationLabel.setObjectName("DestinationLabel")
        self.DestPortLabel = QtWidgets.QLabel(self.centralwidget)
        self.DestPortLabel.setGeometry(QtCore.QRect(1180, 600, 71, 19))
        self.DestPortLabel.setObjectName("DestPortLabel")
        self.ActionLabel = QtWidgets.QLabel(self.centralwidget)
        self.ActionLabel.setGeometry(QtCore.QRect(490, 600, 61, 19))
        self.ActionLabel.setObjectName("ActionLabel")
        self.TrafficeTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TrafficeTypeLabel.setGeometry(QtCore.QRect(300, 600, 101, 19))
        self.TrafficeTypeLabel.setObjectName("TrafficeTypeLabel")
        self.RuleChainLabel = QtWidgets.QLabel(self.centralwidget)
        self.RuleChainLabel.setGeometry(QtCore.QRect(130, 600, 91, 19))
        self.RuleChainLabel.setObjectName("RuleChainLabel")
        self.Check_Add = QtWidgets.QLabel(self.centralwidget)
        self.Check_Add.setGeometry(QtCore.QRect(820, 720, 91, 31))
        self.Check_Add.setStyleSheet("background-color: rgb(196, 196, 196);\n""color: rgb(0, 0, 0);")
        self.Check_Add.setObjectName("Check_Add")
        self.Check_Remove = QtWidgets.QCheckBox(self.centralwidget)
        self.Check_Remove.setGeometry(QtCore.QRect(820, 780, 91, 31))
        self.Check_Remove.setStyleSheet("background-color: rgb(196, 196, 196);\n""color: rgb(0, 0, 0);")
        self.Check_Remove.setObjectName("Check_Remove")
        self.Check_Update = QtWidgets.QCheckBox(self.centralwidget)
        self.Check_Update.setGeometry(QtCore.QRect(820, 750, 91, 31))
        self.Check_Update.setStyleSheet("background-color: rgb(196, 196, 196);\n""color: rgb(0, 0, 0);")
        self.Check_Update.setObjectName("Check_Update")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(20, 620, 61, 61))
        self.spinBox.setObjectName("spinBox")
        self.Num = QtWidgets.QLabel(self.centralwidget)
        self.Num.setGeometry(QtCore.QRect(30, 600, 41, 19))
        self.Num.setObjectName("Num")
        self.RemoveRule = QtWidgets.QPushButton(self.centralwidget)
        self.RemoveRule.setGeometry(QtCore.QRect(590, 720, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RemoveRule.setFont(font)
        self.RemoveRule.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.RemoveRule.setStyleSheet("")
        self.RemoveRule.setObjectName("RemoveRule")
        self.spinBox_Remove = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Remove.setGeometry(QtCore.QRect(330, 740, 61, 61))
        self.spinBox_Remove.setObjectName("spinBox_Remove")
        self.RuleChain_Remove = QtWidgets.QComboBox(self.centralwidget)
        self.RuleChain_Remove.setGeometry(QtCore.QRect(410, 740, 151, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.RuleChain_Remove.setFont(font)
        self.RuleChain_Remove.setStyleSheet("")
        self.RuleChain_Remove.setPlaceholderText("")
        self.RuleChain_Remove.setObjectName("RuleChain_Remove")
        self.RuleChain_Remove.addItem("")
        self.RuleChain_Remove.setItemText(0, "Rule Chain")
        self.RuleChain_Remove.addItem("")
        self.RuleChain_Remove.addItem("")
        self.RuleChain_Remove.addItem("")
        self.Num_Remove = QtWidgets.QLabel(self.centralwidget)
        self.Num_Remove.setGeometry(QtCore.QRect(340, 720, 41, 19))
        self.Num_Remove.setObjectName("Num_Remove")
        self.RuleChainLabel_Remove = QtWidgets.QLabel(self.centralwidget)
        self.RuleChainLabel_Remove.setGeometry(QtCore.QRect(440, 720, 91, 19))
        self.RuleChainLabel_Remove.setObjectName("RuleChainLabel_Remove")
        self.SrcIP = QtWidgets.QLineEdit(self.centralwidget)
        self.SrcIP.setGeometry(QtCore.QRect(610, 620, 211, 61))
        self.SrcIP.setObjectName("SrcIP")
        self.DstIP = QtWidgets.QLineEdit(self.centralwidget)
        self.DstIP.setGeometry(QtCore.QRect(940, 620, 211, 61))
        self.DstIP.setObjectName("DstIP")
        self.SrcPort = QtWidgets.QLineEdit(self.centralwidget)
        self.SrcPort.setGeometry(QtCore.QRect(840, 620, 81, 61))
        self.SrcPort.setObjectName("SrcPort")
        self.DstPort = QtWidgets.QLineEdit(self.centralwidget)
        self.DstPort.setGeometry(QtCore.QRect(1170, 620, 81, 61))
        self.DstPort.setObjectName("DstPort")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(20, 800, 61, 26))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1405, 28))
        self.menubar.setObjectName("menubar")
        self.menuSave = QtWidgets.QMenu(self.menubar)
        self.menuSave.setObjectName("menuSave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionRestore = QtWidgets.QAction(MainWindow)
        self.actionRestore.setObjectName("actionRestore")
        self.menuSave.addAction(self.actionSave)
        self.menuSave.addAction(self.actionRestore)
        self.menuSave.addSeparator()
        self.menubar.addAction(self.menuSave.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Save file / Restore file
        self.actionSave.triggered.connect(self.file_save)
        self.actionRestore.triggered.connect(self.file_restore)

        #When a button is clicked (fuction calls)
        self.AddRule.clicked.connect(self.add_rule_button) #calls add_rule_button function when clicked. (Adds rule)
        self.RemoveRule.clicked.connect(self.remove_rule_button) #call remove_rule_button when clicked. (Removes rule)
        self.UpdateConfirm.clicked.connect(self.confirm_button) #call confirm_button when clicked. (Grabs data for confirmation of replacement/update)
        self.UpdateRule.clicked.connect(self.update_rule_button) #call update_rule_button when clicked. (Updates rule)
        self.Reset.clicked.connect(self.show_popup) #calls show_popup function when clicked. (Confirmation screen)
        self.Clear.clicked.connect(self.clear_text) #calls clear_text when clicked. (Clear box text)
        self.TrafficType.currentIndexChanged.connect(self.disable_box) #calls disable_box when "Traffic Type" dropdown value changes. Checks for ICMP/IP
        self.spinBox.valueChanged.connect(self.switch_name) #swaps between "Add" and "Insert" for the button name

        #set buttons state
        self.AddRule.setEnabled(False) #set "Add Rule" button unclickable for beginning
        self.UpdateRule.setEnabled(False) #set "Update Rule" button unclickable for beginning
        self.RemoveRule.setEnabled(False) #set "Remove Rule" button unclickable for beginning
        self.UpdateConfirm.setEnabled(False) #set "Update Confirm" button unclickable for beginning

        #Calls check_rule, if "RuleChain, TrafficType, Action" are changed from index 0. Allows "Add Rule" button to be active
        self.RuleChain.currentIndexChanged.connect(self.check_rule)
        self.TrafficType.currentIndexChanged.connect(self.check_rule)
        self.Action.currentIndexChanged.connect(self.check_rule)
        self.RuleChain.currentIndexChanged.connect(self.update_check_rule)
        self.TrafficType.currentIndexChanged.connect(self.update_check_rule)
        self.Action.currentIndexChanged.connect(self.update_check_rule)

        #Hide labels and unhide when box field has string value
        self.RuleChainLabel.setHidden(True)
        self.ActionLabel.setHidden(True)
        self.TrafficeTypeLabel.setHidden(True)
        self.SourceLabel.setHidden(True)
        self.SrcPortLabel.setHidden(True)
        self.DestinationLabel.setHidden(True)
        self.DestPortLabel.setHidden(True)
        self.RuleChain.currentIndexChanged.connect(self.hidden_label)
        self.Action.currentIndexChanged.connect(self.hidden_label)
        self.TrafficType.currentIndexChanged.connect(self.hidden_label)
        self.SrcIP.textChanged.connect(self.hidden_label)
        self.SrcPort.textChanged.connect(self.hidden_label)
        self.DstIP.textChanged.connect(self.hidden_label)
        self.DstPort.textChanged.connect(self.hidden_label)

        #Hidden State for Remove Button toggle checkmark
        self.Num_Remove.setHidden(True)
        self.spinBox_Remove.setHidden(True)
        self.RuleChain_Remove.setHidden(True)
        self.RuleChainLabel_Remove.setHidden(True)

        #Checkbox state
        self.Check_Add.setAlignment(QtCore.Qt.AlignCenter) #Alignment of the "Mode" Label
        self.Check_Update.stateChanged.connect(self.uncheck_update) #only allows 1 check, will do tasks for "Update" mode
        self.Check_Remove.stateChanged.connect(self.uncheck_remove) #only allows 1 check, will do tasks for "Remove" mode
        self.RuleChain_Remove.currentIndexChanged.connect(self.check_remove) #if the dropdown list for the remove "Rule Chain" has changed from index 0 enable the button
        self.RuleChain_Remove.currentIndexChanged.connect(self.check_update)

        #View iptable rules on screen via GUI, initially running "sudo iptables -L" by calling function "view_rule"
        self.view_rule()

        #Checkbox state, set buttons for both to be hidden from beginning, only "Add Rule" by default
        self.UpdateRule.setHidden(True)
        self.RemoveRule.setHidden(True)
        self.UpdateConfirm.setHidden(True)

        #Set Character Limit, 15 for IP including '.' and 5 for Port since 65535
        self.SrcIP.setMaxLength(18)
        self.SrcPort.setMaxLength(5)
        self.DstIP.setMaxLength(18)
        self.DstPort.setMaxLength(5)
        #self.spinBox.setMinimum(1)

        input_header = self.tableWidget.horizontalHeader()
        input_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents) #Accept
        input_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents) #Protocol
        input_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch) #srcIP
        input_header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents) #srcPort
        input_header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch) #destinationIP
        input_header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents) #destPort

        forward_header = self.tableWidget_2.horizontalHeader()
        forward_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents) #Accept
        forward_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents) #Protocol
        forward_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch) #srcIP
        forward_header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents) #srcPort
        forward_header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch) #destinationIP
        forward_header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents) #destPort

        output_header = self.tableWidget_3.horizontalHeader()
        output_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents) #Accept
        output_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents) #Protocol
        output_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch) #srcIP
        output_header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents) #srcPort
        output_header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch) #destinationIP
        output_header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents) #destPort

        #function call at the beginning to initialize the current table when loading the application
        # self.load_input()
        # self.load_forward()
        # self.load_output()

    #Renaming the items
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "driptables"))
        self.RuleChain.setItemText(1, _translate("MainWindow", "INPUT"))
        self.RuleChain.setItemText(2, _translate("MainWindow", "FORWARD"))
        self.RuleChain.setItemText(3, _translate("MainWindow", "OUTPUT"))
        self.TrafficType.setItemText(1, _translate("MainWindow", "TCP"))
        self.TrafficType.setItemText(2, _translate("MainWindow", "UDP"))
        self.TrafficType.setItemText(3, _translate("MainWindow", "IP"))
        self.TrafficType.setItemText(4, _translate("MainWindow", "ICMP"))
        self.Action.setCurrentText(_translate("MainWindow", "Action"))
        self.Action.setItemText(0, _translate("MainWindow", "Action"))
        self.Action.setItemText(1, _translate("MainWindow", "ACCEPT"))
        self.Action.setItemText(2, _translate("MainWindow", "DROP"))
        self.Action.setItemText(3, _translate("MainWindow", "REJECT"))
        self.Clear.setText(_translate("MainWindow", "🚮 CLEAR"))
        self.AddRule.setText(_translate("MainWindow", "Add Rule"))
        self.Reset.setText(_translate("MainWindow", "⛔ Reset Rules"))
        self.UpdateRule.setText(_translate("MainWindow", "Update Rule"))
        self.UpdateConfirm.setText(_translate("MainWindow", "Confirm"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Target"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Source IP"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Src Port"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Destination IP"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Dest Port"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Target"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Source IP"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Src Port"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Destination IP"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Dest Port"))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Target"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Protocol"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Source IP"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Src Port"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Destination IP"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Dest Port"))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.SourceLabel.setText(_translate("MainWindow", "Source IP"))
        self.SrcPortLabel.setText(_translate("MainWindow", "Src Port"))
        self.DestinationLabel.setText(_translate("MainWindow", "Destination IP"))
        self.DestPortLabel.setText(_translate("MainWindow", "Dst Port"))
        self.ActionLabel.setText(_translate("MainWindow", "Action"))
        self.TrafficeTypeLabel.setText(_translate("MainWindow", "Traffic Type"))
        self.RuleChainLabel.setText(_translate("MainWindow", "Rule Chain"))
        self.Check_Add.setText(_translate("MainWindow", "Modes"))
        self.Check_Remove.setText(_translate("MainWindow", "Remove"))
        self.Check_Update.setText(_translate("MainWindow", "Update"))
        self.Num.setText(_translate("MainWindow", "Num"))
        self.RemoveRule.setText(_translate("MainWindow", "🗑️ Remove Rule"))
        self.RuleChain_Remove.setItemText(1, _translate("MainWindow", "INPUT"))
        self.RuleChain_Remove.setItemText(2, _translate("MainWindow", "FORWARD"))
        self.RuleChain_Remove.setItemText(3, _translate("MainWindow", "OUTPUT"))
        self.Num_Remove.setText(_translate("MainWindow", "Num"))
        self.RuleChainLabel_Remove.setText(_translate("MainWindow", "Rule Chain"))
        self.SrcIP.setPlaceholderText(_translate("MainWindow", "Source IP"))
        self.DstIP.setPlaceholderText(_translate("MainWindow", "Destination IP"))
        self.SrcPort.setPlaceholderText(_translate("MainWindow", "Src Port"))
        self.DstPort.setPlaceholderText(_translate("MainWindow", "Dst Port"))
        self.toolButton.setText(_translate("MainWindow", "Info 🔍"))
        self.menuSave.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save 💾"))
        self.actionRestore.setText(_translate("MainWindow", "Restore 🔄"))

### HELPER FUNCTIONS ###
    def load_input(self):
        commandline = subprocess.Popen([f"sudo iptables -L INPUT -n --line-numbers | sed -e '1,2d'"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        test, stderr_output = commandline.communicate() #storing the output of the commandline to variable output
        test = test.decode("utf-8") #saving the output as a string type to parse
        tablerow = 0 #increment the table row
        self.tableWidget.setRowCount(0) #set it to zero if no rules
        for line in test.splitlines(): #parsing each line in the INPUT CHAIN
            line = line.split() #putting all data into a list, example: ['1', 'ACCEPT', 'tcp', '--', '8.8.8.8', '1.1.1.1', 'tcp', 'spt:24', 'dpt:23']
            self.tableWidget.setRowCount(int(line[0])) #setting the row per how many rules there are
            if line[2] == 'icmp' and line[2] == 'all': #only ip/icmp ruleset meaning NO SRC/DST PORT #
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(line[1])) #insert target (accept,drop,reject)
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(line[2].upper())) #insert protocol
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(line[4])) #insert src ip
                self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(line[5])) #insert dst ip
            elif len(line) <= 6: #any other protocol that doesn't have src/dst port
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(line[1])) #insert target (accept,drop,reject)
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(line[2].upper())) #insert protocol
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(line[4])) #insert src ip
                self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(line[5])) #insert dst ip
            else: #for rules with src/dst port and more data
                self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(line[1])) #insert target (accept,drop,reject)
                self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(line[2].upper())) #insert protocol
                self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(line[4])) #insert src ip
                self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(line[5])) #insert dst ip
                if len(line) >= 9: #if spt and dpt exists, save both then append both
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(line[7][4:])) #insert src port
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(line[8][4:])) #insert dst port
                elif 'spt' in line[7]: #if spt is index 7, insert src port
                    self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(line[7][4:]))
                elif 'dpt' in line[7]: #if dpt is index 7, insert dst port
                    self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(line[7][4:]))
            tablerow += 1 #increment very important to add every rule to the table. From first rule to final rule.

    def load_forward(self):
        commandline = subprocess.Popen([f"sudo iptables -L FORWARD -n --line-numbers | sed -e '1,2d'"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        test, stderr_output = commandline.communicate() #storing the output of the commandline to variable output
        test = test.decode("utf-8") #saving the output as a string type to parse
        tablerow = 0 #increment the table row
        self.tableWidget_2.setRowCount(0) #set it to zero if no rules
        for line in test.splitlines(): #parsing each line in the INPUT CHAIN
            line = line.split() #putting all data into a list, example: ['1', 'ACCEPT', 'tcp', '--', '8.8.8.8', '1.1.1.1', 'tcp', 'spt:24', 'dpt:23']
            self.tableWidget_2.setRowCount(int(line[0])) #setting the row per how many rules there are
            if line[2] == 'icmp' and line[2] == 'all': #only ip/icmp ruleset meaning NO SRC/DST PORT #
                self.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(line[1])) #insert target (accept,drop,reject)
                self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(line[2].upper())) #insert protocol
                self.tableWidget_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(line[4])) #insert src ip
                self.tableWidget_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(line[5])) #insert dst ip
            elif len(line) <= 6: #any other protocol that doesn't have src/dst port
                self.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(line[1])) #insert target (accept,drop,reject)
                self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(line[2].upper())) #insert protocol
                self.tableWidget_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(line[4])) #insert src ip
                self.tableWidget_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(line[5])) #insert dst ip
            else: #for rules with src/dst port and more data
                self.tableWidget_2.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(line[1])) #insert target (accept,drop,reject)
                self.tableWidget_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(line[2].upper())) #insert protocol
                self.tableWidget_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(line[4])) #insert src ip
                self.tableWidget_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(line[5])) #insert dst ip
                if len(line) >= 9: #if spt and dpt exists, save both then append both
                    self.tableWidget_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(line[7][4:])) #insert src port
                    self.tableWidget_2.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(line[8][4:])) #insert dst port
                elif 'spt' in line[7]: #if spt is index 7, insert src port
                    self.tableWidget_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(line[7][4:]))
                elif 'dpt' in line[7]: #if dpt is index 7, insert dst port
                    self.tableWidget_2.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(line[7][4:]))
            tablerow += 1 #increment very important to add every rule to the table. From first rule to final rule.

    def load_output(self):
        commandline = subprocess.Popen([f"sudo iptables -L OUTPUT -n --line-numbers | sed -e '1,2d'"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        test, stderr_output = commandline.communicate() #storing the output of the commandline to variable output
        test = test.decode("utf-8") #saving the output as a string type to parse
        tablerow = 0 #increment the table row
        self.tableWidget_3.setRowCount(0) #set it to zero if no rules
        for line in test.splitlines(): #parsing each line in the INPUT CHAIN
            line = line.split() #putting all data into a list, example: ['1', 'ACCEPT', 'tcp', '--', '8.8.8.8', '1.1.1.1', 'tcp', 'spt:24', 'dpt:23']
            self.tableWidget_3.setRowCount(int(line[0])) #setting the row per how many rules there are
            if line[2] == 'icmp' and line[2] == 'all': #only ip/icmp ruleset meaning NO SRC/DST PORT #
                self.tableWidget_3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(line[1])) #insert target (accept,drop,reject)
                self.tableWidget_3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(line[2].upper())) #insert protocol
                self.tableWidget_3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(line[4])) #insert src ip
                self.tableWidget_3.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(line[5])) #insert dst ip
            elif len(line) <= 6: #any other protocol that doesn't have src/dst port
                self.tableWidget_3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(line[1])) #insert target (accept,drop,reject)
                self.tableWidget_3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(line[2].upper())) #insert protocol
                self.tableWidget_3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(line[4])) #insert src ip
                self.tableWidget_3.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(line[5])) #insert dst ip
            else: #for rules with src/dst port and more data
                self.tableWidget_3.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(line[1])) #insert target (accept,drop,reject)
                self.tableWidget_3.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(line[2].upper())) #insert protocol
                self.tableWidget_3.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(line[4])) #insert src ip
                self.tableWidget_3.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(line[5])) #insert dst ip
                if len(line) >= 9: #if spt and dpt exists, save both then append both
                    self.tableWidget_3.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(line[7][4:])) #insert src port
                    self.tableWidget_3.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(line[8][4:])) #insert dst port
                elif 'spt' in line[7]: #if spt is index 7, insert src port
                    self.tableWidget_3.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(line[7][4:]))
                elif 'dpt' in line[7]: #if dpt is index 7, insert dst port
                    self.tableWidget_3.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(line[7][4:]))
            tablerow += 1 #increment very important to add every rule to the table. From first rule to final rule

    #saving the current ruleset to a file, user selects the path to save the file
    def file_save(self):
        filename = QFileDialog.getSaveFileName()
        path = filename[0]
        commandline = subprocess.Popen([f"sudo iptables-save > {path}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        output, stderr_output = commandline.communicate() #will save rules to a file
        if path != "":
            msg = QMessageBox()
            msg.setWindowTitle("Saved")
            msg.setText("iptables have been saved!")
            msg.setIcon(QMessageBox.Information)
            msg.exec_()

    #restoring ruleset from a file
    def file_restore(self):
        filename = QFileDialog.getOpenFileName() #opens up file explorer and lets you select your file to restore
        path = filename[0] #grabs just the path of that file, aka the absolute path, and feed the absolute path to the process to restore rules
        commandline = subprocess.Popen([f"sudo iptables-restore < {path}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        output, stderr_output = commandline.communicate() #will import rules that were saved to the file
        self.view_rule() #Updates iptable table on screen after restoring

    #Iptables Rule List, is called and then updates the table to have latest entry of the iptable on Linux machine
    def view_rule(self):
        commandline = subprocess.Popen([f"sudo iptables -L INPUT -n --line-numbers | head -n1"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        input, stderr_output = commandline.communicate() #storing the output of the commandline to variable output
        input = input.decode("utf-8") #saving the output as a string type to parse
        input = input.split("(policy ") #using delimiter to grab only the policy type
        input_policy = input[1][:-2].strip()

        commandline = subprocess.Popen([f"sudo iptables -L FORWARD -n --line-numbers | head -n1"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        forward, stderr_output = commandline.communicate() #storing the output of the commandline to variable output
        forward = forward.decode("utf-8") #saving the output as a string type to parse
        forward = forward.split("(policy ") #using delimiter to grab only the policy type
        forward_policy = forward[1][:-2].strip()

        commandline = subprocess.Popen([f"sudo iptables -L OUTPUT -n --line-numbers | head -n1"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        output, stderr_output = commandline.communicate() #storing the output of the commandline to variable output
        output = output.decode("utf-8") #saving the output as a string type to parse
        output = output.split("(policy ") #using delimiter to grab only the policy type
        output_policy = output[1][:-2].strip()

        #setting the label type to be either "ACCEPT | DROP" depending on which state it is natively
        self.Input.setText(QtCore.QCoreApplication.translate("MainWindow", f"Chain INPUT (policy {input_policy})"))
        self.Forward.setText(QtCore.QCoreApplication.translate("MainWindow", f"Chain FORWARD (policy {forward_policy})"))
        self.Output.setText(QtCore.QCoreApplication.translate("MainWindow", f"Chain OUTPUT (policy {output_policy})"))

        #loading each 3 table's data
        self.load_input()
        self.load_forward()
        self.load_output()

    #Confirmation button for updating 1 rule at a time in update mode state (will grab num and rule chain)
    def confirm_button(self):
        spt = "" #gotta assign here because if never reaches if-else will toss error
        dpt = "" #gotta assign here because if never reaches if-else will toss error
        update = {} #container to store the variables of spinBox and protocol type
        update['chain'] = self.RuleChain_Remove.currentText()
        update['num'] = str(self.spinBox_Remove.value()) #convert to str since originally is type int for concatenation
        #process will grab the actual line from the iptable given valid (num/chain)
        commandline = subprocess.Popen([f"sudo iptables -L {update['chain']} -n --line-numbers | grep -w ^{update['num']}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        output, stderr_output = commandline.communicate() #storing the output of the commandline to variable output
        output = output.decode("utf-8") #saving the output as a string type
        output = output.split() #List data type where: 0=num, 1=ACTION, 2=PROTOCOL, 3=opt, 4=srcIP, 5=dstIP, 6=port protocol, 7=spt, 8=dpt (7 & 8 can be interchange due to not having spt but having dpt)
        #print(output) #print statement for testing
        #Validation checking process for valid output given from commandline
        if output != []: #if there is no error and selected a valid num and chain that exists proceed forward
            num = output[0]
            action = output[1]
            protocol = output[2].upper() #capitalize the protocol so that it works with commands later
            srcIP = output[4]
            dstIP = output[5]
            if protocol != 'ICMP' and protocol != 'ALL': #ignore spt and dpt for ICMP and IP since they don't rely on the two fields
                if 'spt' in output[7]: #if spt is index 7 save as spt, only saves one for index 7
                    spt = (output[7][4:])
                elif 'dpt' in output[7]: #if dpt is index 7 save as dpt, only saves one for index 7
                    dpt = (output[7][4:])
                if len(output) == 9: #if spt and dpt exists, save both then
                    dpt = output[8][4:]
            #sending here because otherwise the rule does not exists in the table
            self.fill_data(update['chain'], num, action, protocol, srcIP, dstIP, spt, dpt) #sending the data over to another function after parsing
        else:
            if int(update['num']) == 0 or output == []:
                self.num_error_popup()

    #filling in the data grabbed from confirm_button to populate the boxes for ease of access when updating a rule that already exists
    def fill_data(self, chain, num, action, protocol, srcIP, dstIP, spt, dpt):
        self.unhide() #unhide the UI that holds the original boxes where the data is being sent to and stored for process command
        self.UpdateConfirm.setHidden(True)
        self.spinBox_Remove.setHidden(True)
        self.Num_Remove.setHidden(True)
        self.RuleChain_Remove.setHidden(True)
        self.RuleChainLabel_Remove.setHidden(True)
        self.UpdateRule.setHidden(False)

        #filling in all the empty fields with data that was parsed from the confirmation screen
        if chain == "INPUT":
            self.RuleChain.setCurrentIndex(1) #set to INPUT
        elif chain == "FORWARD":
            self.RuleChain.setCurrentIndex(2) #set to FORWARD
        elif chain == "OUTPUT":
            self.RuleChain.setCurrentIndex(3) #set to OUTPUT

        if protocol == "TCP":
            self.TrafficType.setCurrentIndex(1) #set to TCP
        elif protocol == "UDP":
            self.TrafficType.setCurrentIndex(2) #set to UDP
        elif protocol == "IP":
            self.TrafficType.setCurrentIndex(3) #set to IP
        elif protocol == "ICMP":
            self.TrafficType.setCurrentIndex(4) #set to ICMP

        if action == "ACCEPT":
            self.Action.setCurrentIndex(1) #set to ACCEPT
        elif action == "DROP":
            self.Action.setCurrentIndex(2) #set to DROP
        elif action == "REJECT":
            self.Action.setCurrentIndex(3) #set to REJECT

        #rest of the populating of data to containers other than combo-box, lineEdit containers below
        self.spinBox.setValue(int(num))
        self.SrcIP.setText(srcIP)
        self.SrcPort.setText(spt)
        self.DstIP.setText(dstIP)
        self.DstPort.setText(dpt)

    #Update rule to the actual iptable in Linux
    def update_rule_button(self):
        ip_regex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/(\\d|[1-2]\\d|3[0-2]))?$" #regular expression for IPv4 address + CIDR notation
        #ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$" #old regular expression for IPv4 address does not check for CIDR
        rule_flag = True #for checking if IP validation check passes
        boxes = {} #dictionary to store values from boxes
        boxes = {'num':self.spinBox,'chain':self.RuleChain,'protocol':self.TrafficType,'action':self.Action,'source':self.SrcIP,'src_port':self.SrcPort,'destination':self.DstIP,'dst_port':self.DstPort}
        #Reset rules for each instance. New iptable rule
        rules = {} #dictionary to store string representation value from variable "boxes" by toPlainText conversion, below is the conversion
        rules['num'] = str(boxes['num'].value()) #spinBox type is int but needs to be converted to string in order to be concatenated
        rules['chain'] = boxes['chain'].currentText() #Input, Forward, Output
        rules['protocol'] = boxes['protocol'].currentText() #TCP, UDP, IP, ICMP
        rules['action'] = boxes['action'].currentText() #Accept, Drop, Reject
        rules['source'] = boxes['source'].text() #Source IP Address
        rules['src_port'] = boxes['src_port'].text() #Source Port Number
        rules['destination'] = boxes['destination'].text() #Destination IP Address
        rules['dst_port'] = boxes['dst_port'].text() #Destination Port Number

        #Check if Source IP/Destination IP addresses is valid:
        if rules['source'] != '' and rules['destination'] != '': #if both boxes have fields
            #valid, do nothing (pass)
            #otherwise, toss an error dialog box, different reasonings below
            if (re.search(ip_regex, rules['source']) and re.search(ip_regex, rules['destination'])): #if both valid via comparison
                pass
            else:
                rule_flag = False
                msg = QMessageBox()
                msg.setWindowTitle("Error, Try Again!")
                msg.setText("Source IP or Destination IP Address are Invalid.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        elif rules['source'] != '': #if source IP has fields
            if (re.search(ip_regex, rules['source'])): #source IP is valid
                pass
            else:
                rule_flag = False
                msg = QMessageBox()
                msg.setWindowTitle("Error, Try Again!")
                msg.setText("Source IP Address is Invalid.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        elif rules['destination'] != '': #if destination IP has fields
            if (re.search(ip_regex, rules['destination'])): #destination IP is valid
                pass
            else:
                rule_flag = False
                msg = QMessageBox()
                msg.setWindowTitle("Error, Try Again!")
                msg.setText("Destination IP Address is Invalid.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

        #Check if Ports are Valid
        try: #if "Src Port" and "Dst Port" is valid
            if rules['src_port'] != '':
                if 1 <= int(rules['src_port']) <= 65535:
                    pass
                else:
                    raise ValueError
            if rules['dst_port'] != '':
                if 1 <= int(rules['dst_port']) <= 65535:
                    pass
                else:
                    raise ValueError
        except ValueError: #catch the invalid and show popup about the error
            rule_flag = False
            msg = QMessageBox()
            msg.setWindowTitle("Error, Try Again!")
            msg.setText("Invalid Port Number, must be between 1 and 65535.")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

        #If the IP check passes, add rule to iptables (Default = True, if fails validation check set to False)
        if rule_flag:
            self.autocomplete(rules['source'],rules['destination'],rules['src_port'],rules['dst_port']) #sending valid inputs to autocomplete to be saved
        #Concatenate source, src_port, destination, dst_port to remove spaces when formatting bash command
            if rules['source'] != '':
                rules['source'] = ' --src ' + rules['source']
            if rules['src_port'] != '':
                rules['src_port'] = ' --sport ' + rules['src_port']
            if rules['destination'] != '':
                rules['destination'] = ' --dst ' + rules['destination']
            if rules['dst_port'] != '':
                rules['dst_port'] = ' --dport ' + rules['dst_port']
            remainder_rule = rules['source'] + rules['src_port'] + rules['destination'] + rules['dst_port']

            #print to see output format on commandline, testing
            #print(f"sudo iptables -R {rules['chain']} {rules['num']} --protocol {rules['protocol']} --jump {rules['action']}{remainder_rule}")
            #Run bash command to replace item in Linux iptables, command is built from dictionary variable values
            commandline = subprocess.Popen([f"sudo iptables -R {rules['chain']} {rules['num']} --protocol {rules['protocol']} --jump {rules['action']}{remainder_rule}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            output, stderr_output = commandline.communicate()
            self.view_rule() #calls view_rule function after adding rule (Updates iptable table on screen)

    #Remove rule to the actual iptable in Linux
    def remove_rule_button(self):
        removal = {} #dictionary, below is saving the value as a string type to concatenate
        removal['num'] = str(self.spinBox_Remove.value())
        removal['chain'] = self.RuleChain_Remove.currentText()
        #print to see output format on commandline
        #print(f"sudo iptables -D {removal['chain']} {removal['num']}")
        #Run bash command to remove rule from Linux iptables, command is built from dictionary variable values
        commandline = subprocess.Popen([f"sudo iptables -D {removal['chain']} {removal['num']}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        output, stderr_output = commandline.communicate()
        self.view_rule() #calls view_rule function after removing rule (Updates iptable table on screen after deletion)
        #toss error for nonexistent num and chain combination
        if int(removal['num']) == 0 or 'Index' in output.decode("utf-8"):
            self.num_error_popup()

    def num_error_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Invalid Num/Chain combination!")
        msg.setText("Must be an existing rule.")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()

    #Add rule to the actual iptable in Linux
    def add_rule_button(self):
        ip_regex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/(\\d|[1-2]\\d|3[0-2]))?$" #regular expression for IPv4 address + CIDR notation
        #ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$" #old regular expression for IPv4 address does not check for CIDR
        rule_flag = True #for checking if IP validation check passes
        boxes = {} #dictionary to store values from boxes
        boxes = {'num':self.spinBox,'chain':self.RuleChain,'protocol':self.TrafficType,'action':self.Action,'source':self.SrcIP,'src_port':self.SrcPort,'destination':self.DstIP,'dst_port':self.DstPort}
        #Reset rules for each instance. New iptable rule
        rules = {} #dictionary to store string representation value from variable "boxes" by toPlainText conversion, below is the conversion
        rules['num'] = str(boxes['num'].value()) #spinBox type is int but needs to be converted to string in order to be concatenated
        rules['chain'] = boxes['chain'].currentText() #Input, Forward, Output
        rules['protocol'] = boxes['protocol'].currentText() #TCP, UDP, IP, ICMP
        rules['action'] = boxes['action'].currentText() #Accept, Drop, Reject
        rules['source'] = boxes['source'].text() #Source IP Address
        rules['src_port'] = boxes['src_port'].text() #Source Port Number
        rules['destination'] = boxes['destination'].text() #Destination IP Address
        rules['dst_port'] = boxes['dst_port'].text() #Destination Port Number

        #Check if Source IP/Destination IP addresses is valid:
        if rules['source'] != '' and rules['destination'] != '': #if both boxes have fields
            if (re.search(ip_regex, rules['source']) and re.search(ip_regex, rules['destination'])): #if both valid via comparison
                pass
            else:
                rule_flag = False
                msg = QMessageBox()
                msg.setWindowTitle("Error, Try Again!")
                msg.setText("Source IP or Destination IP Address are Invalid.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        elif rules['source'] != '': #if source IP has fields
            if (re.search(ip_regex, rules['source'])): #source IP is valid
                pass
            else:
                rule_flag = False
                msg = QMessageBox()
                msg.setWindowTitle("Error, Try Again!")
                msg.setText("Source IP Address is Invalid.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()
        elif rules['destination'] != '': #if destination IP has fields
            if (re.search(ip_regex, rules['destination'])): #destination IP is valid
                pass
            else:
                rule_flag = False
                msg = QMessageBox()
                msg.setWindowTitle("Error, Try Again!")
                msg.setText("Destination IP Address is Invalid.")
                msg.setIcon(QMessageBox.Critical)
                msg.exec_()

        #Check if Ports are Valid
        try: #if "Src Port" and "Dst Port" is valid
            if rules['src_port'] != '':
                if 1 <= int(rules['src_port']) <= 65535:
                    pass
                else:
                    raise ValueError
            if rules['dst_port'] != '':
                if 1 <= int(rules['dst_port']) <= 65535:
                    pass
                else:
                    raise ValueError
        except ValueError: #catch the invalid and show popup about the error
            rule_flag = False
            msg = QMessageBox()
            msg.setWindowTitle("Error, Try Again!")
            msg.setText("Invalid Port Number, must be between 1 and 65535.")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

        #If the IP check passes, add rule to iptables (Default = True, if fails validation check set to False)
        if rule_flag:
            self.autocomplete(rules['source'],rules['destination'],rules['src_port'],rules['dst_port']) #sending valid inputs to autocomplete to be saved
        #Concatenate source, src_port, destination, dst_port to remove spaces when formatting bash command
            if rules['source'] != '':
                rules['source'] = ' --src ' + rules['source']
            if rules['src_port'] != '':
                rules['src_port'] = ' --sport ' + rules['src_port']
            if rules['destination'] != '':
                rules['destination'] = ' --dst ' + rules['destination']
            if rules['dst_port'] != '':
                rules['dst_port'] = ' --dport ' + rules['dst_port']
            remainder_rule = rules['source'] + rules['src_port'] + rules['destination'] + rules['dst_port']

            #insert mode if num spinbox is active
            if boxes['num'].value() > 0:
                #print to see output format on commandline
                #print(f"sudo iptables --insert {rules['chain']} {rules['num']} --protocol {rules['protocol']} --jump {rules['action']}{remainder_rule}")
                #Run bash command to insert to Linux iptables, command is built from dictionary variable values
                commandline = subprocess.Popen([f"sudo iptables --insert {rules['chain']} {rules['num']} --protocol {rules['protocol']} --jump {rules['action']}{remainder_rule}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                output, stderr_output = commandline.communicate()
                self.view_rule() #calls view_rule function after adding rule (Updates iptable table on screen)
                if "Index of insertion too big" in output.decode("utf-8"):
                    msg = QMessageBox()
                    msg.setWindowTitle("Error, Try Again!")
                    msg.setText("Index of insertion too big!")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec_()
            else: #otherwise it is just normal adding mode
                #print to see output format on commandline
                #print(f"sudo iptables --append {rules['chain']} --protocol {rules['protocol']} --jump {rules['action']}{remainder_rule}")
                #Run bash command to add to Linux iptables, command is built from dictionary variable values
                commandline = subprocess.Popen([f"sudo iptables --append {rules['chain']} --protocol {rules['protocol']} --jump {rules['action']}{remainder_rule}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                output, stderr_output = commandline.communicate()
                self.view_rule() #calls view_rule function after adding rule (Updates iptable table on screen)

    def switch_name(self):
        if self.spinBox.value() > 0:
            self.AddRule.setText(QtCore.QCoreApplication.translate("MainWindow", "Insert Rule"))
        else:
            self.AddRule.setText(QtCore.QCoreApplication.translate("MainWindow", "Add Rule"))

    #Will enable "Add Rule" button if dropdown box has changed from index 0 (placeholder values)
    def check_rule(self):
        if (self.RuleChain.currentIndex() > 0 and
            self.TrafficType.currentIndex() > 0 and
            self.Action.currentIndex() > 0):
            self.AddRule.setEnabled(True) #When all no longer placeholder, enable the "Add Rule" button
        else:
            self.AddRule.setEnabled(False) #Otherwise disable the button

    #Will enable "Update Rule" button if dropdown box has changed from index 0 (placeholder values)
    def update_check_rule(self):
        if (self.RuleChain.currentIndex() > 0 and
            self.TrafficType.currentIndex() > 0 and
            self.Action.currentIndex() > 0):
            self.UpdateRule.setEnabled(True) #When all no longer placeholder, enable the "Update Rule" button
        else:
            self.UpdateRule.setEnabled(False) #Otherwise disable the button

    #Disable text box if select ICMP or IP as "Traffic Type"
    def disable_box(self, index):
        if index!=3 and index!=4: #If TCP or UDP, enable edit
            self.SrcPort.setPlaceholderText("Src Port")
            self.SrcPort.setEnabled(True)
            self.DstPort.setPlaceholderText("Dst Port")
            self.DstPort.setEnabled(True)
        else: #Otherwise disable edit for ICMP and IP
            self.SrcPort.setText('') #clear SrcPort field, else data still transparent
            self.DstPort.setText('') #clear DstPort field, else data still transparent
            self.SrcPort.setPlaceholderText("N/A")
            self.SrcPort.setEnabled(False)
            self.DstPort.setPlaceholderText("N/A")
            self.DstPort.setEnabled(False)

    #Confirmation popup box to flushing the tables. Options: "Yes" or "Cancel"
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Flush iptables")
        msg.setText("Reset which iptable chain or ALL?")
        msg.setIcon(QMessageBox.Warning)
        #Four buttons added for which chain to flush on iptable
        msg.addButton(QPushButton('INPUT'), QMessageBox.NoRole)
        msg.addButton(QPushButton('FORWARD'), QMessageBox.RejectRole)
        msg.addButton(QPushButton('OUTPUT'), QMessageBox.HelpRole)
        msg.addButton(QPushButton('ALL'), QMessageBox.YesRole)
        msg.buttonClicked.connect(self.reset) #Activate from click on any button, calls reset function below
        msg.exec_() #Popup box appear on screen

    #Reset function after show_popup check
    def reset(self, whichButton):
        if whichButton.text() == "ALL": #if "Yes" button clicked, flush the tables via bash command
            reset = subprocess.Popen([f"sudo iptables -F"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            output, stderr_output = reset.communicate()
            self.view_rule() #calls the function to update with empty table
        elif whichButton.text() == "INPUT":
            reset = subprocess.Popen([f"sudo iptables -F INPUT"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            output, stderr_output = reset.communicate()
            self.view_rule()
        elif whichButton.text() == "FORWARD":
            reset = subprocess.Popen([f"sudo iptables -F FORWARD"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            output, stderr_output = reset.communicate()
            self.view_rule()
        elif whichButton.text() == "OUTPUT":
            reset = subprocess.Popen([f"sudo iptables -F OUTPUT"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            output, stderr_output = reset.communicate()
            self.view_rule()
        else:
            pass #Clicked Cancel, do nothing and exit

    #Clear all textbox and dropdown box to be empty
    def clear_text(self):
        self.spinBox.setValue(0)
        self.RuleChain.setCurrentIndex(0)
        self.TrafficType.setCurrentIndex(0)
        self.Action.setCurrentIndex(0)
        self.SrcIP.setText('')
        self.SrcPort.setText('')
        self.DstIP.setText('')
        self.DstPort.setText('')
        self.SrcPort.setPlaceholderText("Src Port")
        self.DstPort.setPlaceholderText("Dst Port")
        self.spinBox_Remove.setValue(0)
        self.RuleChain_Remove.setCurrentIndex(0)

    #Will unhide once field has value, and will hide again once empty
    def hidden_label(self):
        if self.RuleChain.currentIndex() > 0:
            self.RuleChainLabel.setHidden(False)
        else:
            self.RuleChainLabel.setHidden(True)
        if self.Action.currentIndex() > 0:
            self.ActionLabel.setHidden(False)
        else:
            self.ActionLabel.setHidden(True)
        if self.TrafficType.currentIndex() > 0:
            self.TrafficeTypeLabel.setHidden(False)
        else:
            self.TrafficeTypeLabel.setHidden(True)
        if self.SrcIP.text() != "":
            self.SourceLabel.setHidden(False)
        else:
            self.SourceLabel.setHidden(True)
        if self.SrcPort.text() != "":
            self.SrcPortLabel.setHidden(False)
        else:
            self.SrcPortLabel.setHidden(True)
        if self.DstIP.text() != "":
            self.DestinationLabel.setHidden(False)
        else:
            self.DestinationLabel.setHidden(True)
        if self.DstPort.text() != "":
            self.DestPortLabel.setHidden(False)
        else:
            self.DestPortLabel.setHidden(True)

    #Should have definitely used a container for these two functions.
    def unhide(self):
        self.spinBox.setHidden(False)
        self.Num.setHidden(False)
        self.RuleChain.setHidden(False)
        self.TrafficType.setHidden(False)
        self.Action.setHidden(False)
        self.SrcIP.setHidden(False)
        self.SrcPort.setHidden(False)
        self.DstIP.setHidden(False)
        self.DstPort.setHidden(False)
        self.Clear.setHidden(False)
    def hide(self):
        self.spinBox.setHidden(True)
        self.Num.setHidden(True)
        self.RuleChain.setHidden(True)
        self.TrafficType.setHidden(True)
        self.Action.setHidden(True)
        self.SrcIP.setHidden(True)
        self.SrcPort.setHidden(True)
        self.DstIP.setHidden(True)
        self.DstPort.setHidden(True)
        self.Clear.setHidden(True)

    def uncheck_update(self): #call by changes to Check_Update
        if self.Check_Update.isChecked(): #if update is checked, hide other buttons and show only "Update Rule" button
            self.Check_Remove.setChecked(False) #unchecks the remove checkbox so no error
            self.AddRule.setHidden(True)
            self.RemoveRule.setHidden(True)
            self.UpdateRule.setHidden(True)
            self.UpdateConfirm.setHidden(False) #only show Confirm Button
            self.clear_text()
            self.hide()
            #unhide two UI when checked
            self.spinBox_Remove.setHidden(False)
            self.Num_Remove.setHidden(False)
            self.RuleChain_Remove.setHidden(False)
            self.RuleChainLabel_Remove.setHidden(False)

        else: #for when update is unchecked bring back "Add Rule"
            self.AddRule.setHidden(False) #only show back the Add Rule Button
            self.UpdateConfirm.setHidden(True)
            self.UpdateRule.setHidden(True)
            #hide two UI when unchecked
            self.spinBox_Remove.setHidden(True)
            self.Num_Remove.setHidden(True)
            self.RuleChain_Remove.setHidden(True)
            self.RuleChainLabel_Remove.setHidden(True)
            self.clear_text() #clear text to have clean slate
            self.unhide() #calling unhide function to show all original UI

    def uncheck_remove(self): #call by changes to Check_Remove
        if self.Check_Remove.isChecked(): #if remove is checked, hide other buttons and show only "Remove Rule" button
            self.Check_Update.setChecked(False) #unchecks the update checkbox so no error
            self.AddRule.setHidden(True)
            self.UpdateRule.setHidden(True)
            self.RemoveRule.setHidden(False) #only show Remove Rule Button
            #unhide two UI when checked
            self.spinBox_Remove.setHidden(False)
            self.Num_Remove.setHidden(False)
            self.RuleChain_Remove.setHidden(False)
            self.RuleChainLabel_Remove.setHidden(False)
            self.clear_text() #clear text to have clean slate
            self.hide() #calling hide function to hide all original UI
        else: #for when remove is unchecked bring back "Add Rule"
            self.AddRule.setHidden(False)
            self.RemoveRule.setHidden(True)
            #hide two UI when unchecked
            self.spinBox_Remove.setHidden(True)
            self.Num_Remove.setHidden(True)
            self.RuleChain_Remove.setHidden(True)
            self.RuleChainLabel_Remove.setHidden(True)
            self.clear_text() #clear text to have clean slate
            self.unhide() #calling unhide function to show all original UI

    #Autocomplete option for when need to access previous inputted IP address, called by add_rule_button after validation check
    def autocomplete(self, srcIP, dstIP, srcPort, dstPort):
        #append valid inputs to respective lists, only if it is a unique entry
        if srcIP not in src_ip:
            src_ip.append(srcIP)
        if dstIP not in dst_ip:
            dst_ip.append(dstIP)
        if srcPort not in src_port:
            src_port.append(srcPort)
        if dstPort not in dst_port:
            dst_port.append(dstPort)
        #grab all items from lists and convert to Qcompleter type
        src_ip_com = QtWidgets.QCompleter(src_ip)
        dst_ip_com = QtWidgets.QCompleter(dst_ip)
        src_port_com = QtWidgets.QCompleter(src_port)
        dst_port_com = QtWidgets.QCompleter(dst_port)
        #set autocomplete options taken from conversion of _com for respective lineEdit boxes
        self.SrcIP.setCompleter(src_ip_com)
        self.DstIP.setCompleter(dst_ip_com)
        self.SrcPort.setCompleter(src_port_com)
        self.DstPort.setCompleter(dst_port_com)

    #Will enable "Remove Rule" button if the "Chain Rule" (for removal) dropdown box has been changed
    def check_remove(self):
        if self.RuleChain_Remove.currentIndex() > 0:
            self.RemoveRule.setEnabled(True)
        else:
            self.RemoveRule.setEnabled(False)

    #Will enable "Confirm" button if the "Chain Rule" (for update) dropdown box has been changed
    def check_update(self):
        if self.RuleChain_Remove.currentIndex() > 0:
            self.UpdateConfirm.setEnabled(True)
        else:
            self.UpdateConfirm.setEnabled(False)

### DUNDER CHECK ###
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
