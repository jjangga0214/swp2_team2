import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit,QGridLayout)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.combobox = QComboBox()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()


    def initUI(self):

        grid = QGridLayout()
        grid.setSpacing(10)

        
        name = QLabel("Name:", self)
        age = QLabel("Age:", self)
        score = QLabel("Score:", self)
        amount = QLabel("Amount:", self)
        key = QLabel("Key:", self)
        result = QLabel("Result:", self)

        self.nameEdit = QLineEdit()
        self.ageEdit = QLineEdit()
        self.scoreEdit = QLineEdit()
        self.amountEdit = QLineEdit()
        self.resultEdit = QTextEdit()

        self.keybox = QComboBox()
        self.keybox.addItem("Name")
        self.keybox.addItem("Age")
        self.keybox.addItem("Score")

        addbutton = QPushButton("Add", self)
        grid.addWidget(addbutton, 3, 1)
        addbutton.clicked.connect(self.addbuttonClicked)

        delbutton = QPushButton("Del", self)
        grid.addWidget(delbutton, 3, 2)
        delbutton.clicked.connect(self.delbuttonClicked)

        findbutton = QPushButton("Find", self)
        grid.addWidget(findbutton, 3, 3)
        findbutton.clicked.connect(self.findbuttonClicked)

        incbutton = QPushButton("Inc", self)
        grid.addWidget(incbutton, 3, 4)
        incbutton.clicked.connect(self.incbuttonClicked)

        showbutton = QPushButton("Show", self)
        grid.addWidget(showbutton, 3, 5)
        showbutton.clicked.connect(self.showbuttonClicked)

        grid.addWidget(name,1,0)
        grid.addWidget(self.nameEdit,1,1)
        grid.addWidget(age,1,2)
        grid.addWidget(self.ageEdit,1,3)
        grid.addWidget(score,1,4)
        grid.addWidget(self.scoreEdit,1,5)
        grid.addWidget(amount,2,2)
        grid.addWidget(self.amountEdit,2,3)
        grid.addWidget(key,2,4)
        grid.addWidget(self.keybox,2,5)
        grid.addWidget(result,4,0)
        grid.addWidget(self.resultEdit,5,0,5,6)

        self.setLayout(grid)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

    def addbuttonClicked(self):
        record = {'Name': self.nameEdit.text(), 'Age': self.ageEdit.text(), 'Score': self.scoreEdit.text()}
        self.scoredb += [record]
        self.showScoreDB()


    def delbuttonClicked(self):
        new_scdb = sorted(self.scoredb, key=lambda x: x["Name"], reverse=True)
        for p in new_scdb:
            if p['Name'] == self.nameEdit.text():
                self.scoredb.remove(p)
        self.showScoreDB()

    def findbuttonClicked(self):
        result = ""
        for p in sorted(self.scoredb, key=lambda person: person["Name"]):
            for attr in sorted(p):
                if p['Name'] == self.nameEdit.text():
                    result += attr + "=" + str(p[attr]) + " "
            result += "\n"
        self.resultEdit.setText(result)

    def incbuttonClicked(self):
        for p in sorted(self.scoredb, key=lambda person: person["Name"]):
            for attr in sorted(p):
                if p["Name"] == self.nameEdit.text():
                    p["Score"] += int(self.amountEdit.text())
                    break
        self.showScoreDB()



    def showbuttonClicked(self):
        self.showScoreDB(self.keybox.currentText())

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)

        fH.close()

    def showScoreDB(self,keyname="Name"):
        result = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                result += attr + "=" + str(p[attr]) + " "
            result += "\n"
        self.resultEdit.setText(result)

        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = ScoreDB()
    ex.show()
    sys.exit(app.exec_())






