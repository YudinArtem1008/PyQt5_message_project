import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

from load import *


class MyWidget(QMainWindow):
    def __init__(self, theme):
        super().__init__()
        self.theme = theme
        uic.loadUi('UI files/UI1.ui', self)
        self.findButton.clicked.connect(self.find_users)
        self.label.hide()
        self.theme_button.clicked.connect(lambda: print(self.theme.data))
        self.listWidget.addItem("Test")

    def find_users(self):
        if self.lineEdit.text() == '':
            self.label.setText("Для начала введите номер или id контакта")
            self.label.show()
        else:
            self.label.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open('elements/styles/elements.css').read())
    ex = MyWidget(theme)
    ex.show()
    sys.exit(app.exec_())
