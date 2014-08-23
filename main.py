from PyQt4 import QtCore, QtGui
import urllib , os , configparser, pynotify

config = configparser.ConfigParser()
config.read('data/conf.ini')
pynotify.init("image")

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        Form.setMinimumSize(QtCore.QSize(800, 600))
        Form.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("data/megaglest.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(_fromUtf8("color:#fff;"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("data/mg_launcher.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(200, 10, 590, 581))
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.checkBox = QtGui.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(100, 520, 101, 21))
        self.checkBox.setStyleSheet(_fromUtf8("color:#000;"))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 520, 74, 21))
        self.checkBox_2.setStyleSheet(_fromUtf8("color:#000;"))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 520, 85, 23))
        self.pushButton_2.setStyleSheet(_fromUtf8("color:#000;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.treeWidget = QtGui.QTreeWidget(self.tab)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 581, 511))
        self.treeWidget.setStyleSheet(_fromUtf8("background:#294b7c;"))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.listWidget_2 = QtGui.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(440, 0, 141, 511))
        self.listWidget_2.setStyleSheet(_fromUtf8("background:#294b7c;"))
        self.listWidget_2.setFrameShadow(QtGui.QFrame.Plain)
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        item = QtGui.QListWidgetItem()
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("data/shaman.bmp")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon1)
        self.listWidget_2.addItem(item)
        self.lineEdit = QtGui.QLineEdit(self.tab_2)
        self.lineEdit.setGeometry(QtCore.QRect(0, 520, 581, 31))
        self.lineEdit.setStyleSheet(_fromUtf8("color:#000;"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 441, 521))
        self.plainTextEdit.setStyleSheet(_fromUtf8("background:#294b7c;"))
        self.plainTextEdit.setFrameShadow(QtGui.QFrame.Plain)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText(_fromUtf8(""))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 550, 181, 40))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(_fromUtf8("background:rgb(0, 128, 0);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 171, 431))
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.pushButton_2.setEnabled(False)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
        self.treeWidget.clicked.connect(self.updateJoinGame)
        self.pushButton_2.clicked.connect(self.joinGame)
        self.pushButton.clicked.connect(self.startMegaglest)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Megaglest Lobby", None))
        self.checkBox.setText(_translate("Form", "Auto Join", None))
        self.checkBox_2.setText(_translate("Form", "Notify", None))
        self.pushButton_2.setText(_translate("Form", "Join", None))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Status", None))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Title", None))
        self.treeWidget.headerItem().setText(2, _translate("Form", "Techtree", None))
        self.treeWidget.headerItem().setText(3, _translate("Form", "Map", None))
        self.treeWidget.headerItem().setText(4, _translate("Form", "Players", None))
        self.treeWidget.headerItem().setText(5, _translate("Form", "Slots", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Games", None))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("Form", "ChanServ", None))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Chat", None))
        self.pushButton.setText(_translate("Form", "Start Megaglest", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>New updates available:</p><p>- Megaglest 3.9.3</p><p>- TowerDefense #17</p><p><br/></p><p><a href=\"#update\"><span style=\" text-decoration: underline; color:#0057ae;\">Click here</span></a> to update.</p></body></html>", None))
        self.treeWidget.header().resizeSection(0,120)
        self.treeWidget.header().resizeSection(1,120)
        self.treeWidget.header().resizeSection(2,120)
        self.treeWidget.header().resizeSection(3,120)
        self.treeWidget.header().resizeSection(4,50)
        self.treeWidget.header().resizeSection(5,40)
        self.checkMGdir()
    
    servers_oldList = "x"
    servers_ip = []
    
    def checkMGdir(self):
        if not os.path.isfile(config['MGLauncher']['mg_dir']):
            mg_dir = str(QtGui.QFileDialog.getExistingDirectory(None,'Select Megaglest directory',os.path.expanduser('~')))
            mg_dir += "/start_megaglest"
            config['MGLauncher']['mg_dir'] = mg_dir
            with open('data/conf.ini', 'w') as configfile:
                config.write(configfile)
                
            self.checkMGdir()
        else:
            self.updateServers()
    
    def updateServers(self):
        servers_list = urllib.urlopen("http://play.mg/showServersForGlest.php")
        servers_data = servers_list.read()
        if servers_data != Ui_Form.servers_oldList:
            self.treeWidget.clear()
            Ui_Form.servers_ip = []
            fields = servers_data.split("|")
            servers_count = len(fields)/14
            repeat = 0
            notifyUser = False
            while servers_count != repeat:
                offset = repeat * 14
                status_code = int(fields[13+offset])
                status_label = "Unknown"
                if status_code == 0:
                    status_label = "Waiting for players"
                    if int(fields[10+offset]) > 0:
                        status_label = "Accepting players"
                        notifyUser = True
                elif status_code == 1:
                    status_label = "Game full, pending start"
                elif status_code == 2:
                    status_label = "In progress"

                item = QtGui.QTreeWidgetItem([status_label,fields[3+offset],fields[5+offset],fields[6+offset],fields[11+offset],fields[8+offset]])
                Ui_Form.servers_ip.append([fields[4+offset],fields[11+offset]])
                self.treeWidget.insertTopLevelItem(0,item)
                repeat += 1
            Ui_Form.servers_oldList = servers_data
            self.pushButton_2.setEnabled(False)
            
            #TODO , make it show only when needed
            if int(self.checkBox_2.checkState()) == 2 and notifyUser and int(self.checkBox.checkState()) == 0:
                notify = pynotify.Notification("MG Launcher","Slots available",os.getcwd()+"/data/megaglest.bmp",)
                notify.show()
            elif int(self.checkBox_2.checkState()) == 2 and notifyUser and int(self.checkBox.checkState()) == 2:
                areYouSure = QtGui.QMessageBox.question(None, 'Joining game',"You are about to join a game, Do you want to proceed ?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                if areYouSure == QtGui.QMessageBox.Yes:
                    index = self.treeWidget.indexOfTopLevelItem(self.treeWidget.currentItem())
                    mg_dir = str(config['MGLauncher']['mg_dir'])
                    self.checkBox.setCheckState(False)
                    os.system(mg_dir+" --connect="+Ui_Form.servers_ip[index][0]+":"+Ui_Form.servers_ip[index][1])
             
        QtCore.QTimer.singleShot(10000, self.updateServers)
        
    def updateJoinGame(self):
        index = self.treeWidget.indexOfTopLevelItem(self.treeWidget.currentItem())
        if index > -1:
            self.pushButton_2.setEnabled(True)
        else:
            self.pushButton_2.setEnabled(False)
    
    def joinGame(self):
        index = int(self.treeWidget.indexOfTopLevelItem(self.treeWidget.currentItem()))
        mg_dir = str(config['MGLauncher']['mg_dir'])
        Ui_Form.servers_ip.reverse()
        os.system(mg_dir+" --connect="+Ui_Form.servers_ip[index][0]+":"+Ui_Form.servers_ip[index][1])
        
    def startMegaglest(self):
        mg_dir = str(config['MGLauncher']['mg_dir'])
        os.system(mg_dir)
    
    def center(self):
        frameGm = self.frameGeometry()
        screen = QtGui.QApplication.desktop().screenNumber(QtGui.QApplication.desktop().cursor().pos())
        centerPoint = QtGui.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())
        
        self.center()
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
