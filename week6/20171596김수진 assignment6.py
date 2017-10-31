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

    def initUI(self):

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        name = QLabel('Name :', self)
        age = QLabel('Age :', self)
        score = QLabel('Score :', self)
        amount = QLabel('Amount :', self)
        key = QLabel('Key :', self)
        result = QLabel('Result : ',self)

        self.nameEdit = QLineEdit(self)
        self.ageEdit = QLineEdit(self)
        self.scoreEdit = QLineEdit(self)
        self.amountEdit = QLineEdit(self)

        self.keycombo = QComboBox(self)
        self.keycombo.addItem("Name")
        self.keycombo.addItem("Age")
        self.keycombo.addItem("Score")

        addButton = QPushButton('Add')
        delButton = QPushButton('Del')
        findButton = QPushButton('Find')
        incButton = QPushButton('Inc')
        showButton = QPushButton('Show')

        addButton.clicked.connect(self.doScoreDB)
        delButton.clicked.connect(self.doScoreDB)
        findButton.clicked.connect(self.doScoreDB)
        incButton.clicked.connect(self.doScoreDB)
        showButton.clicked.connect(self.showScoreDB)

        self.resultDisplay = QTextEdit(self)

        # first line layout
        hbox = QHBoxLayout()
        hbox.addWidget(name)
        hbox.addWidget(self.nameEdit)
        hbox.addWidget(age)
        hbox.addWidget(self.ageEdit)
        hbox.addWidget(score)
        hbox.addWidget(self.scoreEdit)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        # second line layout
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(amount)
        hbox1.addWidget(self.amountEdit)
        hbox1.addWidget(key)
        hbox1.addWidget(self.keycombo)

        vbox.addLayout(hbox1)

        # third line layout
        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(addButton)
        hbox2.addWidget(delButton)
        hbox2.addWidget(findButton)
        hbox2.addWidget(incButton)
        hbox2.addWidget(showButton)

        vbox.addLayout(hbox2)

        # forth line layout
        hbox3 = QHBoxLayout()
        hbox3.addWidget(result)

        vbox.addLayout(hbox3)

        # fifth line layout
        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.resultDisplay)

        vbox.addLayout(hbox4)

        self.setLayout(vbox)
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

    def doScoreDB(self):
        sender = self.sender()
        # add
        if sender.text() == 'Add':
            record = {'Name': self.nameEdit.text(), 'Age': int(self.ageEdit.text()), 'Score': int(self.scoreEdit.text())}
            self.scoredb += [record]

        # del
        elif sender.text() == 'Del':
            new_scoredb = []
            for p in self.scoredb:
                if self.nameEdit.text() != p['Name']:
                    new_scoredb.append(p)
            self.scoredb = new_scoredb

        # find
        elif sender.text() == "Find":
            st = ''
            for p in self.scoredb:
                if self.nameEdit.text() == p['Name']:
                    for attr in sorted(p):
                        st += attr + "=" + str(p[attr]) + "   "
                    st += '\n'
                    self.resultDisplay.setText(st)

        # inc
        elif sender.text() == "Inc":
            for p in self.scoredb:
                if self.nameEdit.text() == p['Name']:
                    p['Score'] += int(self.amountEdit.text())

    # show
    def showScoreDB(self):
        show_str = ''
        for p in sorted(self.scoredb, key=lambda person: person[self.keycombo.currentText()]):
            for attr in sorted(p):
                show_str += attr + '=' + str(p[attr]) + '   '
            show_str += '\n'
            self.resultDisplay.setText(show_str)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





