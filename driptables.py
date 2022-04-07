#!/usr/bin/env python3
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import os
rule_table = []

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        #global variables to grab value for iptable command
        global RuleChain
        global TrafficType
        global Action
        global SrcIP
        global SrcPort
        global DstIP
        global DstPort
        #GUI skeleton code
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1407, 966)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RuleChain = QtWidgets.QComboBox(self.centralwidget)
        self.RuleChain.setGeometry(QtCore.QRect(40, 250, 151, 61))
        self.RuleChain.setObjectName("RuleChain")
        self.RuleChain.addItem("")
        self.RuleChain.addItem("")
        self.RuleChain.addItem("")
        self.RuleChain.addItem("")
        self.RuleChain.addItem("")
        self.TrafficType = QtWidgets.QComboBox(self.centralwidget)
        self.TrafficType.setGeometry(QtCore.QRect(210, 250, 151, 61))
        self.TrafficType.setObjectName("TrafficType")
        self.TrafficType.addItem("")
        self.TrafficType.addItem("")
        self.TrafficType.addItem("")
        self.TrafficType.addItem("")
        self.TrafficType.addItem("")
        self.Action = QtWidgets.QComboBox(self.centralwidget)
        self.Action.setGeometry(QtCore.QRect(380, 250, 151, 61))
        self.Action.setPlaceholderText("")
        self.Action.setFrame(True)
        self.Action.setObjectName("Action")
        self.Action.addItem("")
        self.Action.addItem("")
        self.Action.addItem("")
        self.Action.addItem("")
        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(1220, 260, 87, 27))
        self.Reset.setObjectName("Reset")
        self.SrcIP = QtWidgets.QTextEdit(self.centralwidget)
        self.SrcIP.setGeometry(QtCore.QRect(550, 250, 211, 61))
        self.SrcIP.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SrcIP.setAutoFillBackground(False)
        self.SrcIP.setTabChangesFocus(False)
        self.SrcIP.setMarkdown("")
        self.SrcIP.setObjectName("SrcIP")
        self.AppendRule = QtWidgets.QPushButton(self.centralwidget)
        self.AppendRule.setGeometry(QtCore.QRect(570, 630, 201, 91))
        self.AppendRule.setObjectName("AppendRule")
        #added functionality to when the Append Rule button is clicked
        self.AppendRule.clicked.connect(self.add_rule_button) #calls the add_rule_button function
        self.SrcPort = QtWidgets.QTextEdit(self.centralwidget)
        self.SrcPort.setGeometry(QtCore.QRect(780, 250, 71, 61))
        self.SrcPort.setObjectName("SrcPort")
        self.DstIP = QtWidgets.QTextEdit(self.centralwidget)
        self.DstIP.setGeometry(QtCore.QRect(870, 250, 211, 61))
        self.DstIP.setObjectName("DstIP")
        self.DstPort = QtWidgets.QTextEdit(self.centralwidget)
        self.DstPort.setGeometry(QtCore.QRect(1100, 250, 71, 61))
        self.DstPort.setObjectName("DstPort")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1407, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "iptables"))
        self.RuleChain.setItemText(0, _translate("MainWindow", "Rule Chain"))
        self.RuleChain.setItemText(1, _translate("MainWindow", "INPUT"))
        self.RuleChain.setItemText(2, _translate("MainWindow", "FORWARD"))
        self.RuleChain.setItemText(3, _translate("MainWindow", "OUTPUT"))
        self.RuleChain.setItemText(4, _translate("MainWindow", "PREROUTING"))
        self.TrafficType.setItemText(0, _translate("MainWindow", "Traffic Type"))
        self.TrafficType.setItemText(1, _translate("MainWindow", "TCP"))
        self.TrafficType.setItemText(2, _translate("MainWindow", "UDP"))
        self.TrafficType.setItemText(3, _translate("MainWindow", "IP"))
        self.TrafficType.setItemText(4, _translate("MainWindow", "ICMP"))
        self.Action.setCurrentText(_translate("MainWindow", "Action"))
        self.Action.setItemText(0, _translate("MainWindow", "Action"))
        self.Action.setItemText(1, _translate("MainWindow", "ACCEPT"))
        self.Action.setItemText(2, _translate("MainWindow", "DROP"))
        self.Action.setItemText(3, _translate("MainWindow", "REJECT"))
        self.Reset.setText(_translate("MainWindow", "RESET"))
        self.SrcIP.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.SrcIP.setPlaceholderText(_translate("MainWindow", "Source IP"))
        self.AppendRule.setText(_translate("MainWindow", "Append Rule"))
        self.SrcPort.setPlaceholderText(_translate("MainWindow", "Src Port"))
        self.DstIP.setPlaceholderText(_translate("MainWindow", "Destination IP"))
        self.DstPort.setPlaceholderText(_translate("MainWindow", "Dest IP"))

    #Helper Functions

    #function to append rule to the actual iptable in Linux
    def add_rule_button(self):
        global boxes
        boxes = {}
        boxes = {'chain':self.RuleChain,'protocol':self.TrafficType,'action':self.Action,'source':self.SrcIP,'src_port':self.SrcPort,'destination':self.DstIP,'dst_port':self.DstPort}
        rule_table.append(boxes)

        #resetting the rules and each instance for new iptable rules
        rules = {} #dictionary to store string representation value from what is in memory in variable boxes

        #series of redundant steps for coverting memory address to readable string but will change later to just be effect in commandline variable
        #Input, Forward, Output, Prerouting
        rules['chain'] = boxes['chain'].currentText()

        #TCP, UDP, IP, ICMP
        rules['protocol'] = boxes['protocol'].currentText()

        #Accept, Drop, Reject
        rules['action'] = boxes['action'].currentText()

        #Source IP Address
        rules['source'] = boxes['source'].toPlainText()

        #Source Port Number
        rules['src_port'] = boxes['src_port'].toPlainText()

        #Destination IP Address
        rules['destination'] = boxes['destination'].toPlainText()

        #Destination Port Number
        rules['dst_port'] = boxes['dst_port'].toPlainText()

        #print(rules) - Rule testing
        commandline = subprocess.Popen([f"sudo iptables --append {rules['chain']} --protocol {rules['protocol']} --jump {rules['action']} --src {rules['source']} --sport {rules['src_port']} --dst {rules['destination']} --dport {rules['dst_port']}"], stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
        #Testing the append rule button
        #print(f"sudo iptables --append {boxes['chain'].currentText()} --protocol {boxes['protocol']} --jump {boxes['action']} --src {boxes['source']} --sport {boxes['src_port']} --dst {boxes['destination']} --dport {boxes['dst_port']}")
        output, stderr_output = commandline.communicate()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec_()
