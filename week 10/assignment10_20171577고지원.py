from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):
    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

    def __init__(self, text, callback):
        super().__init__()

        self.setSizePolicy(QSizePolicy.Expanding,
                       QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)


class Calculator(QWidget):
    #버튼 클릭 함수
    def buttonClicked(self):
        button = self.sender()

        key = button.text()
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.setText('')
        else:
            self.display.setText(self.display.text() + key)

    #숫자 표시 창
    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]
        # for i in range(0,10):
        #     self.digitButton[i] = Button('',self.buttonClicked)
        self.digitButton[0] = Button('0',self.buttonClicked)
        self.digitButton[1] = Button('1',self.buttonClicked)
        self.digitButton[2] = Button('2',self.buttonClicked)
        self.digitButton[3] = Button('3',self.buttonClicked)
        self.digitButton[4] = Button('4',self.buttonClicked)
        self.digitButton[5] = Button('5',self.buttonClicked)
        self.digitButton[6] = Button('6',self.buttonClicked)
        self.digitButton[7] = Button('7',self.buttonClicked)
        self.digitButton[8] = Button('8',self.buttonClicked)
        self.digitButton[9] = Button('9',self.buttonClicked)

        # . and = Buttons
        self.decButton = Button('.',self.buttonClicked)
        self.eqButton = Button('=',self.buttonClicked)

        # Operator Buttons
        self.mulButton = Button('*',self.buttonClicked)
        self.divButton = Button('/',self.buttonClicked)
        self.addButton = Button('+',self.buttonClicked)
        self.subButton = Button('-',self.buttonClicked)

        # Parentheses Buttons
        self.lparButton = Button('(',self.buttonClicked)
        self.rparButton = Button(')',self.buttonClicked)

        # Clear Button
        self.clearButton = Button('C',self.buttonClicked)

        # Layout

        #숫자 표시 창
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        #숫자 키패드
        numLayout = QGridLayout()
        for i in range(1,10):
            numLayout.addWidget(self.digitButton[i], (9-i) // 3, (i-1) % 3)
        numLayout.addWidget(self.digitButton[0], 3, 0)

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        #메인레이아웃에 1행0열에 자리함
        mainLayout.addLayout(numLayout, 1, 0)

        #연산자 키패드
        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        #메인레이아웃에 1행1열에 자리함
        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")




if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
