import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label1 = QLabel("Click in this window")

        self.setCentralWidget(self.label1)

    def mouseMoveEvent(self, e):
        self.label1.setText("mouseMoveEvent")

    def mousePressEvent(self, e):
        self.label1.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label1.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label1.setText("mouseDoubleClickEvent")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()