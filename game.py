#Created by Satyadev-Patel
#twitter:@emSatyadev


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from evaluate import Ui_OtherWindow

class Ui_MainWindow(object):
    p=sqlite3.connect('Project.db')
    curs=p.cursor()
    
    def f(self):
        self.Dialog = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
    def setupUi(self, MainWindow):
        self.count=0
        self.wkn=0
        self.batn=0
        self.bowln=0
        self.points=1000
        self.used=0
        self.alln=0
        self.teamcount=0
        self.batsmen=[" "," "," "," "," "," "," "," "," "," "]
        self.bowler=[" "," "," "," "," "," "," "," "]
        self.allround=[" "," "," "," "]
        self.wicketkeep=[" "," "," "]
        self.merged=""
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(822, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.batno = QtWidgets.QLabel(self.centralwidget)
        self.batno.setObjectName("batno")
        self.horizontalLayout.addWidget(self.batno)
        self.bats = QtWidgets.QLabel(self.centralwidget)
        self.bats.setObjectName("bats")
        self.horizontalLayout.addWidget(self.bats)
        spacerItem1 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.bowlno = QtWidgets.QLabel(self.centralwidget)
        self.bowlno.setObjectName("bowlno")
        self.horizontalLayout.addWidget(self.bowlno)
        self.bowls = QtWidgets.QLabel(self.centralwidget)
        self.bowls.setObjectName("bowls")
        self.horizontalLayout.addWidget(self.bowls)
        spacerItem2 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.alllno = QtWidgets.QLabel(self.centralwidget)
        self.alllno.setObjectName("alllno")
        self.horizontalLayout.addWidget(self.alllno)
        self.alls = QtWidgets.QLabel(self.centralwidget)
        self.alls.setObjectName("alls")
        self.horizontalLayout.addWidget(self.alls)
        spacerItem3 = QtWidgets.QSpacerItem(88, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.wkno = QtWidgets.QLabel(self.centralwidget)
        self.wkno.setObjectName("wkno")
        self.horizontalLayout.addWidget(self.wkno)
        self.wks = QtWidgets.QLabel(self.centralwidget)
        self.wks.setObjectName("wks")
        self.horizontalLayout.addWidget(self.wks)
        spacerItem4 = QtWidgets.QSpacerItem(118, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pointsa = QtWidgets.QLabel(self.centralwidget)
        self.pointsa.setText("Points Available")
        self.pointsa.setObjectName("pointsa")
        self.horizontalLayout_3.addWidget(self.pointsa)
        self.pointsavail = QtWidgets.QLabel(self.centralwidget)
        self.pointsavail.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">1000</span></p></body></html>")
        self.pointsavail.setObjectName("pointsavail")
        self.horizontalLayout_3.addWidget(self.pointsavail)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.pointu = QtWidgets.QLabel(self.centralwidget)
        self.pointu.setObjectName("pointu")
        self.horizontalLayout_4.addWidget(self.pointu)
        self.pointsused = QtWidgets.QLabel(self.centralwidget)
        self.pointsused.setObjectName("pointsused")
        self.horizontalLayout_4.addWidget(self.pointsused)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.batbtnr = QtWidgets.QRadioButton(self.centralwidget)
        self.batbtnr.setChecked(False)
        self.batbtnr.setObjectName("batbtnr")
        self.horizontalLayout_2.addWidget(self.batbtnr)
        self.bowlbtnr = QtWidgets.QRadioButton(self.centralwidget)
        self.bowlbtnr.setObjectName("bowlbtnr")
        self.horizontalLayout_2.addWidget(self.bowlbtnr)
        self.allbtnr = QtWidgets.QRadioButton(self.centralwidget)
        self.allbtnr.setObjectName("allbtnr")
        self.horizontalLayout_2.addWidget(self.allbtnr)
        self.wkbtnr = QtWidgets.QRadioButton(self.centralwidget)
        self.wkbtnr.setObjectName("wkbtnr")
        self.horizontalLayout_2.addWidget(self.wkbtnr)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem15)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem17)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem18)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.teamname = QtWidgets.QLabel(self.centralwidget)
        self.teamname.setObjectName("teamname")
        self.horizontalLayout_5.addWidget(self.teamname)
        self.team_name = QtWidgets.QLabel(self.centralwidget)
        self.team_name.setObjectName("team_name")
        self.horizontalLayout_5.addWidget(self.team_name)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.AvailablePlayers = QtWidgets.QListWidget(self.centralwidget)
        self.AvailablePlayers.setObjectName("AvailablePlayers")
        self.horizontalLayout_6.addWidget(self.AvailablePlayers)
                    
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem19)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../Users/SATYADEV/Desktop/download.jpg"))
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/SATYADEV/Desktop/download.jpg"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem20)
        self.SelectedPlayers = QtWidgets.QListWidget(self.centralwidget)
        self.SelectedPlayers.setObjectName("SelectedPlayers")
        self.horizontalLayout_6.addWidget(self.SelectedPlayers)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 31))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_team = QtWidgets.QAction(MainWindow)
        self.actionNew_team.setObjectName("actionNew_team")
        self.actionOpen_team = QtWidgets.QAction(MainWindow)
        self.actionOpen_team.setObjectName("actionOpen_team")
        self.actionSave_team = QtWidgets.QAction(MainWindow)
        self.actionSave_team.setObjectName("actionSave_team")
        self.actionEvaluate_team = QtWidgets.QAction(MainWindow)
        self.actionEvaluate_team.setObjectName("actionEvaluate_team")
        self.menuManage_Teams.addAction(self.actionNew_team)
        self.menuManage_Teams.addAction(self.actionOpen_team)
        self.menuManage_Teams.addAction(self.actionSave_team)
        self.menuManage_Teams.addAction(self.actionEvaluate_team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.menuManage_Teams.triggered[QtWidgets.QAction].connect(self.menuAction)
        self.batbtnr.toggled.connect(self.function)
        self.bowlbtnr.toggled.connect(self.function)
        self.allbtnr.toggled.connect(self.function)
        self.wkbtnr.toggled.connect(self.function)
        self.batbtnr.toggled.connect(self.chkname)
        self.bowlbtnr.toggled.connect(self.chkname)
        self.allbtnr.toggled.connect(self.chkname)
        self.wkbtnr.toggled.connect(self.chkname)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def chkname(self):
        if self.batbtnr.isChecked()==True or self.bowlbtnr.isChecked()==True or self.allbtnr.isChecked()==True or self.wkbtnr.isChecked()==True:
            if self.team_name.text()=="                           ":
                self.warn("Enter your team name\nGo to Menu bar>Manage Teams>New Team")
    def function(self):
            self.AvailablePlayers.clear()
            if self.batbtnr.isChecked()==True:
                for i in range(0,10-self.batn):
                    item = QtWidgets.QListWidgetItem()
                    self.AvailablePlayers.addItem(item)
            elif self.bowlbtnr.isChecked()==True:
                try:
                    for i in range(0,8-self.bowln):
                        item = QtWidgets.QListWidgetItem()
                        self.AvailablePlayers.addItem(item)
                except:
                    print("ERROR")
            elif self.allbtnr.isChecked()==True:
                for i in range(0,4-self.alln):
                    item = QtWidgets.QListWidgetItem()
                    self.AvailablePlayers.addItem(item)
            elif self.wkbtnr.isChecked()==True:
                for i in range(0,3-self.wkn):
                    item = QtWidgets.QListWidgetItem()
                    self.AvailablePlayers.addItem(item)
    def functions(self):
        self.SelectedPlayers.clear()
        for i in range(0,self.batn):
            item = QtWidgets.QListWidgetItem()
            self.SelectedPlayers.addItem(item)
        for i in range(0,self.bowln):
            item = QtWidgets.QListWidgetItem()
            self.SelectedPlayers.addItem(item)
        for i in range(0,self.alln):
            item = QtWidgets.QListWidgetItem()
            self.SelectedPlayers.addItem(item)
        for i in range(0,self.wkn):
            item = QtWidgets.QListWidgetItem()
            self.SelectedPlayers.addItem(item)
                

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Your Selections:</span></p></body></html>"))
        self.batno.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Batsmen</span></p></body></html>"))
        self.bats.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#0055ff;\">0</span></p></body></html>"))
        self.bowlno.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Bowlers</span></p></body></html>"))
        self.bowls.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">0</span></p></body></html>"))
        self.alllno.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">All-rounders</span></p></body></html>"))
        self.alls.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">0</span></p></body></html>"))
        self.wkno.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">WK</span></p></body></html>"))
        self.wks.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">0</span></p></body></html>"))
        self.pointu.setText(_translate("MainWindow", "Points used"))
        self.pointsused.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">0</span></p></body></html>"))
        self.batbtnr.setText(_translate("MainWindow", "BAT"))
        self.bowlbtnr.setText(_translate("MainWindow", "BWL"))
        self.allbtnr.setText(_translate("MainWindow", "ALL"))
        self.wkbtnr.setText(_translate("MainWindow", "WK"))
        self.teamname.setText(_translate("MainWindow", "Team Name:"))
        self.team_name.setText(_translate("MainWindow", "                           "))
        __sortingEnabled = self.AvailablePlayers.isSortingEnabled()
        self.AvailablePlayers.setSortingEnabled(False)
        self.AvailablePlayers.setSortingEnabled(__sortingEnabled)
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNew_team.setText(_translate("MainWindow", "New team"))
        self.actionOpen_team.setText(_translate("MainWindow", "Open team"))
        self.actionSave_team.setText(_translate("MainWindow", "Save"))
        self.actionEvaluate_team.setText(_translate("MainWindow", "Evaluate Score"))
        self.AvailablePlayers.itemDoubleClicked.connect(self.remlist1)
        self.SelectedPlayers.itemDoubleClicked.connect(self.remlist2)
        self.batbtnr.toggled.connect(self.function1)
        self.bowlbtnr.toggled.connect(self.function1)
        self.allbtnr.toggled.connect(self.function1)
        self.wkbtnr.toggled.connect(self.function1)
        self.p.commit()
    def function1(self):
        if self.batbtnr.isChecked()==True:
            i=0
            x="du plessis" in self.batsmen
            if x==False:
                self.curs.execute("SELECT * from stats WHERE players='du plessis';")
                m=self.curs.fetchone()[1]
                item = self.AvailablePlayers.item(i)
                item.setText("du plessis")
                i=i+1
            x="Shikhar Dhawan" in self.batsmen
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Shikhar Dhawan")
                i=i+1
            x="Rohit Sharma" in self.batsmen
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Rohit Sharma")
                i=i+1
            x="Virat Kohli" in self.batsmen
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Virat Kohli")
                i=i+1
            x="Shreyas Iyer" in self.batsmen
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Shreyas Iyer")
                i=i+1
            x="Steve Smith" in self.batsmen
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Steve Smith")
                i=i+1
            x="Manish Pandey" in self.batsmen
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Manish Pandey")
                i=i+1
            x="David Warner" in self.batsmen
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("David Warner")
                i=i+1
            x="Aaron Finch" in self.batsmen
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Aaron Finch")
                i=i+1
            x="AB de Villiers" in self.batsmen
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("AB de Villiers")
        elif self.bowlbtnr.isChecked()==True:
            i=0
            x="Mitchell Starc" in self.bowler
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Mitchell Starc")
                i=i+1
            x="Jasprit Bumrah" in self.bowler
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Jasprit Bumrah")
                i=i+1
            x="Umesh Yadav" in self.bowler
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Umesh Yadav")
                i=i+1
            x="Pat Cummins" in self.bowler
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Pat Cummins")
                i=i+1
            x="Bhuvneshwar Kumar" in self.bowler
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Bhuvneshwar Kumar")
                i=i+1
            x="Imran Tahir" in self.bowler
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Imran Tahir")
                i=i+1
            x="Dale Steyn" in self.bowler
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Dale Steyn")
                i=i+1
            x="Mohammad Shami" in self.bowler
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Mohammad Shami")
        elif self.allbtnr.isChecked()==True:
            i=0
            x="Suresh Raina" in self.allround
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Suresh Raina")
                i=i+1
            x="Ravindra Jadeja" in self.allround
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Ravindra Jadeja")
                i=i+1
            x="Hardik Pandya" in self.allround
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Hardik Pandya")
                i=i+1
            x="Glenn Maxwell" in self.allround
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Glenn Maxwell")
        elif self.wkbtnr.isChecked()==True:
            i=0
            x="MS Dhoni" in self.wicketkeep
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("MS Dhoni")
                i=i+1
            x="Alex Carey" in self.wicketkeep
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("Alex Carey")
                i=i+1
            x="KL Rahul" in self.wicketkeep
            if x==False:
                item = self.AvailablePlayers.item(i)
                item.setText("KL Rahul")
                i=i+1
    def functions1(self):
        i=0
        x="du plessis" in self.batsmen
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("du plessis")
            i=i+1
        x="Shikhar Dhawan" in self.batsmen
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Shikhar Dhawan")
            i=i+1
        x="Rohit Sharma" in self.batsmen
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Rohit Sharma")
            i=i+1
        x="Virat Kohli" in self.batsmen
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Virat Kohli")
            i=i+1
        x="Shreyas Iyer" in self.batsmen
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Shreyas Iyer")
            i=i+1
        x="Steve Smith" in self.batsmen
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Steve Smith")
            i=i+1
        x="Manish Pandey" in self.batsmen
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Manish Pandey")
            i=i+1
        x="David Warner" in self.batsmen
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("David Warner")
            i=i+1
        x="Aaron Finch" in self.batsmen
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Aaron Finch")
            i=i+1
        x="AB de Villiers" in self.batsmen
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("AB de Villiers")
            i=i+1
        x="Mitchell Starc" in self.bowler
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Mitchell Starc")
            i=i+1
        x="Jasprit Bumrah" in self.bowler
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Jasprit Bumrah")
            i=i+1
        x="Umesh Yadav" in self.bowler
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Umesh Yadav")
            i=i+1
        x="Pat Cummins" in self.bowler
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Pat Cummins")
            i=i+1
        x="Bhuvneshwar Kumar" in self.bowler
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Bhuvneshwar Kumar")
            i=i+1
        x="Imran Tahir" in self.bowler
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Imran Tahir")
            i=i+1
        x="Dale Steyn" in self.bowler
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Dale Steyn")
            i=i+1
        x="Mohammad Shami" in self.bowler
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Mohammad Shami")
            i=i+1
        x="Suresh Raina" in self.allround
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Suresh Raina")
            i=i+1
        x="Ravindra Jadeja" in self.allround
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Ravindra Jadeja")
            i=i+1
        x="Hardik Pandya" in self.allround
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Hardik Pandya")
            i=i+1
        x="Glenn Maxwell" in self.allround
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Glenn Maxwell")
            i=i+1
        x="MS Dhoni" in self.wicketkeep
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("MS Dhoni")
            i=i+1
        x="Alex Carey" in self.wicketkeep
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("Alex Carey")
            i=i+1
        x="KL Rahul" in self.wicketkeep
        if x==True:
            item = self.SelectedPlayers.item(i)
            item.setText("KL Rahul")
            i=i+1
    def menuAction(self,action):
        txt=action.text();
        if txt=="New team":
            self.bats.setText(str(0))
            self.bowls.setText(str(0))
            self.alls.setText(str(0))
            self.wks.setText(str(0))
            self.pointsavail.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">"+str(1000)+"</span></p></body></html>")
            self.pointsused.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">"+str(0)+"</span></p></body></html>")
            self.SelectedPlayers.clear()
            self.team_name.clear()
            self.count=0
            self.wkn=0
            self.batn=0
            self.bowln=0
            self.alln=0
            self.points=1000
            self.used=0
            self.batsmen=[" "," "," "," "," "," "," "," "," "," "]
            self.bowler=[" "," "," "," "," "," "," "," "]
            self.allround=[" "," "," "," "]
            self.wicketkeep=[" "," "," "]
            self.batbtnr.setChecked(True)
            self.function()
            self.function1()
            x,ok=QtWidgets.QInputDialog.getText(MainWindow, "Team Name", "Enter name of team:")
            self.team_name.setText(x)
        if txt=="Save":
            if self.team_name.text()=="                           ":
                self.warn("NO")
            else:
                self.count=self.batn+self.bowln+self.wkn+self.alln
                self.merged=""
                if self.count==11 and self.wkn==1 and self.bowln<=5 and self.batn<=7:
                    for i in range(0,10):
                        if self.batsmen[i]!=" ":
                            self.merged=self.merged+self.batsmen[i]+'-'
                    for i in range(0,8):
                        if self.bowler[i]!=" ":
                            self.merged=self.merged+self.bowler[i]+'-'
                    for i in range(0,4):
                        if self.allround[i]!=" ":
                            self.merged=self.merged+self.allround[i]+'-'
                    for i in range(0,3):
                        if self.wicketkeep[i]!=" ":
                            self.merged=self.merged+self.wicketkeep[i]+'-'
                    x=self.team_name.text()
                    self.curs.execute("SELECT name FROM teams WHERE name='"+x+"';")
                    y=self.curs.fetchone()
                    if y==None:
                        self.team_name.setText(x)
                        self.curs.execute("INSERT into teams (name,players)VALUES('"+x+"','"+self.merged+"');")
                        self.warn2("Team Saved")
                        self.p.commit()
                    else:
                        self.team_name.setText(x)
                        self.curs.execute("UPDATE teams SET players='"+self.merged+"' WHERE name='"+x+"';")
                        self.warn("Team Saved")
                        self.p.commit()
                elif self.count<11:
                    self.warn("Select Atleast 11 players")
                elif self.count>11:
                    self.warn("Select Atmost 11 playerss")
                elif self.wkn==0:
                    self.warn("Select 1 wicket-keeper in your team")
                elif self.wkn>1:
                    self.warn("You can select 1 wicket-keeper only")
                elif self.batn>7:
                    self.warn("You can select atmost 7 batsman not more than that")
                elif self.bowln>5:
                    self.warn("You can select atmost 5 bowlers")
                
        if txt=="Open team":
            self.bats.setText(str(0))
            self.bowls.setText(str(0))
            self.alls.setText(str(0))
            self.wks.setText(str(0))
            self.pointsavail.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">"+str(1000)+"</span></p></body></html>")
            self.pointsused.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">"+str(0)+"</span></p></body></html>")
            self.SelectedPlayers.clear()
            self.team_name.clear()
            self.count=0
            self.wkn=0
            self.batn=0
            self.bowln=0
            self.alln=0
            self.points=1000
            self.used=0
            self.batsmen=[" "," "," "," "," "," "," "," "," "," "]
            self.bowler=[" "," "," "," "," "," "," "," "]
            self.allround=[" "," "," "," "]
            self.wicketkeep=[" "," "," "]
            self.function()
            self.function1()
            self.curs.execute("SELECT name FROM teams;")
            k=self.curs.fetchall()
            j=0
            self.teamcount=len(k)
            team=[None]*self.teamcount
            for i in k:
                team[j]=i[0]
                j=j+1
            x, ok=QtWidgets.QInputDialog.getItem(MainWindow,"Dream","Choose A Team",team,0,False)
            self.team_name.setText(x)
            self.curs.execute("SELECT players FROM teams WHERE name='"+x+"';")
            y=self.curs.fetchone()[0]
            playe=y.split("-")
            playe.pop(len(playe)-1)
            for i in playe:
                self.curs.execute("SELECT * FROM stats WHERE players='"+i+"';")
                x=self.curs.fetchone()
                if x[6]=='BAT':
                    self.batsmen[self.batn]=i
                    self.points=self.points-x[1]
                    self.used=self.used+x[1]
                    self.batn=self.batn+1
                if x[6]=='BWL':
                    self.bowler[self.bowln]=i
                    self.points=self.points-x[1]
                    self.used=self.used+x[1]
                    self.bowln=self.bowln+1
                if x[6]=='ALL':
                    self.allround[self.alln]=i
                    self.points=self.points-x[1]
                    self.used=self.used+x[1]
                    self.alln=self.alln+1
                if x[6]=='WK':
                    self.wicketkeep[self.wkn]=i
                    self.points=self.points-x[1]
                    self.used=self.used+x[1]
                    self.wkn=self.wkn+1
            
            self.bats.setText(str(self.batn))
            self.bowls.setText(str(self.bowln))
            self.alls.setText(str(self.alln))
            self.wks.setText(str(self.wkn))
            self.pointsavail.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">"+str(self.points)+"</span></p></body></html>")
            self.pointsused.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">"+str(self.used)+"</span></p></body></html>")
            self.function()
            self.function1()
            self.functions()
            self.functions1()
            self.batbtnr.setChecked(True)
            
        if txt=="Evaluate Score":
            self.f()

    def warn(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("ERROR")
        Dialog.exec()
    def warn2(self,msg):
        Dialog=QtWidgets.QMessageBox()
        Dialog.setText(msg)
        Dialog.setWindowTitle("SAVED")
        Dialog.exec()
            
    def remlist1(self,item):
        self.AvailablePlayers.takeItem(self.AvailablePlayers.row(item))
        m=item.text()
        self.curs.execute("SELECT * from stats WHERE players='"+m+"';")
        m=self.curs.fetchone()[1]
        if self.used+m<=1000:
            self.used=self.used+m
            self.points=self.points-m
            self.pointsavail.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">"+str(self.points)+"</span></p></body></html>")
            self.pointsused.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">"+str(self.used)+"</span></p></body></html>")
            s="SELECT * from stats WHERE players='"+item.text()+"';"
            catg=self.curs.execute(s).fetchone()[6]
            if catg=='BAT':
                x=item.text() in self.batsmen
                if x==True:
                    print("You can't do this")
                else:
                    self.SelectedPlayers.addItem(item.text())
                    for i in range(0,10):
                            if self.batsmen[i]==' ':
                                self.batsmen[i]=item.text()
                                break
                self.count=self.count+1
                self.batn=self.batn+1
                self.bats.setText(str(self.batn))
            elif catg=='BWL':
                x=item.text() in self.bowler
                if x==True:
                    print("You can't do this")
                else:
                    self.SelectedPlayers.addItem(item.text())
                    for i in range(0,8):
                        if self.bowler[i]==' ':
                            self.bowler[i]=item.text()
                            break
                self.count=self.count+1
                self.bowln=self.bowln+1
                self.bowls.setText(str(self.bowln))
            if catg=='ALL':
                try:
                    x=item.text() in self.allround
                    if x==True:
                        print("You can't do this")
                    else:
                        self.SelectedPlayers.addItem(item.text())
                        for i in range(0,4):
                            if self.allround[i]==' ':
                                self.allround[i]=item.text()
                                break
                    self.count=self.count+1
                    self.alln=self.alln+1
                    self.alls.setText(str(self.alln))
                except:
                    print("ERROR 1")
            if catg=='WK':
                x=item.text() in self.wicketkeep
                if x==True:
                    print("You can't do this")
                else:
                    self.SelectedPlayers.addItem(item.text())
                    for i in range(0,3):
                        if self.wicketkeep[i]==' ':
                            self.wicketkeep[i]=item.text()
                            break
                self.count=self.count+1
                self.wkn=self.wkn+1
                self.wks.setText(str(self.wkn))
        else:
            self.warn("You have exceeded the points limit")
            self.AvailablePlayers.addItem(item.text())
                                   
    def remlist2(self,item):
        self.SelectedPlayers.takeItem(self.SelectedPlayers.row(item))
        m=item.text()
        self.curs.execute("SELECT * from stats WHERE players='"+m+"';")
        m=self.curs.fetchone()[1]
        self.points=self.points+m
        self.used=self.used-m
        self.pointsavail.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">"+str(self.points)+"</span></p></body></html>")
        self.pointsused.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">"+str(self.used)+"</span></p></body></html>")
        s="SELECT * from stats WHERE players='"+item.text()+"';"
        catg=self.curs.execute(s).fetchone()[6]
        if catg=='BAT':
            for i in range(0,10):
                if self.batsmen[i]==item.text():
                    self.batsmen[i]=" "
                    break
            self.count=self.count-1
            x=self.team_name.text()
            self.batn=self.batn-1
            self.bats.setText(str(self.batn))
            self.function()
            self.function1()
        if catg=='BWL':
            for i in range(0,8):
                if self.bowler[i]==item.text():
                    self.bowler[i]=" "
                    break
            self.count=self.count-1
            x=self.team_name.text()
            self.bowln=self.bowln-1
            self.bowls.setText(str(self.bowln))
            self.function()
            self.function1()
        if catg=='ALL':
            try:
                for i in range(0,4):
                    if self.allround[i]==item.text():
                        self.allround[i]=" "
                        break
                self.count=self.count-1
                x=self.team_name.text()
                self.alln=self.alln-1
                self.alls.setText(str(self.alln))
                self.function()
                self.function1()
            except:
                print("ERROR 2")
        if catg=='WK':
            for i in range(0,3):
                if self.wicketkeep[i]==item.text():
                    self.wicketkeep[i]=" "
                    break
            self.count=self.count-1
            x=self.team_name.text()
            self.wkn=self.wkn-1
            self.wks.setText(str(self.wkn))
            self.function()
            self.function1()
        
print("du plessis 90")
print("Virat Kohli 110")
print("Rohit Sharma 110")
print("Manish Pandey 65")
print("AB de Villiers 115")
print("Steve Smith 90")
print("Shreyas Iyer 70")
print("Aaron Finch 110")
print("David Warner 100")
print("Shikhar Dhawan 95")
print("Ravindra Jadeja 90")
print("Hardik Pandya 105")
print("Suresh Raina 95")
print("Glenn Maxwell 90")
print("Bhuvneshwar Kumar 90")
print("Mohammad Shami 70")
print("Jasprit Bumrah 110")
print("Mitchell Starc 110")
print("Pat Cummins 95")
print("Imran Tahir 80")
print("Dale Steyn 80")
print("Umesh Yadav 75")
print("KL Rahul 90")
print("MS Dhoni 105")
print("Alex Carey 65")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
