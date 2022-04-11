#!/usr/bin/env python3

### IMPORT STATEMENTS ###
import subprocess,re,sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#global variables so that when autocomplete function is called does not reset containers
src_ip = []
dst_ip = []
src_port = []
dst_port = []
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1407, 966)
        MainWindow.setStyleSheet("font: 13pt \"Roboto Slab\";\n""")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RuleChain = QtWidgets.QComboBox(self.centralwidget)
        self.RuleChain.setGeometry(QtCore.QRect(70, 620, 151, 61))
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
        self.TrafficType.setGeometry(QtCore.QRect(240, 620, 151, 61))
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
        self.Action.setGeometry(QtCore.QRect(410, 620, 151, 61))
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
        self.Clear.setGeometry(QtCore.QRect(1240, 630, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear")
        self.AddRule = QtWidgets.QPushButton(self.centralwidget)
        self.AddRule.setGeometry(QtCore.QRect(480, 720, 201, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.AddRule.setFont(font)
        self.AddRule.setObjectName("AddRule")
        self.SrcPort = QtWidgets.QLineEdit(self.centralwidget)
        self.SrcPort.setGeometry(QtCore.QRect(810, 620, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SrcPort.setFont(font)
        self.SrcPort.setObjectName("SrcPort")
        self.DstIP = QtWidgets.QLineEdit(self.centralwidget)
        self.DstIP.setGeometry(QtCore.QRect(910, 620, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DstIP.setFont(font)
        self.DstIP.setObjectName("DstIP")
        self.DstPort = QtWidgets.QLineEdit(self.centralwidget)
        self.DstPort.setGeometry(QtCore.QRect(1140, 620, 81, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.DstPort.setFont(font)
        self.DstPort.setObjectName("DstPort")
        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(610, 850, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Reset.setFont(font)
        self.Reset.setObjectName("Reset")
        self.UpdateRule = QtWidgets.QPushButton(self.centralwidget)
        self.UpdateRule.setGeometry(QtCore.QRect(690, 720, 201, 91))
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
        self.label = QtWidgets.QLabel(self.RuleArea)
        self.label.setGeometry(QtCore.QRect(610, 0, 111, 19))
        self.label.setObjectName("label")
        self.showL = QtWidgets.QTextBrowser(self.RuleArea)
        self.showL.setObjectName("showL")
        self.showL.setGeometry(QtCore.QRect(20, 30, 1331, 531))
        self.RuleView.setWidget(self.RuleArea)
        self.SourceLabel = QtWidgets.QLabel(self.centralwidget)
        self.SourceLabel.setGeometry(QtCore.QRect(650, 600, 81, 19))
        self.SourceLabel.setObjectName("SourceLabel")
        self.SrcPortLabel = QtWidgets.QLabel(self.centralwidget)
        self.SrcPortLabel.setGeometry(QtCore.QRect(820, 600, 71, 19))
        self.SrcPortLabel.setObjectName("SrcPortLabel")
        self.DestinationLabel = QtWidgets.QLabel(self.centralwidget)
        self.DestinationLabel.setGeometry(QtCore.QRect(960, 600, 121, 19))
        self.DestinationLabel.setObjectName("DestinationLabel")
        self.DestPortLabel = QtWidgets.QLabel(self.centralwidget)
        self.DestPortLabel.setGeometry(QtCore.QRect(1150, 600, 71, 19))
        self.DestPortLabel.setObjectName("DestPortLabel")
        self.ActionLabel = QtWidgets.QLabel(self.centralwidget)
        self.ActionLabel.setGeometry(QtCore.QRect(460, 600, 61, 19))
        self.ActionLabel.setObjectName("ActionLabel")
        self.TrafficeTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.TrafficeTypeLabel.setGeometry(QtCore.QRect(270, 600, 101, 19))
        self.TrafficeTypeLabel.setObjectName("TrafficeTypeLabel")
        self.RuleChainLabel = QtWidgets.QLabel(self.centralwidget)
        self.RuleChainLabel.setGeometry(QtCore.QRect(100, 600, 91, 19))
        self.RuleChainLabel.setObjectName("RuleChainLabel")
        self.SrcIP = QtWidgets.QLineEdit(self.centralwidget)
        self.SrcIP.setGeometry(QtCore.QRect(580, 620, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Slab")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.SrcIP.setFont(font)
        self.SrcIP.setObjectName("SrcIP")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1407, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #When a button is clicked (fuction calls)
        self.AddRule.clicked.connect(self.add_rule_button) #calls add_rule_button function when clicked. (Adds rule)
        self.Reset.clicked.connect(self.show_popup) #calls show_popup function when clicked. (Confirmation screen)
        self.Clear.clicked.connect(self.clear_text) #calls clear_text when clicked. (Clear box text)
        self.TrafficType.currentIndexChanged.connect(self.disable_box) #calls disable_box when "Traffic Type" dropdown value changes. Checks for ICMP/IP

        #set buttons state
        self.AddRule.setEnabled(False) #set "Add Rule" button unclickable for beginning
        self.UpdateRule.setEnabled(False) #set "Update Rule" button unclickable for beginning

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

        #View iptable rules on screen via GUI, initially running "sudo iptables -L" by calling function "view_rule"
        self.view_rule()

        #Set Character Limit, 15 for IP including '.' and 5 for Port since 65535
        self.SrcIP.setMaxLength(18)
        self.SrcPort.setMaxLength(5)
        self.DstIP.setMaxLength(18)
        self.DstPort.setMaxLength(5)

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
        self.Clear.setText(_translate("MainWindow", "Clear"))
        self.AddRule.setText(_translate("MainWindow", "Add Rule"))
        self.SrcPort.setPlaceholderText(_translate("MainWindow", "Src Port"))
        self.DstIP.setPlaceholderText(_translate("MainWindow", "Destination IP"))
        self.DstPort.setPlaceholderText(_translate("MainWindow", "Dst Port"))
        self.Reset.setText(_translate("MainWindow", "Reset All Rules"))
        self.UpdateRule.setText(_translate("MainWindow", "Update Rule"))
        self.label.setText(_translate("MainWindow", "Current Rules"))
        self.SourceLabel.setText(_translate("MainWindow", "Source IP"))
        self.SrcPortLabel.setText(_translate("MainWindow", "Src Port"))
        self.DestinationLabel.setText(_translate("MainWindow", "Destination IP"))
        self.DestPortLabel.setText(_translate("MainWindow", "Dst Port"))
        self.ActionLabel.setText(_translate("MainWindow", "Action"))
        self.TrafficeTypeLabel.setText(_translate("MainWindow", "Traffic Type"))
        self.RuleChainLabel.setText(_translate("MainWindow", "Rule Chain"))
        self.SrcIP.setPlaceholderText(_translate("MainWindow", "Source IP"))

### HELPER FUNCTIONS ###
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


    #Will enable "Add Rule" button if dropdown box have changed from index 0 (placeholder values)
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
        msg.setText("Reset all iptable rules?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.Cancel) #Two buttons, "Yes" or "Cancel"
        msg.setDefaultButton(QMessageBox.Cancel) #Default button = "Cancel" for clarity, in case mistakenly flush iptables
        msg.buttonClicked.connect(self.reset) #Activate from click on any button, calls reset function below
        msg.exec_() #Popup box appear on screen

    #Reset function after show_popup check
    def reset(self, whichButton):
        if whichButton.text() == "&Yes": #if "Yes" button clicked, flush the tables via bash command
            reset = subprocess.Popen([f"sudo iptables -F"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
            output, stderr_output = reset.communicate()
            self.view_rule() #calls the function to update with empty table
        else:
            pass #Clicked Cancel, do nothing and exit

    #Clear all textbox and dropdown box to be empty
    def clear_text(self):
        self.RuleChain.setCurrentIndex(0)
        self.TrafficType.setCurrentIndex(0)
        self.Action.setCurrentIndex(0)
        self.SrcIP.setText('')
        self.SrcPort.setText('')
        self.DstIP.setText('')
        self.DstPort.setText('')
        self.SrcPort.setPlaceholderText("Src Port")
        self.DstPort.setPlaceholderText("Dst Port")

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

### DUNDER CHECK ###
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
