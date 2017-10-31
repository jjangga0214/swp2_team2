import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
    #레이아웃 만들기
    def initUI(self):
        name = QLabel('Name', self)
        self.NB = QLineEdit()
        age = QLabel('Age', self)
        self.AB = QLineEdit()
        score = QLabel('Score', self)
        self.SB = QLineEdit()

        amount = QLabel('Amount', self)
        self.AmB = QLineEdit()
        key = QLabel('key', self)
        self.KB = QComboBox()
        self.KB.addItems(['Name', 'Age', 'Score'])

        result = QLabel('Result', self)
        self.RS = QTextEdit()

        addButton = QPushButton('add')
        delButton = QPushButton('del')
        incButton = QPushButton('inc')
        findButton = QPushButton('find')
        showButton = QPushButton('show')

        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(name)
        hbox_1.addWidget(self.NB)
        hbox_1.addWidget(age)
        hbox_1.addWidget(self.AB)
        hbox_1.addWidget(score)
        hbox_1.addWidget(self.SB)

        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(5)
        hbox_2.addWidget(amount)
        hbox_2.addWidget(self.Amb)
        hbox_2.addWidget(key)
        hbox_2.addWidget(self.KB)

        hbox_3 = QHBoxLayout()
        hbox_3.addStretch(1)
        hbox_3.addWidget(addButton)
        hbox_3.addWidget(delButton)
        hbox_3.addWidget(incButton)
        hbox_3.addWidget(findButton)
        hbox_3.addWidget(showButton)

        hbox_4 = QHBoxLayout()
        hbox_4.addWidget(result)

        hbox_5 = QHBoxLayout()
        hbox_5.addWidget(self.RS)


        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
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

    def showScoreDB(self, keyname):
        for p in sorted (self.scdb, key=lambda person:person[keyname]):
            for attr in sorted(p):
                print(attr + "=" + str(p[attr]), end = ' ')
            print()

    def add(slef, x, y, z):
        record = {'Name': x, 'Age': y, 'Score': z}
        self.scdb += [record]

    def _del(self):
        list_p = []
        for p in scdb:
            if p['Name'] == self.NB.text():
                list_p.append(p)
        for p in list_p:
            scdb.remove(p)

    def find(self):
        for li in scdb:
            if li['Name'] == self.NB.text():
                for list_ in sorted(li):
                    print(list_ + "=" + str(li[list_]), end=' ')
                print()

    def inc(self):
        for list in scdb:
            if list['Name'] == self.NB.text():



if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





