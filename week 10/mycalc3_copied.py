from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout
import itertools


class Button(QToolButton):
    def __init__(self, text: str, onClicked: callable):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(onClicked)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("My Calculator")

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.setLayout(mainLayout)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        # Display 를 mainLayout의 0행 0열에 세로로 한칸, 가로로 2칸의 크기로 배치한다.
        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        # Number Layout
        numLayout = QGridLayout()
        # 버튼들에 들어갈 텍스트를 만든다. [7, 8, 9, 4, 5, 6, 1, 2, 3, 0, '.', '=']
        # 참고 : itertools.chain 함수는 여러 iterable(반복 가능한 것들)들을 순서대로 연결해준다.
        buttonTexts = itertools.chain(range(7, 10), range(4, 7), range(1, 4), (0, '.', '='))
        # 레이아웃에 버튼들을 한줄에 3개씩 배치한다.
        alignButtonsOnGrid(numLayout, buttonTexts, unit=3, onClicked=self.buttonClicked)
        # Number Layout을 mainLayout의 1행 0열에 배치한다.
        mainLayout.addLayout(numLayout, 1, 0)

        # Operator Layout
        opLayout = QGridLayout()
        # 버튼들에 들어갈 텍스트를 만든다
        buttonTexts = ('*', '/', '+', '-', '(', ')', 'C')
        # 레이아웃에 버튼들을 한줄에 2개씩 배치한다.
        alignButtonsOnGrid(opLayout, buttonTexts, unit=2, onClicked=self.buttonClicked)
        # Operator Layout을 mainLayout의 1행 1열에 배치한다.
        mainLayout.addLayout(opLayout, 1, 1)

    def buttonClicked(self):
        button = self.sender()
        key = button.text()
        if key == '=':
            result = str(eval(self.display.text()))
            self.display.setText(result)
        elif key == 'C':
            self.display.clear()
        else:
            self.display.setText(self.display.text() + key)


# 버튼 GridLayout 에
def alignButtonsOnGrid(layout: QGridLayout, texts, unit: int, onClicked: callable):
    '''
    layout의 왼쪽 위부터 시작해 오른쪽으로 버튼들을 배치하는 메서드이다.
    즉, 한 줄에 unit 개의 버튼들을 배치하고, 줄이 꽉 차면 아랫줄로 이동해 배치한다.

    :param layout: 버튼들을 올려놓을 QGridLayout 객체
    :param texts: 버튼들을 생성하는 데 필요한 텍스트
    :param unit: 한 줄에 가능한 버튼의 수. 즉, layout의 열(column) 수
    :param onClicked: Button 생성자에 인자로 주어질 callback [click 이벤트 핸들러]
    '''
    for i, text in enumerate(texts):
        '''
        때로, for문에 range()를 쓰지 않지만, 반복하면서 인덱스가 필요한 경우가 있다.
        이럴때 enumerate 함수를 쓰면 인덱스까지 사용할수 있어서 좋다.
        (유의 : 여기서 자료구조 안의 인덱스가 아니라 단순히 for 문이 몇번의 반복인지를 의미한다.)
        이 경우에는 text는 texts 안의 요소들이고 i는 논리적인 인덱스이다.
        '''
        button = Button(str(text), onClicked)
        layout.addWidget(button, i // unit, i % unit)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
