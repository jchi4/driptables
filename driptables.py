#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import subprocess,re,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
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
        MainWindow.resize(1413, 881)
        MainWindow.setStyleSheet("font: 13pt \"Roboto Slab\";\n""")
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
        self.Reset.setGeometry(QtCore.QRect(1270, 780, 131, 41))
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
        self.RuleView = QtWidgets.QScrollArea(self.centralwidget)
        self.RuleView.setGeometry(QtCore.QRect(10, 10, 1381, 581))
        self.RuleView.setStyleSheet("background-color: rgb(61, 56, 70);")
        self.RuleView.setWidgetResizable(True)
        self.RuleView.setObjectName("RuleView")
        self.RuleArea = QtWidgets.QWidget()
        self.RuleArea.setGeometry(QtCore.QRect(0, 0, 1379, 579))
        self.RuleArea.setObjectName("RuleArea")
        self.Title = QtWidgets.QLabel(self.RuleArea)
        self.Title.setGeometry(QtCore.QRect(580, 0, 191, 19))
        self.Title.setObjectName("Title")
        self.showL = QtWidgets.QTextBrowser(self.RuleArea)
        self.showL.setGeometry(QtCore.QRect(20, 30, 1331, 531))
        self.showL.setObjectName("showL")
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
        self.Check_Add.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.Check_Add.setObjectName("Check_Add")
        self.Check_Remove = QtWidgets.QCheckBox(self.centralwidget)
        self.Check_Remove.setGeometry(QtCore.QRect(820, 780, 91, 31))
        self.Check_Remove.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.Check_Remove.setObjectName("Check_Remove")
        self.Check_Update = QtWidgets.QCheckBox(self.centralwidget)
        self.Check_Update.setGeometry(QtCore.QRect(820, 750, 91, 31))
        self.Check_Update.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
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
        self.toolButton.setGeometry(QtCore.QRect(10, 790, 61, 26))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1413, 28))
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

        #When a button is clicked (fuction calls)
        self.AddRule.clicked.connect(self.add_rule_button) #calls add_rule_button function when clicked. (Adds rule)
        self.RemoveRule.clicked.connect(self.remove_rule_button) #call remove_rule_button when clicked. (Removes rule)
        self.Reset.clicked.connect(self.show_popup) #calls show_popup function when clicked. (Confirmation screen)
        self.Clear.clicked.connect(self.clear_text) #calls clear_text when clicked. (Clear box text)
        self.TrafficType.currentIndexChanged.connect(self.disable_box) #calls disable_box when "Traffic Type" dropdown value changes. Checks for ICMP/IP

        #set buttons state
        self.AddRule.setEnabled(False) #set "Add Rule" button unclickable for beginning
        self.UpdateRule.setEnabled(False) #set "Update Rule" button unclickable for beginning
        self.RemoveRule.setEnabled(False) #set "Remove Rule" button unclickable for beginning

        #Calls check_rule, if "RuleChain, TrafficType, Action" are changed from index 0. Allows "Add Rule" button to be active
        self.RuleChain.currentIndexChanged.connect(self.check_rule)
        self.TrafficType.currentIndexChanged.connect(self.check_rule)
        self.Action.currentIndexChanged.connect(self.check_rule)

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
        self.RuleChain.currentIndexChanged.connect(self.check_update)

        #View iptable rules on screen via GUI, initially running "sudo iptables -L" by calling function "view_rule"
        self.view_rule()

        #Checkbox state, set buttons for both to be hidden from beginning, only "Add Rule" by default
        self.UpdateRule.setHidden(True)
        self.RemoveRule.setHidden(True)

        #Set Character Limit, 15 for IP including '.' and 5 for Port since 65535
        self.SrcIP.setMaxLength(18)
        self.SrcPort.setMaxLength(5)
        self.DstIP.setMaxLength(18)
        self.DstPort.setMaxLength(5)
        self.spinBox.setMinimum(1)
        self.spinBox_Remove.setMinimum(1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "driptables"))
        self.RuleChain.setItemText(1, _translate("MainWindow", "INPUT"))
        self.RuleChain.setItemText(2, _translate("MainWindow", "FORWARD"))
        self.RuleChain.setItemText(3, _translate("MainWindow", "OUTPUT"))
        self.RuleChain.setItemText(4, _translate("MainWindow", "PREROUTING"))
        self.TrafficType.setItemText(1, _translate("MainWindow", "TCP"))
        self.TrafficType.setItemText(2, _translate("MainWindow", "UDP"))
        self.TrafficType.setItemText(3, _translate("MainWindow", "IP"))
        self.TrafficType.setItemText(4, _translate("MainWindow", "ICMP"))
        self.Action.setCurrentText(_translate("MainWindow", "Action"))
        self.Action.setItemText(0, _translate("MainWindow", "Action"))
        self.Action.setItemText(1, _translate("MainWindow", "ACCEPT"))
        self.Action.setItemText(2, _translate("MainWindow", "DROP"))
        self.Action.setItemText(3, _translate("MainWindow", "REJECT"))
        self.Clear.setText(_translate("MainWindow", "CLEAR"))
        self.AddRule.setText(_translate("MainWindow", "Add Rule"))
        self.Reset.setText(_translate("MainWindow", "Reset Rules"))
        self.UpdateRule.setText(_translate("MainWindow", "Update Rule"))
        self.Title.setText(_translate("MainWindow", "Current IP Tables Rules"))
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
        self.RemoveRule.setText(_translate("MainWindow", "Remove Rule"))
        self.RuleChain_Remove.setItemText(1, _translate("MainWindow", "INPUT"))
        self.RuleChain_Remove.setItemText(2, _translate("MainWindow", "FORWARD"))
        self.RuleChain_Remove.setItemText(3, _translate("MainWindow", "OUTPUT"))
        self.RuleChain_Remove.setItemText(4, _translate("MainWindow", "PREROUTING"))
        self.Num_Remove.setText(_translate("MainWindow", "Num"))
        self.RuleChainLabel_Remove.setText(_translate("MainWindow", "Rule Chain"))
        self.SrcIP.setPlaceholderText(_translate("MainWindow", "Source IP"))
        self.DstIP.setPlaceholderText(_translate("MainWindow", "Destination IP"))
        self.SrcPort.setPlaceholderText(_translate("MainWindow", "Src Port"))
        self.DstPort.setPlaceholderText(_translate("MainWindow", "Dst Port"))
        self.toolButton.setText(_translate("MainWindow", "Info"))
        self.menuSave.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionRestore.setText(_translate("MainWindow", "Restore"))

### HELPER FUNCTIONS ###
    def uncheck_update(self): #call by changes to Check_Update
        if self.Check_Update.isChecked(): #if update is checked, hide other buttons and show only "Update Rule" button
            self.Check_Remove.setChecked(False) #unchecks the remove checkbox so no error
            self.AddRule.setHidden(True)
            self.RemoveRule.setHidden(True)
            self.UpdateRule.setHidden(False)
            self.clear_text()
            self.disable_buttons()

        else: #for when update is unchecked bring back "Add Rule"
            self.AddRule.setHidden(False)
            self.UpdateRule.setHidden(True)
            self.clear_text()
            self.enable_buttons()

    def uncheck_remove(self): #call by changes to Check_Remove
        if self.Check_Remove.isChecked(): #if remove is checked, hide other buttons and show only "Remove Rule" button
            self.Check_Update.setChecked(False) #unchecks the update checkbox so no error
            self.AddRule.setHidden(True)
            self.UpdateRule.setHidden(True)
            self.RemoveRule.setHidden(False)
            #hiding all UI, and only show two UI boxes
            self.clear_text() #clear text to have clean slate
            self.hide() #calling hide function to hide all original UI
            #unhide two UI when checked
            self.spinBox_Remove.setHidden(False)
            self.Num_Remove.setHidden(False)
            self.RuleChain_Remove.setHidden(False)
            self.RuleChainLabel_Remove.setHidden(False)
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

    #Iptables Rule List, is called and then updates the table to have latest entry of the iptable on Linux machine
    def view_rule(self):
        view_all = subprocess.Popen(["sudo iptables -L -n --line-numbers"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True) #storing bash command to a variable "view_all"
        current, stderr_current = view_all.communicate() #stderr_current is holding metadata unimportant whereas current holds value of output from command
        current = current.decode("utf-8") #data type is "bytes" so needs to use decode to transfer to type "string"
        self.showL.setText(current)
        self.showL.selectAll() #selecting all plaintext
        self.showL.setAlignment(QtCore.Qt.AlignCenter) #centering all text selected in previous statement

    #Will enable "Remove Rule" button if the "Chain Rule" (for removal) dropdown box has been changed
    def check_remove(self):
        if self.RuleChain_Remove.currentIndex() > 0:
            self.RemoveRule.setEnabled(True)
        else:
            self.RemoveRule.setEnabled(False)

    #Will enable "Update Rule" button if the "Chain Rule" dropdown box has been changed
    def check_update(self):
        if self.Check_Update.isChecked(): #check if Update is checked first before doing all remaining tasks
            if self.RuleChain.currentIndex() > 0:
                self.enable_buttons()
                self.UpdateRule.setEnabled(True)
                if self.RuleChain.currentText() == "INPUT":
                    pass #parse and match from iptable correct rule to populate (Traffic Type, Action, SrcIP, SrcPort, DstIP, DstPort)
                elif self.RuleChain.currentText() == "FORWARD":
                    pass #parse and match from iptable correct rule to populate (Traffic Type, Action, SrcIP, SrcPort, DstIP, DstPort)
                elif self.RuleChain.currentText() == "OUTPUT":
                    pass #parse and match from iptable correct rule to populate (Traffic Type, Action, SrcIP, SrcPort, DstIP, DstPort)
                else:
                    pass
            else:
                self.disable_buttons()
                self.UpdateRule.setEnabled(False)
        else:
            self.UpdateRule.setEnabled(False)

    #Will enable "Add Rule" button if dropdown box has changed from index 0 (placeholder values)
    def check_rule(self):
        if (self.RuleChain.currentIndex() > 0 and
            self.TrafficType.currentIndex() > 0 and
            self.Action.currentIndex() > 0):
            self.AddRule.setEnabled(True) #When all no longer placeholder, enable the "Add Rule" button
        else:
            self.AddRule.setEnabled(False) #Otherwise disable the button

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

    #Remove rule to the actual iptable in Linux
    def remove_rule_button(self):
        removal = {} #dictionary, below is saving the value as a string type to concatenate
        removal['num'] = str(self.spinBox_Remove.value())
        removal['chain'] = self.RuleChain_Remove.currentText()

        #*** Need a validation method to find out if a rule is existent, implement later ***

        #print to see output format on commandline
        print(f"sudo iptables -D {removal['chain']} {removal['num']}")
        #Run bash command to remove rule from Linux iptables, command is built from dictionary variable values
        commandline = subprocess.Popen([f"sudo iptables -D {removal['chain']} {removal['num']}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        output, stderr_output = commandline.communicate()
        self.view_rule() #calls view_rule function after removing rule (Updates iptable table on screen after deletion)

    #Add rule to the actual iptable in Linux
    def add_rule_button(self):
        ip_regex = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])(\\/(\\d|[1-2]\\d|3[0-2]))?$" #regular expression for IPv4 address + CIDR notation
        #ip_regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$" #old regular expression for IPv4 address does not check for CIDR
        rule_flag = True #for checking if IP validation check passes
        boxes = {} #dictionary to store values from boxes
        boxes = {'chain':self.RuleChain,'protocol':self.TrafficType,'action':self.Action,'source':self.SrcIP,'src_port':self.SrcPort,'destination':self.DstIP,'dst_port':self.DstPort}
        #Reset rules for each instance. New iptable rule
        rules = {} #dictionary to store string representation value from variable "boxes" by toPlainText conversion, below is the conversion
        rules['chain'] = boxes['chain'].currentText() #Input, Forward, Output, Prerouting
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
                msg.setText("Source IP and Destination IP Address are Invalid.")
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

            #print to see output format on commandline
            print(f"sudo iptables --append {rules['chain']} --protocol {rules['protocol']} --jump {rules['action']}{remainder_rule}")
            #Run bash command to add to Linux iptables, command is built from dictionary variable values
            commandline = subprocess.Popen([f"sudo iptables --append {rules['chain']} --protocol {rules['protocol']} --jump {rules['action']}{remainder_rule}"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            output, stderr_output = commandline.communicate()
            self.view_rule() #calls view_rule function after adding rule (Updates iptable table on screen)

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
        self.spinBox.setValue(1)
        self.RuleChain.setCurrentIndex(0)
        self.TrafficType.setCurrentIndex(0)
        self.Action.setCurrentIndex(0)
        self.SrcIP.setText('')
        self.SrcPort.setText('')
        self.DstIP.setText('')
        self.DstPort.setText('')
        self.SrcPort.setPlaceholderText("Src Port")
        self.DstPort.setPlaceholderText("Dst Port")
        self.spinBox_Remove.setValue(1)
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

    def disable_buttons(self):
        self.TrafficType.setEnabled(False)
        self.Action.setEnabled(False)
        self.SrcIP.setEnabled(False)
        self.SrcPort.setEnabled(False)
        self.DstIP.setEnabled(False)
        self.DstPort.setEnabled(False)

    def enable_buttons(self):
        self.TrafficType.setEnabled(True)
        self.Action.setEnabled(True)
        self.SrcIP.setEnabled(True)
        self.SrcPort.setEnabled(True)
        self.DstIP.setEnabled(True)
        self.DstPort.setEnabled(True)

### DUNDER CHECK ###
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
