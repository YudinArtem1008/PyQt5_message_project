import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI files/UI1.ui', self)
        self.findButton.clicked.connect(self.find_users)
        self.label.hide()

    def find_users(self):
        if self.lineEdit.text() == '':
            self.label.setText("Для начала введите номер или id контакта")
            self.label.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(open('styles/label.css', 'r').read())
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
