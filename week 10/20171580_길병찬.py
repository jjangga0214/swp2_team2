import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qgui
from PyQt5.QtCore import Qt
import sys
import itertools


def add_widgets(widgets, layout, col_size):
    for i, widget in enumerate(reversed(widgets)):
        if widget is None:
            continue

        row = i // col_size
        col = abs(i % col_size - col_size)
        layout.addWidget(widget, row, col)


class CalculatorView(qtw.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.display = CalculatorView._create_display()

        num_layout = qtw.QGridLayout()
        self.num_btns = CalculatorView._create_btns([0, ".", "="] + list(range(1, 10))
                                                    , handler=self.append_on_display
                                                    , ishandlable=lambda i, btn: i is not 2)
        self.num_btns[2].clicked.connect(self.calc)
        add_widgets(self.num_btns, num_layout, 3)

        cmd_layout = qtw.QGridLayout()
        self.cmd_btns = CalculatorView._create_btns(("C", None, "(", ")", "+", "-", "*", "/",)
                                                    , handler=self.append_on_display)
        self.cmd_btns[0].clicked.connect(lambda: self.display.setText(""))
        add_widgets(self.cmd_btns, cmd_layout, 2)

        main_layout = qtw.QGridLayout()
        main_layout.addWidget(self.display, 0, 0, 1, 2)
        main_layout.addLayout(num_layout, 1, 0)
        main_layout.addLayout(cmd_layout, 1, 1)
        main_layout.setSizeConstraint(qtw.QLayout.SetFixedSize)

        self.setLayout(main_layout)
        self.setWindowTitle("My Calculator")
        self._register_shortcuts()

    def _register_shortcuts(self):
        btns = itertools.chain(self.num_btns, self.cmd_btns)
        for btn in filter(lambda btn: btn is not None, btns):
            shortcut = qtw.QShortcut(qgui.QKeySequence(btn.text()), self)
            shortcut.activated.connect(btn.click)

    @staticmethod
    def _create_display():
        display = qtw.QLineEdit()
        display.setReadOnly(True)
        display.setAlignment(Qt.AlignRight)
        display.setMaxLength(55)
        display.setFixedHeight(50)

        font = qgui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        display.setFont(font)
        return display

    @staticmethod
    def _create_btns(btns_, *, handler: callable, ishandlable: callable = lambda i, btn: True):
        btns = tuple(map(lambda el: el if el is None else Button(el), btns_))
        for i, btn in enumerate(btns):
            if btn is not None and ishandlable(i, btn):
                btn.clicked.connect(handler)
        return btns

    def append_on_display(self):
        btn_clicked = self.sender()
        self.display.setText(self.display.text() + btn_clicked.text())

    def calc(self):
        statement = self.display.text()
        if statement is "":
            return

        try:
            # FIXME : eval 은 취약할 수 있습니다.
            result = eval(statement)
        except (SyntaxError, TypeError):
            self.display.setText("")
            self._warning("식이 부적절합니다. 다시 입력해주세요.")
            return
        except ZeroDivisionError:
            self._warning("0으로 나눌 수 없습니다.")
            return
        self.display.setText(str(int(result) if int(result) == result else result))

    def _warning(self, msg: str, title: str = "입력값 오류"):
        qtw.QMessageBox.question(self, title, msg, qtw.QMessageBox.Yes)


class Button(qtw.QToolButton):
    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(qtw.QSizePolicy.Expanding,
                           qtw.QSizePolicy.Preferred)
        self.setText(str(text))

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    view = CalculatorView()
    view.show()
    sys.exit(app.exec_())
