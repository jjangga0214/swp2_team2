from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
from keyped import numPadList, operatorList, constantList, functionList
from calcFunctions import factorial, decToBin, binToDec


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
    error = False

    def buttonClicked(self):
        if self.error:
            self.display.clear()
            self.error = False

        button = self.sender()
        key = button.text()

        ConstantGroups = {'pi': '3.141592', '빛의 이동 속도 (m/s)': '3E+8',
                     '소리의 이동 속도 (m/s)': '340', '태양과의 평균 거리 (km)': '1.5E+8'}

        if key == '=':
            try:
                result = str(eval(self.display.text()))
            except:
                result = 'Error!'
                self.error = True
            self.display.setText(result)

        elif key == 'C':
            self.display.clear()

        elif key in constantList:
            self.display.setText(self.display.text() + ConstantGroups[key])

        elif key == functionList[0]:
            n = self.display.text()
            value = factorial(n)
            self.display.setText(str(value))

        elif key == functionList[1]:
            n = self.display.text()
            value = decToBin(n)
            self.display.setText(str(value))

        elif key == functionList[2]:
            n = self.display.text()
            value = binToDec(n)
            self.display.setText(str(value))

        else:
            self.display.setText(self.display.text() + key)

    # 숫자 표시 창
    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        mainLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        # 메인레이아웃에 1행0열에 자리함
        mainLayout.addLayout(numLayout, 1, 0)
        # 메인레이아웃에 1행1열에 자리함
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.buttonGroups = {'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
                             'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
                             'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
                             'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1}
                             }

        for label in self.buttonGroups.keys():
            r = 0
            c = 0
            buttonPad = self.buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0
                    r += 1

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
