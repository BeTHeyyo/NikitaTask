import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QMenu, QApplication
from PyQt5.QtCore import QSize    

class MyTableWidget(QMainWindow):

    def __init__(self, name='Table1', parent=None):
        super().__init__()
        self.name = name

    def contextMenuEvent(self, event):
        menu = QMenu(self)

        Action = menu.addAction("I am a %s Action" %self.name)
        Action.triggered.connect(self.printName)

        menu.exec_(event.globalPos())

    def printName(self):
        print ("Action triggered from %s" %self.name)


class Main(QWidget):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        layout = QVBoxLayout(self)

        self.table1 = MyTableWidget(name='Table1', parent=self)
        self.table2 = MyTableWidget(name='Table2', parent=self)

        layout.addWidget(self.table1)
        layout.addWidget(self.table2)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()

    app.exec_()
