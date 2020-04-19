#Created by Satyadev-Patel
#twitter:@emSatyadev

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_OtherWindow(object):
    p=sqlite3.connect('Project.db')
    curs=p.cursor()
    def setupUi(self, OtherWindow):
        self.playe=[" "," "," "," "," "," "," "," "," "," "," "," "]
        self.runs=0
        self.balls=0
        self.fours=0
        self.sixes=0
        self.bowled=0
        self.runsgiven=0
        self.maiden=0
        self.wkts=0
        self.catch=0
        self.stump=0
        self.ro=0
        self.mainpoints=0
        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(572, 596)
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.curs.execute("SELECT name FROM teams;")
        s=self.curs.fetchall()
        for i in s:
            self.comboBox_2.addItem(i[0])
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.points = QtWidgets.QLabel(self.centralwidget)
        self.points.setObjectName("points")
        self.horizontalLayout_4.addWidget(self.points)
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setObjectName("score")
        self.horizontalLayout_4.addWidget(self.score)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.teamPlayers = QtWidgets.QListWidget(self.centralwidget)
        self.teamPlayers.setObjectName("teamPlayers")
        self.horizontalLayout_5.addWidget(self.teamPlayers)
        x=self.comboBox_2.currentText()
        self.curs.execute("SELECT players FROM teams WHERE name='"+x+"';")
        y=self.curs.fetchone()[0]
        self.playe=y.split("-")
        self.playe.pop(len(self.playe)-1)
        for i in self.playe:
            item = QtWidgets.QListWidgetItem()
            self.teamPlayers.addItem(item)
            item.setText(i)
        self.playersScore = QtWidgets.QListWidget(self.centralwidget)
        self.playersScore.setObjectName("playersScore")
        self.horizontalLayout_5.addWidget(self.playersScore)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setObjectName("calculate")
        self.horizontalLayout_6.addWidget(self.calculate)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 572, 31))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)
        self.comboBox_2.currentTextChanged.connect(self.playerlist)
        self.comboBox.currentTextChanged.connect(self.clearr)
        self.calculate.clicked.connect(self.scoreBtn)

    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "OtherWindow"))
        self.label.setText(_translate("OtherWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#5555ff;\">It\'s time to evaluate your team\'s score</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("OtherWindow", "match1"))
        self.comboBox.setItemText(1, _translate("OtherWindow", "match2"))
        self.comboBox.setItemText(2, _translate("OtherWindow", "match3"))
        self.comboBox.setItemText(3, _translate("OtherWindow", "match5"))
        self.label_3.setText(_translate("OtherWindow", "Players"))
        self.points.setText(_translate("OtherWindow", "Points"))
        self.score.setText(_translate("OtherWindow", "<html><head/><body><p><span style=\" font-weight:600; color:#5555ff;\">0</span></p></body></html>"))
        self.calculate.setText(_translate("OtherWindow", "Calculate Score"))
    def clearr(self,item):
        self.playersScore.clear()
        self.score.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">0</span></p></body></html>")
    def playerlist(self,item):
        self.teamPlayers.clear()
        self.playersScore.clear()
        self.score.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">0</span></p></body></html>")
        self.curs.execute("SELECT players FROM teams WHERE name='"+item+"';")
        y=self.curs.fetchone()[0]
        self.playe=y.split("-")
        self.playe.pop(len(self.playe)-1)
        for i in self.playe:
            item = QtWidgets.QListWidgetItem()
            self.teamPlayers.addItem(item)
            item.setText(i)
    def scoreBtn(self):
        self.mainpoints=0
        self.playersScore.clear()
        for i in self.playe:
            self.scoreCalc(i)
        self.score.setText("<html><head/><body><p><span style=\" font-weight:600; color:#5500ff;\">"+str(self.mainpoints)+"</span></p></body></html>")
    def scoreCalc(self,name=" "):
        x=self.comboBox.currentText()
        self.curs.execute("SELECT ctg FROM stats WHERE players='"+name+"';")
        y=self.curs.fetchone()
        #print(y)
        if y[0]=='BAT':
            self.curs.execute("SELECT * FROM "+x+" WHERE player='"+name+"';")
            m=self.curs.fetchone()
            #print(m[0])
            self.runs=m[1]
            self.balls=m[2]
            self.fours=m[3]
            self.sixes=m[4]
            self.catch=m[9]
            self.stump=m[10]
            self.ro=m[11]
            points=0
            points=points+self.runs/2
            if self.runs>=50:
                points=points+5
            if self.runs>=100:
                points=points+10
            strikerate=(self.runs/self.balls)*100
            if strikerate>=80 and strikerate<=100:
                points=points+2
            if strikerate>100:
                points=points+4
            points=points+self.fours    
            points=points+2*self.sixes
            points=points+10*(self.catch+self.stump+self.ro)
            self.mainpoints=self.mainpoints+points
            item = QtWidgets.QListWidgetItem()
            self.playersScore.addItem(item)
            item.setText(str(points))
            #print(points)
        if y[0]=='BWL':
            self.curs.execute("SELECT * FROM "+x+" WHERE player='"+name+"';")
            m=self.curs.fetchone()
            #print(m[0])
            self.bowled=m[5]
            self.maiden=m[6]
            self.runsgiven=m[7]
            self.wkts=m[8]
            self.catch=m[9]
            self.stump=m[10]
            self.ro=m[11]
            points=0
            points=points+12.5*self.wkts
            if self.wkts>=3:
                points=points+5
            if self.wkts>=5:
                points=points+10
            ecrate=self.runsgiven/(self.bowled/6)
            if ecrate>3.5 and ecrate<=4.5:
                points=points+4
            if ecrate>2 and ecrate<=3.5:
                points=points+7
            if ecrate<=2:
                points=points+10
            points=points+10*(self.catch+self.stump+self.ro)
            item = QtWidgets.QListWidgetItem()
            self.playersScore.addItem(item)
            item.setText(str(points))
            #print(points)
            self.mainpoints=self.mainpoints+points
        if y[0]=='ALL':
            self.curs.execute("SELECT * FROM "+x+" WHERE player='"+name+"';")
            m=self.curs.fetchone()
           # print(m[0])
            self.runs=m[1]
            self.balls=m[2]
            self.fours=m[3]
            self.sixes=m[4]
            self.catch=m[9]
            self.stump=m[10]
            self.ro=m[11]
            self.bowled=m[5]
            self.maiden=m[6]
            self.runsgiven=m[7]
            self.wkts=m[8]
            points=0
            points=points+self.runs/2
            if self.runs>=50:
                points=points+5
            if self.runs>=100:
                points=points+10
            strikerate=(self.runs/self.balls)*100
            if strikerate>=80 and strikerate<=100:
                points=points+2
            if strikerate>100:
                points=points+4
            points=points+self.fours    
            points=points+2*self.sixes
            points=points+10*(self.catch+self.stump+self.ro)
            points=points+12.5*self.wkts
            if self.wkts>=3:
                points=points+5
            if self.wkts>=5:
                points=points+10
            ecrate=self.runsgiven/(self.bowled/6)
            if ecrate>3.5 and ecrate<=4.5:
                points=points+4
            if ecrate>2 and ecrate<=3.5:
                points=points+7
            if ecrate<=2:
                points=points+10
            #print(points)
            item = QtWidgets.QListWidgetItem()
            self.playersScore.addItem(item)
            item.setText(str(points))
            self.mainpoints=self.mainpoints+points
        if y[0]=='WK':
            self.curs.execute("SELECT * FROM "+x+" WHERE player='"+name+"';")
            m=self.curs.fetchone()
            #print(m[0])
            self.runs=m[1]
            self.balls=m[2]
            self.fours=m[3]
            self.sixes=m[4]
            self.catch=m[9]
            self.stump=m[10]
            self.ro=m[11]
            points=0
            points=points+self.runs/2
            if self.runs>=50:
                points=points+5
            if self.runs>=100:
                points=points+10
            strikerate=(self.runs/self.balls)*100
            if strikerate>=80 and strikerate<=100:
                points=points+2
            if strikerate>100:
                points=points+4
            points=points+self.fours    
            points=points+2*self.sixes
            points=points+10*(self.catch+self.stump+self.ro)
            #print(points)
            item = QtWidgets.QListWidgetItem()
            self.playersScore.addItem(item)
            item.setText(str(points))
            self.mainpoints=self.mainpoints+points
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
